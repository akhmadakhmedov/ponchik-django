from django import forms
from django.db import models
from django.forms import fields
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'phone_number', 'email', 'address_line_1', 'address_line_2',  'city', 'state','order_note']