good_1={'name':'面包','price':14,'number':3}
good_2={'name':'蛋糕','price':50,'number':2}
good_3={'name':'牛奶','price':20,'number':1}
good_null={'name':'三明治','price':15,'number':-1}
good_4={'name':'咖啡','price':20,'number':0}
goods_list=[good_1,good_2,good_3,good_4]
goods_list_error=[good_null]
goods_list_null=[]


def sum_goods_value(product):
  if not product:
    return "没有商品！"
  total = 0 
  for x in product:
    if(x['number']<0):
      return '错误！'+x['name']+'数量为负数！'
    total+=(x['number']*x['price'])
  return "商品总价："+str(total)

def cal_goods_value(product):
  if not product:
      return "没有商品！"
  total = 0
  for x in product:
    if(x['number']<0):
          return '错误！'+x['name']+'数量为负数！'
    total+=x['price']
  return "商品单价和:"+str(total)

print("正确结果:"+sum_goods_value(goods_list)+'  '+cal_goods_value(goods_list))
print("错误结果:"+sum_goods_value(goods_list_error)+'   '+cal_goods_value(goods_list_error))
print("空结果:"+sum_goods_value(goods_list_null)+'   '+cal_goods_value(goods_list_null))

  