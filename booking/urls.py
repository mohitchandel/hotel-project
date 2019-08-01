from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('thanku', views.thanku, name='thanku'),
]