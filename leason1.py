
"""
This script prints "Hello, World!" to the console.

"""
print("Hello, World!")

# 变量赋值
counter = 100;          # 整型变量
miles   = 1000.0;       # 浮点型变量
name    = "runoob";     # 字符串

print (counter)
print (miles)
print (name)
 
str='''123456789
1233
frrrtt
rrrrr''';
# input("\n\n按下 enter 键后退出。")
print(str)                 # 输出字符串
# print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
# print(str[0])              # 输出字符串第一个字符
# print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
# print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
# print(str * 2)             # 输出字符串两次
# print(str + '你好')         # 连接字符串
 
# print('------------------------------')
 
# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

sys.stdout.write(" hi ")    # hi 前后各有 1 个空格


x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()


print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)


from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('\n argv:',argv) # 因为已经导入path成员，所以此处引用时不需要加sys.path
print('\n path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path