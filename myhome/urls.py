from django.urls import path
from  .views import *

urlpatterns = [
         path('', home, name='home'),
         path('cart/', cart, name='cart'),
         path('checkout/', checkout, name='checkout'),
         path('contact/', contact, name='contact'),
         path('detail/', detail, name='detail'),
         path('shop/', shop, name='shop'),
         path('base/', base, name='base'),
]
