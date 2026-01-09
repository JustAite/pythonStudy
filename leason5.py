name = 'Runoob'
print('Hello %s' % name)

print('Hello {}'.format(name))

print(f'Hello {name}')


str = "this is string Example From Runoob....wow!!!"

print ("str.capitalize() : ", str.capitalize())

str = "[runoob]"

print ("str.center(40, '*') : ", str.center(40, '*'))


str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
 
print(str)
 
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
 
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))


Str='Runoob example....wow!!!'
suffix='!!'
print (len(Str))
print (Str.endswith(suffix))
print (Str.endswith(suffix,24))
suffix='run'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))


str = "runoob\t12345\tabc"  
print('原始字符串:', str)
 
# 默认 8 个空格
# runnob 有 6 个字符，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，后面的 \t 填充 3 个空格
print('替换 \\t 符号:', str.expandtabs())
 
# 2 个空格
# runnob 有 6 个字符，刚好是 2 的 3 倍，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，不是 2 的倍数，后面的 \t 填充 1 个空格
print('使用 2 个空格替换 \\t 符号:', str.expandtabs(2))
 
# 3 个空格
print('使用 3 个空格:', str.expandtabs(3))
 
# 4 个空格
print('使用 4 个空格:', str.expandtabs(4))
 
# 5 个空格
print('使用 5 个空格:', str.expandtabs(5))
 
# 6 个空格
print('使用 6 个空格:', str.expandtabs(6))

tru = (1,2,3,4,5)
print(id(tru))
del tru
# print(tru)

dict = {}
print(dict)
print(type(dict))
print(isinstance(dict, int))
print(id(dict))

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del tinydict['Name'] # 删除键 'Name'
print(tinydict)
tinydict.clear()     # 清空字典
print(tinydict)
