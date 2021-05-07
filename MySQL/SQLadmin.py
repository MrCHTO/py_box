from tkinter import *
from tkinter import font
from pymysql import *
from tkinter.font import BOLD, Font

db = NULL
cursor = NULL


def Loginu():
    username = entry0.get()
    userpasswd = entry1.get()
    global db
    db = connect(host='rm-2ze2pr85o2ozj8479po.mysql.rds.aliyuncs.com', port=3306,
                 user=username, passwd=userpasswd, charset='utf8')
    entry2.delete(0, END)
    if db == NULL:
        entry2.insert(0, '登陆失败，请检查用户名密码！')
    elif db != NULL:
        entry2.insert(0, '登陆成功！')


def Exitu():
    global db
    db.close()
    db = NULL
    entry2.delete(0, END)
    if db == NULL:
        entry2.insert(0, '已退出登录！')
    elif db != NULL:
        entry2.insert(0, '退出失败，请重试！')


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
    entry2.delete(0, END)
    if results != NULL:
        entry2.insert(0, '查询成功！')
    elif results == NULL:
        entry2.insert(0, '记录为空！')


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
    if results != NULL:
        entry2.insert(0, '查询成功！')
    elif results == NULL:
        entry2.insert(0, '记录为空！')


top = Tk()  # 创建顶层容器
top.title('MySQL')  # 设置容器名称
top.geometry('733x643')  # 设置容器大小
top.resizable(False, False)  # 防止用户调整大小

font0 = Font(family='Courier', size=14, weight=BOLD)  # 标签和按钮的字体设置
font1 = Font(family='Courier', size=12)  # 列表的字体设置

label0 = Label(top, font=font0, text='用户:', width=5)
label0.grid(row=0, column=0)
label1 = Label(top, font=font0, text='密码:', width=5)
label1.grid(row=0, column=2)
label2 = Label(top, font=font0, text='状态:', width=5)
label2.grid(row=20, column=0)

button0 = Button(top, font=font0, text='登录', width=5,
                 relief=GROOVE, command=Loginu)
button0.grid(row=0, column=4)
button1 = Button(top, font=font0, text='退出', width=5,
                 relief=GROOVE, command=Exitu)
button1.grid(row=0, column=5)
button2 = Button(top, font=font0, text='查库', width=5,
                 relief=GROOVE, command=Sedb)
button2.grid(row=0, column=6)
button3 = Button(top, font=font0, text='查表', width=5,
                 relief=GROOVE, command=Setb)
button3.grid(row=0, column=7)

entry0 = Entry(top, font=font0, width=10,)
entry0.grid(row=0, column=1)
entry0.insert(0, 'rds_user')
entry1 = Entry(top, font=font0, width=10, show="*")
entry1.insert(0, 'CTuser1928')
entry1.grid(row=0, column=3)
entry2 = Entry(top, font=font0, width=60)
entry2.grid(row=20, column=1, columnspan=7)


list0 = Listbox(top, font=font1, width=35, height=30)
list0.grid(row=2, column=0, rowspan=18, columnspan=4)
list1 = Listbox(top, font=font1, width=35, height=30)
list1.grid(row=2, column=4, rowspan=18, columnspan=4)

top.mainloop()  # 进入循环
