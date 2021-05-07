from tkinter import *
from tkinter import font
from pymysql import *
from tkinter.font import BOLD, Font

db = NULL
cursor = NULL


def Loginu():
    username = entry0.get()
    userpasswd = entry1.get()
    userpost = entry2.get()
    useradd = entry3.get()
    global db
    db = connect(host=useradd, port=int(userpost),
                 user=username, passwd=userpasswd, charset='utf8')
    entry5.delete(0, END)
    if db == NULL:
        entry5.insert(0, '登陆失败，请检查用户名密码！')
    elif db != NULL:
        Sedb()


def Exitu():
    global db
    db.close()
    db = NULL
    entry5.delete(0, END)
    if db == NULL:
        entry5.insert(0, '已退出登录！')
    elif db != NULL:
        entry5.insert(0, '退出失败，请重试！')


def Sedb():
    global db, cursor
    cursor = db.cursor()
    sql = 'show databases'
    cursor.execute(sql)
    results = cursor.fetchall()
    length = len(results)
    list0.delete(0, END)
    for item in results:
        list0.insert(0, item)
    entry5.delete(0, END)
    if results != NULL:
        entry5.insert(0, '查询成功！')
    elif results == NULL:
        entry5.insert(0, '记录为空！')


def Setb():
    global cursor
    listin = list0.selection_get()
    sql0 = 'use ' + listin
    sql1 = 'show tables'
    cursor.execute(sql0)
    cursor.execute(sql1)
    results = cursor.fetchall()
    length = len(results)
    list1.delete(0, END)
    for item in results:
        list1.insert(0, item)
    entry5.delete(0, END)
    if results != NULL:
        entry5.insert(0, '查询成功！')
    elif results == NULL:
        entry5.insert(0, '记录为空！')


top = Tk()  # 创建顶层容器
top.title('MySQL')  # 设置容器名称
top.geometry('670x675')  # 设置容器大小
top.resizable(False, False)  # 防止用户调整大小

font0 = Font(family='Courier', size=14, weight=BOLD)  # 标签和按钮的字体设置
font1 = Font(family='Courier', size=12)  # 列表的字体设置

label0 = Label(top, font=font0, text='用户', width=5)
label0.grid(row=0, column=0)
label1 = Label(top, font=font0, text='密码', width=5)
label1.grid(row=0, column=2)
label2 = Label(top, font=font0, text='端口', width=5)
label2.grid(row=0, column=4)
label3 = Label(top, font=font0, text='地址', width=5)
label3.grid(row=1, column=0)
label4 = Label(top, font=font0, text='内容', width=5)
label4.grid(row=14, column=0)
label5 = Label(top, font=font0, text='操作', width=5)
label5.grid(row=15, column=0)
label6 = Label(top, font=font0, text='状态', width=5)
label6.grid(row=16, column=0)

button0 = Button(top, font=font0, text='登录', width=10,
                 relief=GROOVE, command=Loginu)
button0.grid(row=1, column=4)
button1 = Button(top, font=font0, text='退出', width=10,
                 relief=GROOVE, command=Exitu)
button1.grid(row=1, column=5)
button2 = Button(top, font=font0, text='添加', width=10, relief=GROOVE)
button2.grid(row=15, column=1)
button3 = Button(top, font=font0, text='删除', width=10, relief=GROOVE)
button3.grid(row=15, column=2)
button4 = Button(top, font=font0, text='修改', width=10, relief=GROOVE)
button4.grid(row=15, column=3)
button5 = Button(top, font=font0, text='查询', width=10,
                 relief=GROOVE, command=Setb)
button5.grid(row=15, column=4)
button6 = Button(top, font=font0, text='撤销', width=10, relief=GROOVE)
button6.grid(row=15, column=5)

entry0 = Entry(top, font=font0, width=10)
entry0.grid(row=0, column=1)
entry0.insert(0, 'rds_user')
entry1 = Entry(top, font=font0, width=10, show="*")
entry1.grid(row=0, column=3)
entry1.insert(0, 'CTuser1928')
entry2 = Entry(top, font=font0, width=10)
entry2.grid(row=0, column=5)
entry2.insert(0, '3306')
entry3 = Entry(top, font=font0, width=32, show="*")
entry3.grid(row=1, column=1, columnspan=3)
entry3.insert(0, 'rm-2ze2pr85o2ozj8479po.mysql.rds.aliyuncs.com')
entry4 = Entry(top, font=font0, width=54)
entry4.grid(row=14, column=1, columnspan=5)
entry5 = Entry(top, font=font0, width=54)
entry5.grid(row=16, column=1, columnspan=5)

Text0 = Text(top, font=font1, width=36, height=28)
Text0.grid(row=2, column=3, rowspan=12, columnspan=3)

list0 = Listbox(top, font=font1, width=29, height=13)
list0.grid(row=2, column=0, rowspan=6, columnspan=3)
list1 = Listbox(top, font=font1, width=29, height=13)
list1.grid(row=8, column=0, rowspan=6, columnspan=3)


top.mainloop()  # 进入循环
