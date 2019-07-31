from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpRequest, HttpResponse
from django.core.mail import EmailMessage
from django.core import mail
from .models import Booking
from django.core.mail import send_mail


def index(request):
    def send_email(request):
        if request.method == "POST":
            booking_id    = request.POST.get('booking_id', '')
            arval_date    = request.POST.get('arval_date', '')
            dep_date      = request.POST.get('dep_date', '')
            customer_name = request.POST.get('customer_name', '')
            persons       = request.POST.get('persons', '')
            child         = request.POST.get('child', '')    
            email         = request.POST.get('email', '')
            room_type     = request.POST.get('room_type', '')
            total_rooms   = request.POST.get('total_rooms', '')
            phone_num     = request.POST.get('phone_num', '')
            price         = request.POST.get('price', '')
            print(arval_date, dep_date, customer_name, persons, child, email, room_type, total_rooms,  phone_num, price)
            booking = Booking(arval_date=arval_date, dep_date=dep_date, customer_name=customer_name, persons=persons,  child=child, email=email, room_type=room_type, total_rooms=total_rooms, phone_num=phone_num, price=price  )
            booking.save()
    return render(request, 'index.html')