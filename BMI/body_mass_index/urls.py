from django.urls import path
from . import views

app_name = 'body_mass_index'

urlpatterns = [
    path('', views.body_mass_index_view, name='home'),
]