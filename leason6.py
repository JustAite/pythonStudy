# var1 = 100
# if var1:
#     print ("1 - if 表达式条件为 true")
#     print (var1)
 
# var2 = 0
# if var2:
#     print ("2 - if 表达式条件为 true")
#     print (var2)
# print ("Good bye!")

# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age -2)*5
#     print("对应人类年龄: ", human)
 
# ### 退出提示
# input("点击 enter 键退出")

# num = 10
# key = -1
# while num != key:
#     key = int(input("请输入一个数字："))
#     if key == num:
#         print("猜对了")
#         break
#     elif key > num:
#         print("大了")
#     else:
#         print("小了")

# def updateValue(num):
#     match num:
#         case 1|2|3:
#             print(num)
#         case _:
#             print("default")

# num = input("请输入一个数字：")
# print(num)
# updateValue(num)


# n = 100
 
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
 
# print("1 到 %d 之和为: %d" % (n,sum))


# n = 10
# a, b = 0, 1
# for i in range(n):
#     print(b)
#     a, b = b, a + b


# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# new_dict = {k:v for k,v in dict.items() if k != 'Age'}
# print(new_dict)

# numlist = [1, 2, 3, 4, 5]

# it = iter(numlist)
# print(next(it))
# print(next(it))

# for x in it:
#     print(x, end=' ')



print("\a")
import leason4