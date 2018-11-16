from django.shortcuts import render

from goods.models import Goods, GoodsCategory
from utils.function import login_required


# @login_required
def index(request):
    if request.method == 'GET':
        goods = Goods.objects.all()
        types = GoodsCategory.CATEGORY_TYPE
        goods_dict = {}
        for type in types:
            goods_list = []
            count = 0
            for good in goods:
                # 判断商品分类和商品对象
                if count < 4:
                    if type[0] == good.category_id:
                        goods_list.append(good)
                        count += 1
            # {'新鲜水果':[], '猪牛羊肉':[]....}
            goods_dict[type[1]] = goods_list
        return render(request, 'index.html', {'goods_dict': goods_dict})


def detail(request, id):
    if request.method == 'GET':
        # 查看商品详情，返回商品对象
        goods = Goods.objects.filter(pk=id).first()
        return render(request, 'detail.html', {'goods': goods})
