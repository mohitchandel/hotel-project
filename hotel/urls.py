from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('', include('contact.urls')),
    path('accomodation', views.accomodation, name='accomodation')
]
