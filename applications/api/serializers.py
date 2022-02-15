

from rest_framework.serializers import ModelSerializer

from ..models import  *

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        read_only={'password'}

class CategorySeriallizers(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class SubCategorySeriallizers(ModelSerializer):
    class Meta:
        model=SubCategory
        fields='__all__'

 
class ProductSerialezer(ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class CartSerialezer(ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'



class OrderitemSerilizer(ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'
 


class shippingSerializer(ModelSerializer):
    class Meta:
        model=ShippingAddress
        fields='__all__'


        
class OrderSerializers(ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"
             