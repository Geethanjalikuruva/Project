from django.db import models

# Create your models here.
class docotrmodel(models.Model):
  name=models.CharField(max_length=30)
  specialization=models.CharField(max_length=30)
  Experience=models.IntegerField()
  image=models.ImageField(upload_to='imagess/')
  def __str__(self):
     return self.name
  



class patientmodel(models.Model):
  First_name=models.CharField(max_length=30,null=True)
  Last_name=models.CharField(max_length=30)
  Gender=models.CharField(max_length=20)
  email=models.EmailField(null=True)
  address=models.CharField(max_length=30)



class servicesmodel(models.Model):
  sevicename=models.CharField(max_length=30)
  serviceimage=models.ImageField(upload_to='images/')
  def __str__(self):
    return self.sevicename

  
  

class Appointment(models.Model):
  Full_Name=models.CharField(max_length=30)
  doctor = models.ForeignKey(docotrmodel, on_delete=models.CASCADE)
  service = models.ForeignKey(servicesmodel, on_delete=models.CASCADE)
  date = models.DateField()
  time = models.TimeField()
  def __str__(self):
        return f"{self.Full_Name} - {self.doctor} - {self.service} - {self.date} - {self.time}"



  


