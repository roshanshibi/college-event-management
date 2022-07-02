from . views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views
from events import views
from .views import GeneratePdf

urlpatterns=[
    path('events/',events,name = "events"),
    path('booking/<int:id>',booking,name="booking"),
    path('departments/',departmentlist,name="departmentlist"),
    path('myevents/',myevents,name="myevents"),
    path('deletebook/<int:id>',deletebooking,name="deletebook"),
    path('messages/',notification,name="notification"),
    path('pdf/<int:id>', GeneratePdf.as_view(),name="pdf"),
    path('results/',eventresult,name="results"),
    path('event_details/<int:id>',event_details,name="eventdetails"),
    
    #path('feedback/',feedbackViews,name="feedback"),

] 



urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)