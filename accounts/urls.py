from django.conf import settings
from . views import *
from django.urls import path
from accounts import views

urlpatterns=[
    path('index/',index,name="index"),
    path('studentregister/',studentregister,name="studentregister"),
    path('studentlogin/',studentlogin,name="studentlogin"),
    path('studentlogout/',studentlogout,name="studentlogout"),
    path('profile/',profile,name="profile"),
    path('change_password/',views.change_password,name="changepassword"),
    
]

