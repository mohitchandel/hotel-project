from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('booking.urls')),
    path('about', views.about, name='about'),
    path('', include('contact.urls')),
]
