from django.db import models

class Contact(models.Model):
    cnt_id     = models.AutoField(primary_key=True) 
    from_name  = models.CharField(max_length=50)
    from_email = models.CharField(max_length=50)
    subject    = models.CharField(max_length=250)
    message    = models.TextField(max_length=1150)

    def __str__(self):
        return self.from_name