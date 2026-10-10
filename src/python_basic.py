good_1={'name':'面包','price':14,'number':3}
good_2={'name':'蛋糕','price':50,'number':2}
good_3={'name':'牛奶','price':20,'number':1}
goods_list=[good_1,good_2,good_3]


def caculate_item_value(product):
  total = 0  
  for x in product:
    total+=(x['number']*x['price'])
  return str(total)

def sum_item_value(product):
  total = 0
  for x in product:
      total+=x['price']
  return str(total)

print("商品单价之和："+caculate_item_value(goods_list)+'  '+"商品总价:"+sum_item_value(goods_list))

  