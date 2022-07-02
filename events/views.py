from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from . models import *
from accounts.models import *
from django.contrib.auth import authenticate,login,get_user_model
from django.views.generic import ListView
from django.db.models import Q, query
from django.contrib.postgres.search import SearchVector

#for html to pdf conversion
from django.template.loader import get_template
from .utils import render_to_pdf 
from django.views.generic import View



#Used to display and categorize events
def events(request):
    categories = eventcategory.get_all_categories()
    # dept = Departments.objects.all()
    #eventss = Events.get_all_events()
    categoryID = request.GET.get('category1')
    if categoryID:
        eventss = Events.get_all_events_by_categoryid(categoryID)
    else:
        eventss = Events.get_all_events();
    
    # deptCategoryID = request.GET.get('dept1')
    # deptcategory = Events.get_all_events_by_department(deptCategoryID)
    # sid = request.GET.get('student_id')
    # book_count = Booking.get_booking_count(sid)
    # print(book_count)
    data = {}
    data['eventss'] = eventss
    data['categories'] = categories
    # data['deptcategory'] = deptcategory
    # data['dept'] = dept
    #data['book_count'] = book_count
    return render(request,'events.html',data )  






#To book an event
def booking(request, id):
    if Booking.objects.filter(event_id=id).exists():
         messages.info(request,'You already registered for this event')
         return redirect('events')
    else:
        Booking.objects.create(student_id=request.user.id, event_id=id)
        messages.info(request, 'Event joined successfully')
        return redirect('events')

    
    
    
    
    



#To display all departments
def departmentlist(request):
    Dept = Departments.objects.all()
    event1 = Events.objects.filter()
    values={
        'Dept':Dept,
        'event1' : event1,
        'values' : request.POST
    }
    if request.method == 'GET':
        return render(request,'department.html',values)
    
    

def myevents(request):
    if request.user.is_authenticated:
        student = request.user
        book = Booking.objects.filter(student=student)
    return render(request,'myevents.html',{'book':book})


# def deletebooking(request,id):
#     if request.user.is_authenticated:
#         student = request.user
#         deletebook = Booking.objects.filter(student=student,event_id=id).delete()
#     return render(request,'myevents.html',{'deletebook':deletebook})
#         #return redirect('events')


def deletebooking(request,id):
    deletebook = Booking.objects.get(pk=id)

    deletebook.delete()
    context = {"object":deletebook}
    return redirect('myevents')
    #return render(request,'myevents.html',{'deletebook':deletebook})
    #return render(request,'myevents.html',context)
    




def notification(request):
    messages1 = Notification.objects.all().order_by("-notification_time")
    values={'messages1':messages1,
     'values' : request.POST
    }
    return render(request,'messages.html',values)
   



class GeneratePdf(View):
     def get(self,request,id):
        
        data = {}
        # id = request.
      
        book = Booking.objects.get(pk=id)
        data['book'] = book
        #getting the template
        pdf = render_to_pdf('invoice.html',data)
        
      
        
        return HttpResponse(pdf,content_type='application/pdf')

    
# def invoiceView(request,id):
#     books = Booking.objects.filter(id=id)
#     data = {}
#     data['books'] = books
#     return render(request,'invoice.html',data)



def eventresult(request):
    results = Result.objects.all()
    if results:
        values = {'results':results,
    
                    'values' : request.POST}
        return render(request,'results.html',values)

    else:
        return HttpResponse("<h1>Not published yet!<h1>")



def event_details(request,id):
    eventdetails = Events.objects.get(pk=id)
    values = {'eventdetails':eventdetails,
    
            'values' : request.POST}
    return render(request,"eventdetails.html",values)



    
    


