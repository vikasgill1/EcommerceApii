from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import BooleanField
# from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    mobile_no=models.CharField(max_length=12)
    address=models.TextField(max_length=300)
    zip_code=models.IntegerField(default=True)
    city=models.CharField(max_length=100)
    def __str__(self):
        return self.username


class Category(models.Model):
    name=models.CharField(max_length=120)
    cate_img=models.ImageField(upload_to='application/images/category')
    desc_category=models.CharField(max_length=300)
    def __str__(self):
        return self.name
class SubCategory(models.Model):
    name=models.CharField(max_length=130)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='application/images/subcategory')
    desc_subcategory=models.CharField(max_length=300)
    def __str__(self):
        return self.name
        
class Product(models.Model):
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=350)
    price=models.IntegerField()
    add_card=models.BooleanField(default=False)
    pro_quantity=models.IntegerField(default=0)
    image=models.ImageField(upload_to='application/images/product')
    product_desc=models.CharField(max_length=300)
    publish_date=models.DateField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product)
    add_card=models.BooleanField(default=False)
    pro_quantity=models.IntegerField(default=0)
    total=models.IntegerField()

class Favorite_item(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product)
    favorite=models.BooleanField(default=False)
    



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price=models.PositiveIntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    transaction_id=models.CharField(max_length=50)
    payment_mode=models.CharField(max_length=8,choices=(('1','paytm'),('2','paypal'),('3','debit card'),('5','credit card'),('6','Netbanking')))
    is_payment_successful=models.BooleanField()
    def __str__(self):
        return self.transaction_id


class OrderItem(models.Model):
	cart = models.OneToOneField(Cart, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200 )
    status=models.CharField(max_length=6,default='2',choices=(('1','success'),('2','pending'),('3','cancel')))
    date=models.DateField()
    def __str__(self):
        return self.city
    
    