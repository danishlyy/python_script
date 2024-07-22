# 向文件中写入内容
file1 = open('name.txt', 'w')
file1.write('张飞')
file1.close()

file2 = open('name.txt', 'r')
print(file2.read())  # 张飞
file2.close()

file3 = open('name.txt', 'a')
file3.write('关羽')
file3.close()

file4 = open('multi_line_name.txt', 'r')
print(file4.readline())  # 1.张飞
file4.close()

file5 = open('multi_line_name.txt', 'r')
for line in file5.readlines():
    # 1.张飞
    #
    # 2.关羽
    #
    # 3.刘备
    print(line)

file6 = open('multi_line_name.txt')
print('当前文件指针的位置 %s' % file6.tell())  # 当前文件指针的位置 0
print('当前读取到一恶搞字符，字符的内容是 %s' % file6.read(1))  # 当前读取到一恶搞字符，字符的内容是 1
print('当前文件指针的位置 %s' % file6.tell())  # 当前文件指针的位置 1
file6.seek(0)
print('我们进行了seek操作')  # 我们进行了seek操作
print('当前文件指针的位置 %s' % file6.tell())  # 当前文件指针的位置 0
print('当前读取到一个字符，字符内容是 %s' % file6.read(1))  # 当前读取到一个字符，字符内容是 1
print('当前文件指针的位置 %s' % file6.tell())  # 当前文件指针的位置 1
file6.close()
