from django.db import models

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    arval_date = models.CharField(max_length=40, default=None)
    dep_date   = models.CharField(max_length=40, default=None)
    persons    = models.CharField(max_length=40, default=None)
    persons    = models.CharField(max_length=40, default=None)
    child      = models.CharField(max_length=40, default=None)    
    room_type  = models.CharField(max_length=40, default=None)
    total_rooms = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=40, default=None)
    phone_num  = models.CharField(max_length=40, default=None)

    def __str__(self):
        return self.customer_name

    
