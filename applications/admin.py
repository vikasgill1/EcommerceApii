from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favorite_item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(ShippingAddress)