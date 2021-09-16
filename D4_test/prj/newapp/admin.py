from django.contrib import admin

# Register your models here.
from .models import Category, Product, Commenet

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Commenet)


