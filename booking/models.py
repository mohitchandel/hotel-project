from django.db import models

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=50, default='')
    arv_date = models.DateField()
    dep_dte  = models.DateField()
    adults   = models.CharField(max_length=20, default='')
    child    = models.CharField(max_length=20, default='')
    child_room = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.cust_name
