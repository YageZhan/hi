x = 5
# declare 宣告 只有第一个创造的是宣告 之后重复出现的x只是改变
print(x)
x = 10
x = 1000
y = 2
# x y 这样的的东西教做菜variable 变数；100 1000 2 叫做value
# =等号理解为把右边存到左边 assignment设置指令
print(y)
print(x)
#==================================================
# data types (种类)
# 资料型别
# 1. 整数 integer int
# 2. 浮点数 (小数) float
# 3. 布林值 boolean bool (True, False)
# 4. 字串 string str (文字) 'Jade' 特色是都有单引号括住， 里面可以装任何东西，或什么都不装就是空字串
price = 10
pen = 0.38
rain = True 
name = 'Jade'
print(price)
print(pen)
print(rain)
print(name)
# 或者 用逗号空格分开 一起print出来
print(price, pen, rain, name)

#==================================================
name = input('请输入名字: ') # 把别人输入的东西存入name里面 再用print把name里的内容印出来
print(name)
print('嗨', name)