from django.shortcuts import render
from WebAsha.models import *
from django.http import HttpResponse
from .forms import *
from django.shortcuts import render, redirect
from django.conf import settings



# Create your views here.


def view_home(request):
    resp=render(request,'WebAsha/home.html')
    return resp


def view_doctos(request):
    resp=render(request,'WebAsha/doctors.html')
    return resp


def view_service(request):
    resp=render(request,'WebAsha/services.html')
    return resp

def view_contact(request):
    if request.method=="GET":
        resp=render(request,'WebAsha/contact.html')
        return resp
    elif request.method=="POST":
        if 'btnsend' in request.POST:
            contact1=contact()
            contact1.name=request.POST.get('name')
            contact1.email=request.POST.get('email')
            contact1.phone=request.POST.get('phone')
            contact1.subject= request.POST.get('subject')
            contact1.message=request.POST.get('message')
            contact1.save()
            resp = render(request,'webasha/thankyou.html')
            return resp
            
           
        
def view_thakyou(request):
    resp=render(request,'WebAsha/thankyou.html')
    return resp

def view_thanks(request):
    resp=render(request,'WebAsha/newsthanks.html')
    return resp


def view_appointment(request):
    if request.method=="GET":
        frm_unbound=bookingForm()
        d1={'form': frm_unbound}
        resp=render(request,"WebAsha/appointment.html",context=d1)
        return resp
    elif request.method == "POST":
        frm_bound=bookingForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            resp = render(request,'webasha/thankyou.html')
            return resp
            
        else:
            d1={'form': frm_bound}
            resp=render(request,"WebAsha/appointment.html",context=d1)
            return resp
            
    

def ear_treatment(request):
    return render(request, 'WebAsha/ear.html')

def blood_treatment(request):
    return render(request, 'WebAsha/blood.html')

def heart_treatment(request):
    return render(request, 'WebAsha/heart.html')

def vision_treatment(request):
    return render(request, 'WebAsha/vision.html')

def teeth_treatment(request):
    return render(request, 'WebAsha/teeth.html')

def general_treatment(request):
    return render(request, 'WebAsha/general.html')


def view_heart_health(request):
    return render(request,'WebAsha/hearthealth.html')

def view_diabeties(request):
    return render(request,'WebAsha/diabeties.html')

def view_management(request):
    return render(request,'WebAsha/management.html')

def view_vision_care(request):
    return render(request,'WebAsha/visioncare.html')

def view_ear_health(request):
    return render(request,'WebAsha/earhealth.html')

def view_testimonials(request):
    return render(request, 'WebAsha/testimonials.html')

def view_finance(request):
    return render(request, 'WebAsha/finance.html')

def view_our_cases(request):
    return render(request, 'WebAsha/our_cases.html')

def view_faq(request):
    return render(request, 'WebAsha/faq.html')

def view_consulting(request):
    return render(request, 'WebAsha/consulting.html')

def view_about(request):
    return render(request,'WebAsha/about.html')

def view_doctors(request):
    return render(request,'WebAsha/doctors.html')

def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'WebAsha/newsthanks.html')
    else:
        form = NewsletterSubscriptionForm()
        return render(request, 'WebAsha/base.html',{'form':form})

