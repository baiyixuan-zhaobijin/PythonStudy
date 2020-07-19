# 除法
print(10/3)     #3.33
print(10//3)    #3
#编码
print(len('中文'))                  #2
print(len('中文'.encode('utf-8')))  #6
#格式化
for i in range(1,6):
    #url =  'https://www.zbytb.com/zb-{0}.html'.format(str(i))
    url = 'https://www.zbytb.com/zb-%s.html' % (str(i))
    print(url)
#基本数据结构
# list 有序的数据集合
list1 = ['张三','李四','王五']
print(list1[-1])
# tuple 只读的数据集合
tuple1 = (1,3,4,'李四')
print(tuple1[-3])
# dict 字段
dict = {'name':'张三','age':18,'score':99}
print(dict['name'])
# 字典迭代
for key,value in dict.items():
    print(key+':'+str(value))
# set 不能重复度的序列
set1 = set(['A','C', 'B', 'D'])
print(set1)
# 检查数据类型
x = 33
if not isinstance(x,(int,float)):
    print('x不是数')
else:
    print('x is number')
# 列表生成器
L = [x*x for x in range(3,9) if x%2==0]
print(L)
# 高阶函数
f = abs
def test(a,b,f):
    print(f(a)+f(b))
test(3,-4,f)




















