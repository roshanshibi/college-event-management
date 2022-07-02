from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields import DateTimeField
from django.utils import timezone
from accounts.models import *
from django.conf import settings
from django.utils.timezone import now



class eventcategory(models.Model):
    category = models.CharField(max_length=50)


    def __str__(self):
        return self.category

    @staticmethod
    def get_all_categories():
        return eventcategory.objects.all()


class Events(models.Model):
    event_name = models.CharField(max_length=50)
    category = models.ForeignKey(eventcategory, on_delete=models.CASCADE,default=1)
    description = models.TextField()
    venue = models.CharField(max_length=50)
    startdatetime = models.DateTimeField() 
    dept = models.ForeignKey(Departments,on_delete=models.CASCADE,default=1)
    event_head = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    img = models.ImageField(upload_to = 'Uploads')
    price = models.IntegerField()
    regtime = models.DateTimeField(null=True)
    no_of_seats = models.IntegerField(null=True)

    def __str__(self):
        return self.event_name



    @staticmethod
    def get_all_events():
        return Events.objects.all()


    @staticmethod
    def get_all_events_by_categoryid(category_id):
        if category_id:
            return Events.objects.filter(category = category_id)
        else:
            return Events.get_all_events();


    @staticmethod
    def get_all_events_by_department(dept_id):
        return Events.objects.filter(dept = dept_id)





class Booking(models.Model):
    student = models.ForeignKey(to=MyUser,on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    time = models.DateTimeField(default=now)

    @staticmethod
    def get_booking_count(student_id):
         return Booking.objects.filter(student = student_id).count()

        
    


class Feedback(models.Model):
    feedname = models.CharField(max_length=20)
    feedemail = models.EmailField(max_length=20,null=False)
    feedmsg = models.CharField(max_length=100)
   



class Notification(models.Model):
    notification = models.CharField(max_length=50)
    notification_time = models.DateTimeField(default=timezone.now)
   

class Result(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='Uploads')