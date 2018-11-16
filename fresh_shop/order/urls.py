"""__author__ = 唐宏进 """
from django.conf.urls import url

from order import views

urlpatterns = [
    # 下单
    url(r'^order/', views.order, name='order'),
    # 订单中心
    url('^user_oder/', views.user_order, name='user_order'),
    # 收货地址
    url('user_order_site/', views.user_order_site, name='user_order_site'),
]