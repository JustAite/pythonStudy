# 打开文件
fo = open("runoob.txt", "wb")
print ("文件名为: ", fo.name)

# 刷新缓冲区
fid = fo.fileno()

print ("文件描述符为: ", fid)

# 关闭文件
fo.close()