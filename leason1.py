
#单行注释用井号（#）开头

'''
多行注释用三个单引号（单引号或双引号均可）
也可以用来作为函数、类、模块的说明文档
'''

"""
多行注释用三个双引号（单引号或双引号均可）
也可以用来作为函数、类、模块的说明文档
需要注意的是，
1、字符串也可以用三个单引号或三个双引号括起来，所以在给函数、类、模块编写说明文档时，要注意不要和字符串混淆。
2、多行注释不能嵌套使用。
"""


# 输出语句
print("Hello, World!")

# 变量赋值
counter = 100;          # 整型变量
miles   = 1000.0;       # 浮点型变量
name    = "runoob";     # 字符串

print (counter)
print (miles)
print (name)
 
#使用三引号可以指定一个多行字符串，输出多行内容
str='''1234567890
qwertyuiop
asdfghjkl
zxcvbnm''';
# input("\n\n按下 enter 键后退出。")

print("=====str=======")
print(str)                 # 输出字符串
print("=====str[0:-1]=======")
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print("=====str[0]=======")
print(str[0])              # 输出字符串第一个字符
print("=====str[2:5]=======")
print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print("=====str[2:]=======")
print(str[2:])             # 输出从第三个开始后的所有字符
print("=====str[1:5:2]=======")
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print("=====str*2=======")
print(str * 2)             # 输出字符串两次
print("=====str + '你好'=======")
print(str + '你好')         # 连接字符串
 
print('------------------------------')

#print()，默认换行
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# sys.stdout.write() 是一个底层的输出函数，与 print() 不同，它不会自动添加换行符（\n）。
# 是否换行完全取决于你是否显式写入换行字符。
import sys; x = 'runBoob'; sys.stdout.write(x + '\n')

sys.stdout.write(" hiiiii ")    # hi 前后各有 1 个空格，


x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 如果需要print不换行输出,可以在print语句中指定end参数
print( x, end=" " )
print( y, end=" " )
print()


print('================Python import mode==========================')
""" 
sys.argv 是 Python 标准库 sys 模块中的一个非常重要的属性，用于获取命令行传递给脚本的参数列表。
sys.path 是 Python 解释器用来搜索模块的路径列表。

当你在命令行中运行一个 Python 脚本时，可以向脚本传递参数，这些参数会被存储在 sys.argv 列表中。
sys.argv 列表的第一个元素（索引为 0）是脚本的名称，后续的元素则是传递给脚本的参数。

sys.argv 是一个列表（list）
它包含了启动 Python 脚本时在终端中输入的所有命令行参数
列表中的每个元素都是字符串（str 类型）,即使你输入 123，它也是 '123'，需手动转 int()


"""
print ('命令行参数为:')
for i in sys.argv:
    print (i)

"""
sys.path 是一个包含字符串的列表，这些字符串表示 Python 解释器在导入模块时会搜索的目录路径。
当你使用 import 语句导入一个模块时，Python 解释器会按照 sys.path 列表中的路径顺序查找该模块。
如果模块在这些路径中的某个位置被找到，解释器就会加载它；如果找不到，则会引发 ImportError 异常。
sys.path 列表包含了 Python 解释器在导入模块时会搜索的目录路径。 这个列表通常包括以下几类路径：
1. 当前脚本所在的目录。
2. 标准库的安装目录。
3. 第三方库的安装目录（例如通过 pip 安装的库）。
4. 用户自定义的路径（如果有的话）。
了解 sys.argv 和 sys.path 对于编写需要处理命令行参数的脚本以及调试模块导入问题非常有帮助。
"""
print ('\n python 路径为',sys.path)


from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('\n argv:',argv) # 因为已经导入path成员，所以此处引用时不需要加sys.path
print('\n path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path