from time import *
from tkinter import *
from tkinter.font import BOLD, Font

t = 0
sum = 0


def Createtxt():
    fn = entry0.get()
    inf = open(fn+"_input.txt", 'w', encoding='UTF-8')
    inf.close
    entry1.delete(0, END)
    entry1.insert(0, '创建成功,请添加内容')


def Btxt():
    sum = 0
    T1 = time_ns()
    fn = entry0.get()
    inf = open(fn+".md", 'r', encoding='UTF-8')
    outf = open(fn+"_output.txt", 'w', encoding='UTF-8')
    s = inf.readline()
    while s:
        length = len(s)
        a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
        for i in range(length):

            if s[i:i+1] == '#':
                a += 1
                if s[i+1:i+2] == ' ':
                    break

            elif s[i:i+1] == '-' and s[i+1:i+2] == ' ':
                b = 1
                break

            elif s[i:i+1] == "\t" and s[i+1:i+2] == '-':
                c = 1
                break

            elif s[i:i+1] == "\t" and s[i+1:i+2] == "\t":
                d = 1
                break

            elif s[i:i+1] == " " and s[i+1:i+2] == " " and s[i+2:i+3] != "\n":
                e = 1
                break

            elif s[i:i+1] == "\t" and s[i+1:i+2] == " " and s[i+3:i+4] != "\n":
                f = 1
                break

            elif s[i:i+1] != "\n" and s[i:i+1] != " " and s[i:i+1] != "\t":
                g = 1
                break

        if a != 0:
            if a == 1:
                s = inf.readline()
                sum += 1
                continue
            if a == 2:
                outf.write('\n***\n')
                sum += 1
            outf.write('\n')
            outf.write(s[1:length])
            s = inf.readline()
            sum += 1
            continue

        if b == 1:
            outf.write('\n###')
            outf.write(s[1:length])
            s = inf.readline()
            sum += 1
            continue

        if c == 1 or d == 1:
            if c == 1:
                outf.write('\n')
            outf.write(s[1:length])
            s = inf.readline()
            sum += 1
            continue

        if e == 1:
            outf.write('>')
            outf.write(s[2:length])
            outf.write('\n')
            s = inf.readline()
            sum += 1
            continue

        if f == 1:
            outf.write('>')
            outf.write(s[3:length])
            outf.write('\n')
            s = inf.readline()
            sum += 1
            continue

        if g == 1:
            outf.write('>')
            outf.write(s[0:length])
            outf.write('\n')
            s = inf.readline()
            sum += 1
            continue

        s = inf.readline()
    inf.close
    outf.close
    T2 = time_ns()
    t = T2-T1
    t = t/100000
    entry2.delete(0, END)
    entry2.insert(0, t)
    entry1.delete(0, END)
    entry1.insert(0, sum)


def Bmd():
    sum = 0
    T1 = time_ns()
    fn = entry0.get()
    inf = open(fn+".md", 'r', encoding='UTF-8')
    outf = open(fn+"_output.md", 'w', encoding='UTF-8')
    s = inf.readline()
    while s:
        length = len(s)
        a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
        for i in range(length):

            if s[i:i+1] == '#':
                a += 1
                if s[i+1:i+2] == ' ':
                    break

            elif s[i:i+1] == '-' and s[i+1:i+2] == ' ':
                b = 1
                break

            elif s[i:i+1] == "\t" and s[i+1:i+2] == '-':
                c = 1
                break

            elif s[i:i+1] == "\t" and s[i+1:i+2] == "\t":
                d = 1
                break

            elif s[i:i+1] == " " and s[i+1:i+2] == " " and s[i+2:i+3] != "\n":
                e = 1
                break

            elif s[i:i+1] == "\t" and s[i+1:i+2] == " " and s[i+3:i+4] != "\n":
                f = 1
                break

            elif s[i:i+1] != "\n" and s[i:i+1] != " " and s[i:i+1] != "\t":
                g = 1
                break

        if a != 0:
            if a == 1:
                s = inf.readline()
                sum += 1
                continue
            if a == 2:
                outf.write('\n***\n')
                sum += 1
            outf.write('\n')
            outf.write(s[1:length])
            s = inf.readline()
            sum += 1
            continue

        if b == 1:
            outf.write('\n###')
            outf.write(s[1:length])
            s = inf.readline()
            sum += 1
            continue

        if c == 1 or d == 1:
            if c == 1:
                outf.write('\n')
            outf.write(s[1:length])
            s = inf.readline()
            sum += 1
            continue

        if e == 1:
            outf.write('>')
            outf.write(s[2:length])
            outf.write('\n')
            s = inf.readline()
            sum += 1
            continue

        if f == 1:
            outf.write('>')
            outf.write(s[3:length])
            outf.write('\n')
            s = inf.readline()
            sum += 1
            continue

        if g == 1:
            outf.write('>')
            outf.write(s[0:length])
            outf.write('\n')
            s = inf.readline()
            sum += 1
            continue

        s = inf.readline()
    inf.close
    outf.close
    T2 = time_ns()
    t = T2-T1
    t = t/100000
    entry2.delete(0, END)
    entry2.insert(0, t)
    entry1.delete(0, END)
    entry1.insert(0, sum)


top = Tk()  # 创建顶层容器
top.title('转化')  # 设置容器名称
top.geometry('217x179')  # 设置容器大小
top.resizable(False, False)  # 防止用户调整大小
font1 = Font(family='Courier', size=14, weight=BOLD)
font2 = Font(family='Courier', size=14)

label0 = Label(top, font=font1, text='-----操作文件名-----', width=19)
label1 = Label(top, font=font1, text='------当前状态------', width=19)
label2 = Label(top, font=font1, text='修改', width=3)
label3 = Label(top, font=font1, text='项', width=2)
label4 = Label(top, font=font1, text='耗时', width=3)
label5 = Label(top, font=font1, text='MS', width=2)
label6 = Label(top, font=font1, text='.MD', width=3)

button0 = Button(top, font=font2, text='导出TXT', width=9,
                 relief=GROOVE, command=Btxt)
button1 = Button(top, font=font2, text='导出MD', width=9,
                 relief=GROOVE, command=Bmd)

entry0 = Entry(top, font=font2, width=15)
entry1 = Entry(top, font=font2, width=8)
entry2 = Entry(top, font=font2, width=8)

entry1.insert(0, '0')
entry2.insert(0, '0')


label0.grid(row=0, columnspan=6)
entry0.grid(row=1, column=0, columnspan=5)
label6.grid(row=1, column=5)
button0.grid(row=3, column=0, columnspan=3)
button1.grid(row=3, column=3, columnspan=3)
label1.grid(row=4, columnspan=6)
label2.grid(row=5, column=0, columnspan=1)
entry1.grid(row=5, column=1, columnspan=4)
label3.grid(row=5, column=5)
label4.grid(row=6, column=0, columnspan=1)
entry2.grid(row=6, column=1, columnspan=4)
label5.grid(row=6, column=5)

top.mainloop()  # 进入循环
