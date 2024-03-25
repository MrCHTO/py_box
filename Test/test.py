print("hhhhh")
name = 999  # 标签变量名，可为任何类型
print(str(name)+"AAAA")
name = "ABC"  # '以及" 只能一行打印 ''' 可以多行打印
print(name+"AAAA")
print(type(name))  # 返回变量类型
print(id(name))  # 返回变量地址
print(float(1.0))  # 浮点数类型
print(repr('aaaaa'))  # 表达式字符串
print(chr(100))  # 数字转字符

name1 = int(input('提示文字 数字'))

print(name1)
print(name, name1)
print(name, name1, '文字')

if name1 > 100:  # and or not (&& || ! )
    print('>100')
elif name1 < 100:
    print('<100')
else:
    print('100\n')

i = 1
while i <= 10:
    print(i, end=' ')  # ,end='中间的分隔符' 在一行输出
    i += 1
print()  # 换行使用

for i in range(0, 10, 1):
    print(i, 'AAA', end=' ')
print()

for i in name:
    print(i+'A', 'B', end='+')
print()

# break 终止 continue 跳过 pass 占位符

a = [1, 2, 3]  # ->列表
b = (1, 2, 3,)  # ->元组
c = {'1': 'A', '2': 'B', '3': 'C'}  # ->字典

if __name__ == '__main__':
    print("__name__ == '__main__")
