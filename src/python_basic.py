from datetime import datetime, date, time, timedelta
##测试数据
product_1={'product_id':1001,
        'name':'Vt1',
        'price':150,
        'number':3
}
product_2={'product_id':1002,
        'name':'Vt2',
        'price':160,
        'number':2
}
product_3={'product_id':1003,
        'name':'Vt3',
        'price':170,
        'number':1
}
product_4={'product_id':1004,
           'name':'Vt4',
           'price':180,
           'number':0
}
product_5={'product_id':1005,
        'name':'vt5',
        'price':190,
        'number':0
}

customer={
    "customer_id":2001,
    "name":"XX公司",
    "level":"普通客户"
}

order_1={
       'order_id':3001,
       'customer_id':2001,
       'product_id':1001,
       'order_date':datetime(2026, 11, 15, 10, 30, 0),
       'order_num':4,
       'price':150,
       'order_sum':750,
       'order_status':'未出库'
}



products_list=[product_1,product_2,product_3,product_4,product_5]


#库存检查
def stock_check(order,product_list):
  order_num= order.get('order_num')
  product_id = order.get('product_id')
  for d in product_list:
    if(d.get("product_id")==product_id):
      return d.get("number")>=order_num
  


##计算订单总价
def order_process(order,product_list):
  ##基础检测
  if not order:
    return "请输入订单！"
  if not product_list:
    return "没有商品信息！"
  product_id = order['product_id']
 
  if not any(d.get("product_id") == product_id for d in product_list):
    return "没有该商品！"
  
  if not stock_check(order,product_list):
    return "该商品库存不足！"
  
  
  ##订单校验
  num=order['order_num']
  price=order['price']
  if num<1:
    return "订单商品数量不得小于等于0"
  if price<0:
      return "商品单价不得为负数"
   
  return "该订单总价为:"+str(num*price)  
  


                              
  
    
##输出结果
print(order_process(order_1,products_list))


  