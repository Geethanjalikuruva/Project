from django.urls import path
from .views import *
app_name='myapp'

urlpatterns = [
    path('register/',register,name='register'),
    path('home/',home,name='home'),
    path('doctors/',doctors,name='doctors'),
    path('patient/',patient,name='patient'),
    path('services/',services,name='services'),
    path('contactus/',contactus,name='contactus'),
    path('list/',list,name='list'),
    path('logout/',logout_view,name='logout'),
    path('login/',login_view,name='login'),
    path('appointment/',appointment,name='appointment'),
    
]
