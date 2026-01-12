"""
# 不同数据类型
type()获取数据类型，返回对象 精确的类型（class），即只认“亲爹”（精确类型）
isinstance()判断数据类型，判断对象是否是 指定类型或其子类的实例，即认“祖宗”（支持继承链）
| 特性 | `type(obj) == T` | `isinstance(obj, T)` |
|------|------------------|------------------------|
| 是否支持继承 | ❌ 否 | ✅ 是 |
| 能否检查多个类型 | ❌（需多次写） | ✅ 支持元组：`isinstance(x, (int, float))` |
| 性能 | 略快（简单比较） | 略慢（需遍历 MRO） |
| Pythonic 推荐度 | ⚠️ 少用 | ✅ 强烈推荐 |
| 适用场景 | 需要严格类型匹配（极少见） | 绝大多数类型检查场景，99% 情况下推荐使用 isinstance() |
"""
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))

print("-----------------复数类型-----------------")
"""
complex（复数）类型在日常编程中不如 int 或 float 常见，但在科学计算、信号处理、电气工程、量子力学、控制系统等领域有重要应用
complex（复数）类型是 Python 内置的数值类型之一，用于表示复数（Complex Numbers），形式为 a + bj，其中：
a 是实部（real part）
b 是虚部（imaginary part）
j 是虚数单位（满足 $ j^2 = -1 $）

创建复数的方法有两种：
# 方法1：直接字面量（推荐）
z1 = 3 + 4j

# 方法2：使用 complex() 构造函数
z2 = complex(3, 4)      # 等价于 3 + 4j
z3 = complex("3+4j")    # 从字符串解析

# 虚部可为负
z4 = 2 - 5j
共轭复数：实部不变，虚部取反
z = 3 + 4j
z_conj = z.conjugate()  # 3 - 4j

访问实部和虚部：
z = 3 + 4j
real_part = z.real    # 3.0
imag_part = z.imag    # 4.0

复数支持常见的算术运算：
z1 = 1 +2j              # a + bj
z2 = 3 + 4j              # c + dj
z_sum = z1 + z2          # (4+6j)=====> (a+c) + (b+d)j
z_diff = z1 - z2         # (-2-2j)====> (a-c) + (b-d)j
z_prod = z1 * z2         # (-5+10j). ====> (ac - bd) + (ad + bc)j
z_quot = z1 / z2         # (0.44+0.08j). ===> ((ac + bd)/(c^2 + d^2)) + ((bc - ad)/(c^2 + d^2))j
复数不支持比较运算（如 z1 < z2），因为复数在数学上没有自然序关系。

复数还支持一些内置函数和模块操作：
abs(z)          # 计算复数的模（magnitude）
pow(z, n)       # 计算复数的幂
import cmath    # 复数数学函数模块
cmath.sqrt(z)   # 计算复数的平方根
cmath.exp(z)    # 计算复数的指数函数  

注意事项：
不能与非数值类型混合运算，如字符串或列表
复数的实部和虚部均为浮点数，即使输入为整数
不支持复数类型的序列化，即不能直接存储为 JSON 等格式
复数是可哈希的，可用作 dict 键或 set 元素
"""
z1 = 1 +2j              # a + bj
z2 = 3 + 4j              # c + dj
z_sum = z1 + z2          # (4+6j)=====> (a+c) + (b+d)j
z_diff = z1 - z2         # (-2-2j)====> (a-c) + (b-d)j
z_prod = z1 * z2         # (-5+10j). ====> (ac - bd) + (ad + bc)j
z_quot = z1 / z2         # (0.44+0.08j). ===> ((ac + bd)/(c^2 + d^2)) + ((bc - ad)/(c^2 + d^2))j

print("z1 + z2 =", z_sum)
print("z1 - z2 =", z_diff)
print("z1 * z2 =", z_prod)
print("z1 / z2 =", z_quot)
print("abs(z1) =", abs(z1))
print("z1 conjugate =", z1.conjugate())


print("-----------------布尔类型-----------------")
# 布尔值在控制流中的应用
if True:
    print("This will always print")
  
if not False:
    print("This will also always print")
   
x = 10
if x:
    print("x is non-zero and thus True in a boolean context")


print("-----------------列表类型-----------------")
list = [ '1', 2 , 3.0, '4', 5.5, 6, "7", '8' ]  # 定义一个列表
tinylist = [123, 'runoob']

