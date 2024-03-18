from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from .forms import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout


def register(request):
    if request.method=="POST":
            user=User.objects.filter(username=request.POST['username'])
            if user.exists():
                  messages.info(request,'User Laready exist')
                  return redirect(reverse('myapp:register'))

            form=RegistrationForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect(reverse('myapp:login'))
    f=RegistrationForm()
    return render(request,'register.html',context={'form':f})

def login_view(request):
    if request.method=='POST':
            form=LoginForm(request.POST)
            if form.is_valid():
                user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                if user:
                      login(request,user)
                      return redirect(reverse('myapp:home'))
                else:
                      messages.error(request,'Invalid username or password')
                      return redirect(reverse('myapp:login'))
    f=LoginForm()
    return render(request,'login.html',context={'form':f})


@login_required(login_url='myapp:login')
def home(request):
      return render(request,'home.html')

@login_required(login_url='myapp:login')
def doctors(request):
      data=docotrmodel.objects.all()
      info={'data':data}
      return render(request,'doctors.html',context=info)


@login_required(login_url='myapp:login')
def patient(request):
      if request.method=="POST":
            form=patientForm(request.POST)
            if form.is_valid():
                  form.save(commit=True)
      form=patientForm()
      return render(request,'patient.html',context={'form':form})

@login_required(login_url='myapp:login')  
def services(request):
      data1=servicesmodel.objects.all()
      info1={'data1':data1}
      return render(request,'services.html',context=info1)

@login_required(login_url='myapp:login')
def appointment(request):
      if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            Full_Name = form.cleaned_data['Full_Name']
            doctor = form.cleaned_data['doctor']
            service = form.cleaned_data['service']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            appointment = Appointment(
                Full_Name=Full_Name,
                doctor=doctor,
                service=service,
                date=date,
                time=time
            )
            appointment.save()
            return redirect(reverse('myapp:appointment'))
      else:
        form = AppointmentForm()
    
      appointments = Appointment.objects.all()
      return render(request, 'appointment.html', {'form': form, 'appointments': appointments})
            

@login_required(login_url='myapp:login')
def contactus(request):
      return render(request,'contactus.html')


@login_required(login_url='myapp:login')
def list(request):
      data2=Appointment.objects.all()
      infor={'data2':data2}
      return render(request,'list.html',context=infor)


def logout_view(request):
      logout(request)
      return redirect(reverse('myapp:login'))
             