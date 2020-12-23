from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

from .models import Billing, Order

   
class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['product', 'buying_price', 'quantity', 'value_added_tax', 'sold_at', 'total']
        
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'item', 'price']
        