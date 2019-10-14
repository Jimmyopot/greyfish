from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('billings/', views.BillingListView.as_view(), name='billings'),
    path('billing/<int:pk>/', views.BillingDetailView.as_view(), name='billing-detail'),
    path('billing/create/', views.BillingCreateView.as_view(), name='billing-create'),
    path('billing/update/<int:pk>/', views.BillingUpdateView.as_view(), name='billing-update'),
    path('billing/delete/<int:pk>/', views.BillingDeleteView.as_view(), name='billing-delete'),
    
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('order/update/<int:pk>/', views.OrderUpdateView.as_view(), name='order-update'),
    path('order/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order-delete'),
]