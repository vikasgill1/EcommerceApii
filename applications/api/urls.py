from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('user/',UserView)
# router1 = DefaultRouter()
# router1.register('category/',CategoryView)
# router2 = DefaultRouter()
# router2.register('subcategory/',SubCategoryView)
# router3 = DefaultRouter()
# router3.register('product/',ProductView)
# router4 = DefaultRouter()
# router4.register('order/',OrderView)
# router5 = DefaultRouter()
# router5.register('shipping/',ShippingView)




urlpatterns = [
    # path('user/', include(router.urls)),
    # path('category/', include(router1.urls)),
    # path('subcategory/', include(router2.urls)),
    # path('product/', include(router3.urls)),
    # path('order/', include(router4.urls)),
    # path('shipping/', include(router5.urls)),
    path('user/<int:pk>',UserView1),
    path('Product/<int:pk>',ProductView),
    path('category/<int:pk>',category),
    path('subcatory/<int:pk>',subcategory),
    path('orderitem/<int:pk>',orderitem),
    path('order/<int:pk>',Order),
    path('shipping/<int:pk>',Shipping),
    path('user/<int:pk>',UserView1),
    path('user/<int:pk>',UserView1),

]
