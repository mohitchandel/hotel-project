from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Contact


def contact(request):
    if request.method == "POST":
        from_name  = request.POST.get('from_name','')
        from_email = request.POST.get('from_email','')
        subject    = request.POST.get('subject','')
        message    = request.POST.get('message','')
        print(from_name, from_email, subject, message)
        contact = Contact(from_name=from_name, from_email=from_email, subject=subject, message=message)
        contact.save()
    '''if request.method =='POST':
            email   = request.POST.get('email', '')
            subject = "Booking"
            name    = request.POST.get('name','')
            message = "Thanks for Contacting ",from_name
            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, ['mohitchandel639@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                    return HttpResponseRedirect('/contact/thanks/')
            else:
                # In reality we'd use a form class
                # to get proper validation errors.
                return HttpResponse('Make sure all fields are entered and valid.')'''    
    return render(request, "contact.html",)