print("-----------------列表切片-----------------")
print(list)            # 打印整个列表
print(len(list))         # 打印列表长度
print(list[0:3])       # 打印列表的第一个到第三个元素（不包含第三个元素）
print(list[0])         # 打印列表的第一个元素
print("===印列表第二到第四个元素（不包含第四个元素）====")
print(list[1:5:2])       # 打印列表第二到第四个元素（不包含第四个元素）
print(list[2:])        # 打印列表从第三个元素开始到末尾
print(tinylist * 2)    # 打印tinylist列表两次
print(list + tinylist)  # 打印两个列表拼接在一起的结果

print("-----------------列表方法-----------------")
def reverseWords(input):
     
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
 
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    #inputWords[::-1]      # ✅ 最常见、最简洁的反转写法
    #inputWords[-1::-1]    # 功能相同，但显式指定了起点
    #reversed(inputWords)  # 返回迭代器，需 list() 包裹才能得到列表
    #inputWords=inputWords[-1::-1] #效果和inputWords[::-1]相同
    #inputWords.reverse()   # 原地反转列表，效率最高，但不返回新列表
    inputWords = inputWords[::-1]
    
 
    # 重新组合字符串
    output = ' '.join(inputWords)
     
    return output
 
if __name__ == "__main__":
    input = 'I very like runoob'
    rw = reverseWords(input)
    print(rw)

print("-----------------特殊的内置变量型-----------------")

print("-----------------__name__-----------------")

"""
__name__: 模块的名称。如果模块被直接运行，__name__ 的值为 "__main__"；如果模块被导入，__name__ 的值为模块的实际名称。
它在控制代码执行逻辑（尤其是区分“直接运行”和“被导入”）时起着关键作用
每个 Python 模块（.py 文件）都有一个 __name__ 属性。
根据模块的运行方式，`__name__` 的值会有所不同：
| 场景 | `__name__` 的值 |
|------|----------------|
| 直接运行脚本 `python foo.py` | `"__main__"` |
| 导入模块 `import foo` | `"foo"` |
| 从包中导入 `from pkg import mod` | `"pkg.mod"` |
| 在交互式解释器（如 IPython）中 | `"__main__"` |
"""
print("模块名称：", __name__)

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # 仅在直接运行脚本时执行
    print(greet("World"))
else:
    # 在被导入时执行
    print("模块被导入，模块名称为：", __name__)
    pass

print("-----------------__file__-----------------")
"""
__file__: 模块的文件路径，表示模块所在的文件系统路径；
返回当前模块的绝对或相对文件路径（字符串）；
它对于定位模块文件、加载资源文件以及调试非常有用。
"""
from operator import __call__
import os
print("__file__:", __file__) 
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
config_path =os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
print(config_path)

print("-----------------__doc__-----------------")
""" 
__doc__: 访问对象的文档字符串，包含模块的简要说明；
用于存储模块、类或函数的文档字符串（docstring）；
它有助于提供代码的说明和使用指南，便于开发者理解和维护代码。

"""
def example_function():
    """这是一个示例函数的文档字符串。"""
    pass
print("模块文档字符串：", __doc__)
print("函数文档字符串：", example_function.__doc__)

print("-----------------其他特殊内置变量-----------------")
print("模块所属包名称：", __package__)
print("模块加载器对象：", __loader__)
print("模块规格说明对象：", __spec__)
print("模块字节码缓存文件路径：", __cached__)
# print(__import__("os"))
print("模块导入的其他模块列表：", __import__ if '__imports__' in globals() else "Not Available")
# print("Python 解释器版本信息：", __version__ if '__version__' in globals() else "Not Available")
# print("模块全局命名空间字典：", __globals__ if '__globals__' in globals() else "Not Available")
print("模块局部命名空间字典：", __call__ if '__locals__' in globals() else "Not Available")   
"""
__package__: 模块所属的包的名称。如果模块不属于任何包，则该值为 None。
__loader__: 模块的加载器对象，负责加载模块的具体实现。
__spec__: 模块的规格说明对象，包含模块的导入和加载信息。
__cached__: 模块的字节码缓存文件路径，如果存在的话。
__imports__: 模块导入的其他模块列表。
__version__: Python 解释器的版本信息。
__globals__: 模块的全局命名空间字典。
__locals__: 模块的局部命名空间字典。

"""
