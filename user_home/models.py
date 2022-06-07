from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductDetails(models.Model):
    sl_no = models.IntegerField(null=True)
    brand = models.TextField()
    serial_number = models.TextField()
    purchase_date = models.DateField()
    model_number = models.TextField()
    device_type = models.TextField(null=True)
    host_name = models.TextField(null=True)
    project = models.TextField(null = True)
    attachments = models.TextField(null = True)
    user_id = models.ForeignKey(User,related_name='user_info',on_delete=models.CASCADE,null=True)



