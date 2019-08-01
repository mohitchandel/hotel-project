from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpRequest, HttpResponse
from django.core.mail import EmailMessage
from django.core import mail
from .models import Booking
from django.core.mail import EmailMessage

def index(request):
        if request.method == "POST":
            booking_id    = request.POST.get('booking_id', '')
            arval_date    = request.POST.get('arval_date', '')
            dep_date      = request.POST.get('dep_date', '')
            customer_name = request.POST.get('customer_name', '')
            persons       = request.POST.get('persons', '')   
            email         = request.POST.get('email', '')
            room_type     = request.POST.get('room_type', '')
            phone_num     = request.POST.get('phone_num', '')
            price         = request.POST.get('price', '')
            print(arval_date, dep_date, customer_name, persons, email, room_type, phone_num, price)
            booking = Booking(arval_date=arval_date, dep_date=dep_date, customer_name=customer_name, persons=persons, email=email, room_type=room_type, phone_num=phone_num, price=price  )
            booking.save()

            email = EmailMessage('Booking', 'message', to=[email])
            email.send()

        return render(request, 'index.html')
        
def thanku(request):
    return render(request, 'thanku.html')


