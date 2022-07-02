from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import *
from events.models import Feedback, Notification
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,get_user_model, update_session_auth_hash
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm



#To display index page
def index(request):
    # if request.Method == "GET":
    #     return render(request,'base.html')
    count = Notification.objects.count()
    if request.method == "POST":
         feedname = request.POST.get('feedname')
         feedemail = request.POST.get('feedemail')
         feedmsg = request.POST.get('feedmsg')
         Feedback.objects.create(feedname=feedname,feedemail=feedemail,feedmsg=feedmsg).save()
         print("Sent")
         return render(request,'base.html')
    return render(request,'base.html', {"count":count})







#For user registration
def studentregister(request):
    Departmentss = Departments.objects.all()
    context = {
        'Departmentss' : Departmentss,
        'values' : request.POST
    }

    if request.method == 'GET':
        return render(request,'register.html', context )

        
    MyUser = get_user_model()
    if request.method == 'POST':
        student_name = request.POST['student_name']
        collegeid = request.POST['collegeid']
        dept_name = request.POST['dept_name']
        phone = request.POST['phone']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if MyUser.objects.filter(username=username).exists():
            messages.info(request,'Username taken!!')
            return redirect('studentregister')
        elif MyUser.objects.filter(email=email).exists():
            messages.info(request,'Email already exists!!')
            return redirect('studentregister')
        elif MyUser.objects.filter(collegeid=collegeid).exists():
            messages.info(request,'College Id already exists')
        else:
            user = MyUser.objects.create_user( email=email, username=username, password=password, student_name=student_name, collegeid=collegeid, dept_name=dept_name, phone=phone )
            user.save()
            print("User created")
            messages.info(request,'Account created successfully')
            return render(request,'register.html')
    
    
    else: 
        return render(request,'register.html')

    return render(request,'register.html')





#For login
def studentlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request,username=username, password=password)
        print('USER:',user)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid Username or Password!!')
            return redirect('studentlogin')

    else:
        return render(request,'login.html')






#For logout
def studentlogout(request):
    auth.logout(request)
    return redirect('index')


def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('index')

    


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changepassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {
        'form': form
    })



