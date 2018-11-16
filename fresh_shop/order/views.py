from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse

from cart.models import ShoppingCart
from fresh_shop.settings import PAGE_NUMBER
from order.models import OrderGoods, OrderInfo
from user.models import UserAddress


def order(request):
    if request.method == 'POST':
        # 1. 从购物车表中取出当前登录系统用户且is_select为1的商品信息
        user_id = request.session.get('user_id')
        carts = ShoppingCart.objects.filter(user_id=user_id,
                                            is_select=1).all()
        # 计算总金额
        order_mount = 0
        for cart in carts:
            order_mount += int(cart.nums) * int(cart.goods.shop_price)
        # 2. 创建订单
        order = OrderInfo.objects.create(user_id=user_id,
                                         order_sn='',
                                         order_mount=order_mount)
        # 3. 创建订单详情信息
        for cart in carts:
            OrderGoods.objects.create(order=order,
                                      goods=cart.goods,
                                      goods_nums=cart.nums)
        # 4. 删除购物车中已经下单的商品信息
        carts.delete()
        return JsonResponse({'code': 200, 'msg': '请求成功'})


def user_order(request):

    if request.method == 'GET':
        user = request.user
        # 获取分页
        try:
            # 如果page参数不能转化为int类型，则异常，默认page为1
            page = int(request.GET.get('page',1))
        except:
            page = 1
        # 获取当前用户所有的订单信息
        order_info = OrderInfo.objects.filter(user=user)
        paginator = Paginator(order_info, PAGE_NUMBER)
        order_info = paginator.page(page)
        order_status = OrderInfo.ORDER_STATUS
        return render(request, 'user_center_order.html', {'order_info': order_info, 'order_status': order_status})


def user_order_site(request):

    if request.method == 'GET':
        user = request.user
        user_addresses = UserAddress.objects.filter(user=user).order_by('-id')

        return render(request, 'user_center_site.html', {'user_addresses': user_addresses})