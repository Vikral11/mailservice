from django.shortcuts import render, HttpResponseRedirect
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    if (request.method=="POST"):
        global mailing_list
        global mail
        mailing_list=request.POST.get("emails")
        mail=request.POST.get("mail")
        return HttpResponseRedirect("/otp_send")
    return render(request, "index.html")

def email_verify_otp_send(request):
    if(request.method=="POST"):
        global verify_mail
        verify_mail= request.POST.get("emails")
        try:
                    
            otp= randint(100000,999999)
            request.session["User"]= verify_mail
            request.session["num"]= otp
            subject = 'identitiy verification'
            message = """your OTP is %d
                    """%otp
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [verify_mail] 
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponseRedirect("/email_verify_otp_check")
        except:
            messages.error(request,"Please Enter Registered Email")
    return render(request, "otpsend.html")


def email_verify_otp_check(request):
    if(request.method=="POST"):
        otp= int(request.POST.get("OTP"))
        num= int(request.session.get("num"))
        if(num==otp):
            return HttpResponseRedirect("/send_mail")
        else:
            return render(request,"hello.html")

    return render(request , "idverify.html")


def sendMail(request):
    x=data()
    x.email=verify_mail
    x.mail=mail
    x.mail_list=mailing_list
    x.save()
    subject = 'no-reply'
    x=mailing_list.split(", ")
    email_from = settings.EMAIL_HOST_USER
    recipient_list = x 
    message= mail
    send_mail(subject, message , email_from, recipient_list )
    return HttpResponseRedirect("/")