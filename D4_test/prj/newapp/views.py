from django.shortcuts import render

# Create your views here.

from .models import Product, Commenet
from django.views.generic import ListView
from django.core.paginator import Paginator
from .filters import ProductFilter, F, C, X
from django.contrib.auth.models import User

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_filter(self):
        return ProductFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter()
        }

def user_list(request):
    f = F(request.GET, queryset=User.objects.all())
    return render(request, 'user_t.html', {'filter': f})

def product_list(request):
    c = C(request.GET, queryset=Product.objects.all())
    return render(request, 'product_t.html', {'filter': c})

def comment_list(request):
    x = X(request.GET, queryset=Commenet.objects.all())
    return render(request, 'comment_t.html', {'filter': x})
