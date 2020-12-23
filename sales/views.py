from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.db.models import Sum

from .models import Billing, Order
from .forms import BillingForm, OrderForm


# CBV for Billing
class BillingListView(ListView):
    model = Billing
    template_name = 'sales/billing_list.html'
    context_object_name = 'my_object'
    

class BillingDetailView(DetailView):
    model = Billing
    template_name = 'sales/billing_detail.html'
    
    
class BillingCreateView(CreateView):
    model = Billing
    fields = ['product', 'buying_price', 'quantity', 'value_added_tax', 'sold_at', 'total']
    template_name = 'sales/billing_create.html'
    
    def get(self, request, *args, **kwargs):
        form = BillingForm()  # this is GET request
        context = {
            'form': form
        }
        return render(request, "sales/billing_create.html", context)
    
    def post(self, request, *args, **kwargs):
        form = BillingForm() 
        if request.method == 'POST':
            form = BillingForm(request.POST or None)
        
            if form.is_valid():
                value_added_tax = 16.0
                tax = (value_added_tax / 100) 
                quantity = form.cleaned_data["quantity"]
                buying_price = form.cleaned_data["buying_price"]
                value_added_tax = form.cleaned_data["value_added_tax"]
                total = (buying_price * tax + buying_price) * (quantity)
                form.fields['total'].initial = total
                #form.fields['total'].widgets.attrs['readonly']=True
                
                context = {
                    'form': form
                }
                return render(request, "sales/billing_create.html", context)
            else: 
               form.fields['total']. initial = total
               context = {'form': form}
               return render(request, "sales/billing_create.html", context)

    
    def get_success_url(self):
        return reverse('sales:billings')
   
class BillingUpdateView(UpdateView):
    model = Billing
    fields = ['product', 'buying_price', 'quantity', 'value_added_tax', 'sold_at', 'total']
    template_name = 'sales/billing_create.html'
    
    def get(self, request, *args, **kwargs):
        form = BillingForm()  # this is GET request
        context = {
            'form': form
        }
        return render(request, "sales/billing_create.html", context)
    
    def post(self, request, *args, **kwargs):
        form = BillingForm() 
        if request.method == 'POST':
            form = BillingForm(request.POST or None)
        
            if form.is_valid():
                value_added_tax = 16.0
                tax = (value_added_tax / 100) 
                quantity = form.cleaned_data["quantity"]
                buying_price = form.cleaned_data["buying_price"]
                value_added_tax = form.cleaned_data["value_added_tax"]
                total = form.cleaned_data["total"]            
                my_total = (buying_price * tax + buying_price) * (quantity)
                total = my_total
                
                context = {
                    'my_total': total,
                    'form': form
                }
                return render(request, "sales/billing_create.html", context)
            else:
                context = {
                    'form': form
                }
                return render(request, "sales/billing_create.html", context)
            
    

class BillingDeleteView(DeleteView):
    model = Billing
    template_name = 'sales/billing_delete.html'
    
    def get_success_url(self):
        return reverse('sales:billings')
    
    
    
    
    
# CBV for Order
class OrderListView(ListView):
    model = Order
    template_name = "sales/order_list.html"
    context_object_name = "orders"
    
    
class OrderDetailView(DetailView):
    model = Order
    template_name = "sales/order_detail.html"
    
    def get_success_url(self):
        return reverse('sales:orders')
    
    
class OrderCreateView(CreateView):
    model = Order
    fields = ['name', 'item', 'price']
    template_name = "sales/order_form.html"
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('sales:orders')
    
    
class OrderUpdateView(UpdateView):
    model = Order
    fields = ['name', 'item', 'price']
    template_name = "sales/order_form.html"
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    
class OrderDeleteView(DeleteView):
    model = Order
    template_name = "sales/order_delete.html"
    
    def get_success_url(self):
        return reverse('sales:orders')

