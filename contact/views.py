from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import EmailMessage



def contact(request):
    if request.method == "POST":
        from_name  = request.POST.get('from_name','')
        from_email = request.POST.get('from_email','')
        subject    = request.POST.get('subject','')
        message    = request.POST.get('message','')
        print(from_name, from_email, subject, message)
        contact = Contact(from_name=from_name, from_email=from_email, subject=subject, message=message)
        contact.save()

        email = EmailMessage('Contact', 'Thanks for submiting your query we will get back soon', to=[from_email])
        email.send()   
         
    return render(request, "contact.html",)