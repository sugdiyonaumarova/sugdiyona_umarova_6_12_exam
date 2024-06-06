from django.contrib import admin
from blog.models import Product, Image, Attribute, Customer


admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Attribute)
admin.site.register(Customer)
