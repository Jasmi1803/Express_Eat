from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.core import mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from app.models import Contact
def home(request):
    return render(request,'index.html')
def home1(request):
    return render(request,'about.html')
def home2(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        message=request.POST.get("message")
        query=Contact(name=name,phone=phone,email=email,message=message)
        query.save()
         
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        email_message=mail.EmailMessage(f'Email from {name}',f'UserEmail : {email}\nUserPhoneNumber : {phone}\n\n\n QUERY : {message}',from_email,['jasmijome@gmail.com','jasmi182003@gmail.com'],connection=connection)
        email_client=mail.EmailMessage('ExpressEat ','Thanks For Reaching us',from_email,[email],connection=connection)

        connection.send_messages([email_message,email_client])
        connection.close()





        messages.info(request,"Thanks for Contacting Us")
        return redirect("contact.html")
        
    return render(request,'contact.html')
def home3(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            
            messages.success(request,"Login Success")
            return redirect("index.html")
        else:
            messages.error(request,"Invalid Credintials")
            return redirect("land.html")

    return render(request,'land.html')
def home4(request):
    if request.method=="POST":
        username=request.POST.get("username")  
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmPassword")
        if password !=confirmpassword:
           messages.warning(request,"Password is Incorrect")
           return redirect("signup.html")
        try:
            if User.objects.get(username=username):
                messages.info(request,"Username is Taken")
                return redirect("signup.html")
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email is Taken")
                return redirect("signup.html")
        except:
            pass
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"signup success Please Login")
        return redirect("land.html")
    return render(request,'signup.html')
    