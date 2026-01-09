num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("num_str 数据类型为:",type(num_str))

print(num_int+int(num_str))

print(complex(1))

# print("\a")


import time

for i in range(101):
    print("\r{:3}%".format(i),end=' ')
    time.sleep(0.05)


    