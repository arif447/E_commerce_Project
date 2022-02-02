from django.shortcuts import render
# Import views
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Models
from App_Shop.models import Product
# Create your views here.
class Home(ListView):
    context_object_name = 'object_list'
    model = Product
    template_name = 'App_Shop/home.html'

class Product_detail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_details.html'

