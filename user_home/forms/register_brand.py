from django import forms
from django.contrib.auth.models import User
from user_home.models import ProductDetails
class ProductDetailsForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = ProductDetails
        fields = ('sl_no','brand','serial_number','purchase_date','model_number','device_type','project','host_name')