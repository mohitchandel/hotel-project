from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpRequest, HttpResponse
from django.core.mail import EmailMessage
from django.core import mail
from booking.models import Booking
from django.core.mail import send_mail


def about(request):
    return render(request, 'about.html')    

def contact(request):
    return render(request, 'contact.html')
  
