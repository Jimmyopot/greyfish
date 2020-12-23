import datetime
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import Sum


class Billing(models.Model):
    product = models.CharField(max_length=255)
    buying_price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    value_added_tax = models.IntegerField(default=16)
    sold_at = models.DateTimeField(default=timezone.now)
    total = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.product
    
    def get_absolute_url(self):
        return reverse("sales:billing-detail", kwargs={"pk": self.pk})
   
   
class Order(models.Model):
    name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
