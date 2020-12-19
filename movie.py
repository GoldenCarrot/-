import numpy as np
import pandas as pd
import math
#读取csv文件，并以utf-8编码解码
csv=pd.read_csv("电影记录.csv",encoding='utf-8')
#定义一个全局变量username
username=""
#定义函数moviename，此函数用于显示当前已储存的影片
def moviename():
    #得到已储存的影片数量
    g = len(csv.index)
    #遍历影片数量
    for i in range(1,g+1):
        #每5部影片换一行
        if i%5==0:
            print('({})'.format(i) + '--' + csv['电影名'][i-1]+"   ")
        else:
            print('({})'.format(i) + '--' + csv['电影名'][i-1]+"   ",end="")

#定义information函数，此函数用于显示影片的具体信息
def information(A):
    #得到csv文件中的每一行的数据，并以列表格式输出
    a=csv.values.tolist()
    #切片其中需要的部分，并分类输出
    b=a[A]
    print("电影名："+str(b[0]))
    print("类型："+str(b[1]))
    print("产地："+str(b[2]))
    print("主演："+str(b[3]))
    print("上映日期："+str(b[4]))
    print("时长："+str(b[5]))

#定义一个alltype函数，用于统计当前收录影片中有多少种不同的类型
def alltype():
    #将csv文件中‘类型’一列以列表形式输出
    a = list(csv['类型'])
    # 得到已储存的影片数量
    g = len(csv.index)
    #建立一个空集合，用于去除相同的数据
    e=set()
    #向集合中添加元素
    for i in range(g):
        b=str(a[i])
        c=b.split('/')
        for i in c:
            e.add(i)
    #返回集合
    return(e)
    print(e)

#定义一个type函数，使用户通过影片类型可查询影片
def type():
    print("欢迎使用电影评分系统1.0")
    m=alltype()
    #列举出已有的电影类型
    print(m)
    #获得用户输入的数据
    choose=str(input("请选择类型："))
    #判定片库中是否已有此类型影片
    if choose in m:
        a=list(csv['类型'])
        g = len(csv.index)
        #将每一部影片的类型与用户需要的类型作比较，将符合类型的影片输出并显示其基本信息和得分
        for i in range(g):
            b=str(a[i])
            c=b.split('/')
            if choose in c:
                information(i)
                grades(i)
                print("")
            else:
                continue
    else:
        print("很抱歉，现有片库中无此类型影片")
        print("")
        x=int(input("输入1即可添加影片信息,其他任意数字返回查询界面："))
        if x==1:
            Add()
        else:
            menu2()
    back2()

#定义一个allbornland函数，用于统计片库中的影片有多少不同的产地
def allbornland():
    a = list(csv['产地'])
    g = len(csv.index)
    # 建立一个空集合，用于去除相同的数据
    e = set()
    # 向集合中添加元素
    for i in range(g):
        b = str(a[i])
        c = b.split('/')
        for i in c:
            e.add(i)
    #返回集合
    return (e)
    print(e)

#定义一个bornland函数，使用户可以通过影片产地查询影片
def bornland():
    print("欢迎使用电影评分系统1.0")
    m = allbornland()
    #列举出已有的电影产地
    print(m)
    # 获得用户输入的数据
    choose = str(input("请选择产地："))
    # 判定片库中是否已有来自此产地的影片
    if choose in m:
        a = list(csv['产地'])
        g = len(csv.index)
        # 将每一部影片的产地与用户需要的产地作比较，将符合类型的影片输出并显示其基本信息和得分
        for i in range(g):
            b = str(a[i])
            c = b.split('/')
            if choose in c:
                information(i)
                grades(i)
                print("")
            else:
                continue
    else:
        print("很抱歉，现有片库中无来自此地的影片")
        print("")
        x = int(input("输入1即可添加影片信息,其他任意数字返回查询界面："))
        if x == 1:
            Add()
        else:
            menu2()
    back2()

#定义一个allmainactor函数，用于统计片库中的影片有多少不同的主演
def allmainactor():
    a = list(csv['主演'])
    g = len(csv.index)
    # 建立一个空集合，用于去除相同的数据
    e = set()
    # 向集合中添加元素
    for i in range(g):
        b = str(a[i])
        c = b.split('/')
        for i in c:
            e.add(i)
    # 返回集合
    return (e)
    print(e)

#定义一个mainactor函数，使用户可以通过影片主演查询影片
def mainactor():
    print("欢迎使用电影评分系统1.0")
    m = allmainactor()
    # 列举出已有的电影主演
    print(m)
    # 获得用户输入的数据
    choose = str(input("请选择主演："))
    # 判定片库中是否已有来自此产地的影片
    if choose in m:
        a = list(csv['主演'])
        g = len(csv.index)
        # 将每一部影片的主演与用户需要的主演作比较，将符合类型的影片输出并显示其基本信息和得分
        for i in range(g):
            b = str(a[i])
            c = b.split('/')
            if choose in c:
                information(i)
                grades(i)
                print("")
            else:
                continue
    else:
        print("很抱歉，现有片库中无此主演饰演的影片")
        print("")
        x = int(input("输入1即可添加影片信息,其他任意数字返回查询界面："))
        if x == 1:
            Add()
        else:
            menu2()
    back2()

#定义一个allborntime函数，用于统计片库中的影片有多少不同的上映日期
def allborntime():
    a = list(csv['上映日期'])
    g = len(csv.index)
    # 建立一个空集合，用于去除相同的数据
    e = set()
    # 向集合中添加元素
    for i in range(g):
        b = str(a[i])
        c = b.split('月')
        d=c[0:1]
        for i in d:
            e.add(str(i)+'月')
    #返回集合
    return (e)

#定义一个borntime函数，使用户可以通过年月来查询影片
def borntime():
    print("欢迎使用电影评分系统1.0")
    print("上映日期索引")
    m=allborntime()
    #列举出已有的上映年月
    print(m)
    #获得用户输入的数据
    year=str(input("请输入年份(阿拉伯数字）:")+'年')
    month = str(input("请输入月份(阿拉伯数字）:")+'月')
    #将用户的数据进行处理并判定片库中是否有此年月上映的影片
    a=list(csv['上映日期'])
    g = len(csv.index)
    h=year+month
    j=h[0:-1]
    if h in m:
        a = list(csv['上映日期'])
        # 将每一部影片的上映年月与用户需要的上映年月作比较，将符合类型的影片输出并显示其基本信息和得分
        for i in range(g):
            b = str(a[i])
            c = b.split('月')
            d=str(c[0:1])
            if j in d:
                information(i)
                grades(i)
                print("")
            else:
                continue
    else:
        print('很抱歉，现有片库中无{}{}上映的影片'.format(year,month))
        print("")
        x = int(input("输入1即可添加影片信息,其他任意数字返回查询界面："))
        if x == 1:
            Add()
        else:
            menu2()
    back2()

#定义一个alltime函数，用于统计片库中的电影时长
def alltime():
    a = list(csv['时长'])
    g = len(csv.index)
    # 建立一个空集合，用于去除相同的数据
    e = set()
    c=[]
    # 向集合中添加元素
    for i in range(g):
        b = str(a[i])
        c.append(b)
        for i in c:
            e.add(i)
    # 返回集合
    return (e)
    print(e)

#定义一个time函数，使用户可以根据影片时长来查询影片
def time():
    print("欢迎使用电影评分系统1.0")
    m = alltime()
    #列举出已有的影片时长
    print(m)
    # 获得用户输入的数据
    choose = str(input("请选择时长：")+'min')
    c=[]
    if choose in m:
        a = list(csv['时长'])
        g = len(csv.index)
        # 将每一部影片的时长与用户需要的时长作比较，将符合类型的影片输出并显示其基本信息和得分
        for i in range(g):
            b = a[i]
            if choose in b:
                information(i)
                grades(i)
                print("")
            else:
                continue
    else:
        print("很抱歉，现有片库中无此时长的影片")
        print("")
        x = int(input("输入1即可添加影片信息,其他任意数字返回查询界面："))
        if x == 1:
            Add()
        else:
            menu2()
    back2()

#定义dic函数，用于得到‘电影名：index的字典类型
def dic():
    dict={}
    for ni in range(100):
        dict.setdefault(csv['电影名'][ni],ni)
    return(dict)

#定义searchname函数，使用户可以根据电影影片查询影片
def searchname():
    print("欢迎使用电影评分系统1.0")
    #创建一个空列表
    ALL=[]
    g = len(csv.index)
    #所有电影名填入列表中
    for i in range(g):
        a=csv["电影名"][i]
        ALL.append(a)
        Name=input("请输入需要查询的影片名称：")
        # 将每一部影片的名称与用户需要的名称作比较，将符合类型的影片输出并显示其基本信息和得分
        if Name in ALL:
            c=dic()
            b=c.get(Name)
            information(b)
            grades(b)
        else:
            print("您所查询的影片未收录到本系统中，请见谅。")
            print("")
            x = int(input("输入1即可添加影片信息,其他任意数字返回查询界面："))
            if x == 1:
                menu3()
            else:
                menu2()
        back2()

#定义register函数，用于用户注册
def register():
    print("欢迎使用电影评分系统1.0")
    global username
    #获得用户的数据
    username=str(input("请输入需要注册的用户名："))
    b=csv.columns
    #判定用户名是否已被占用
    if username in b:
        print("您的用户名已被注册，请更换您的用户名。")
        back3()
    #注册用户名并写入到csv文件中
    else:
        n=len(csv.columns)
        csv.insert(n,username,' ')
        csv.to_csv("电影记录.csv",index=False)
        print("注册成功,进入评分系统")
        menu5()

#定义一个score函数，用于用户评分
def score():
    print("欢迎使用电影评分系统1.0")
    print("从下列影片中选择影片进行评分（0-100）")
    #列举已有的影片
    moviename()
    ALL = []
    g = len(csv.index)
    for i in range(g):
        a = csv['电影名'][i]
        ALL.append(a)
    #获得用户输入的数据
    d=input("请输入需要评分的影片的名称(可以直接复制）：")
    #若影片在片库中，则进行评分
    if d in ALL:
        c = dic()
        b = c.get(d)
        information(b)
        grades(b)
        e=float(input("请评分："))
        csv.loc[b,str(username)]=e
        csv.to_csv("电影记录.csv",index=False)
        print("评分完成")
        back5()
    #若影片未在片库中，则可以选择添加影片
    else:
        print("您所查询的影片未收录到本系统中，请见谅。")
        x = int(input("输入1即可添加影片信息,其他任意数字返回评分界面："))
        if x == 1:
            Add()
        else:
            menu5()

#定义一个review函数，使用户可以查询自己的历史评分
def review():
    print("欢迎使用电影评分系统1.0")
    global username
    g=len(csv.index)
    for i in range(g):
        if csv[username][i]!=" ":
            h=csv['电影名'][i]
            j=csv[username][i]
            print(str(h)+'---'+str(j))
    back5()

#定义一个lookthrough函数，使用户可以查询他人的评分
def lookthrough():
    print("欢迎使用电影评分系统1.0")
    a=list(csv.columns)
    b=a[6:]
    print(b)
    g = len(csv.index)
    #获得用户的数据
    c=str(input("请选择需要查看的用户："))
    if c in csv.columns:
        for i in range(g):
            if csv[c][i]!=" ":
                h=csv['电影名'][i]
                j=csv[c][i]
                print(str(h)+'---'+str(j))
        back5()
    else:
        print("抱歉，系统中无此用户")
        lookthrough()

#定义一个grades函数，使用户可以看到影片得分
def grades(A):
    h=list(csv.columns)
    g=csv['电影名'][A]
    j=h[6:-1]
    l=0
    n=0
    for m in j:
        if csv[m][A] != " ":
            k=csv[m][A]
            l+=int(k)
            n+=1
        else:
            continue
    if n==0:
        print("未有用户对此部电影评分")
    else:
        o=l/n
        print("用户对《{}》的评分平均值为{:.2f}".format(g,o))

#定义一个Add函数，使用户可以添加影片进入片库
def Add():
    global csv
    print("欢迎使用电影评分系统1.0")
    print("如果不需要添加影片，请直接按回车键跳过（若偶然进入此界面）")
    a=str(input("请输入电影名称："))
    b=str(input("请输入影片类型（每种类型之间用/隔开）："))
    c=str(input("请输入影片产地（不同产地间用/隔开）："))
    d=str(input("请输入主演名单（不同人员之间用/隔开）："))
    e=str(input("请输入影片上映日期（格式为'x年x月x日'）："))
    f=str(input("请输入影片时长（格式为'xx'min）："))
    A=int(input("是否需要修改，需要修改请输入1，不需要修改请输入0："))
    if A==1:
        print("")
        Add()
    elif A==0:
        if list(a) in list(csv['电影名']):
            print("此影片已存在，请更换影片")
            print("")
            Add()
        if list(a) in []:
            print("")
            back4()
        else:
            g=[a,b,c,d,e,f]
            n=len(csv.index)
            names=list(csv.columns)
            for i in range(len(csv.columns)):
                if i<=5:
                    csv.loc[n+1,names[i]]=g[i]
                else:
                    csv.loc[n+1,names[i]]=" "
            csv.to_csv("电影记录.csv",index=False)
            csv = pd.read_csv("电影记录.csv", encoding='utf-8')
            print("影片添加成功")
            back4()
    else:
        print("请输入正确的序号")
        back4()


#定义一个log函数，用于用户登录
def log():
    print("欢迎使用电影评分系统1.0")
    global username
    username=str(input("请输入您的用户名："))
    f=csv.columns
    if username in f:
        print("登陆成功,进入评分系统")
        menu5()
    else:
        print("此用户名不存在")
        back3()

#定义rename函数，用于用户更改用户名
def rename():
    global username
    print("欢迎使用电影评分系统1.0")
    a=str(input("请输入新用户名："))
    if a in csv.columns:
        print("此用户名已被占用，请重新输入")
        rename()
    else:
        csv.rename(columns={username:a},inplace=True)
        username=a
        csv.to_csv("电影记录.csv",index=False)
        print("用户名已修改为{}".format(username))
    back3()

#定义out函数，用于用户登出
def out():
    global username
    username=""
    back3()


def back1():
    a=int(input("输入0即可返回主界面："))
    if a==0:
        print("")
        menu1()
    else:
        print("")
        back1()

def back2():
    a = int(input("输入0即可返回上一界面："))
    if a == 0:
        print("")
        menu2()
    else:
        print("")
        back2()

def back3():
    a = int(input("输入0即可返回上一界面："))
    if a == 0:
        print("")
        menu3()
    else:
        print("")
        back3()

def back4():
    a = int(input("输入0即可返回上一界面："))
    if a == 0:
        print("")
        menu4()
    else:
        print("")
        back4()
def back5():
    a = int(input("输入0即可返回上一界面："))
    if a == 0:
        print("")
        menu5()
    else:
        print("")
        back5()

def start():
    print("欢迎使用电影评分系统1.0")
    print("请选择下列功能,输入对应功能前的数字即可")

#主界面
def menu1():
    try:
        start()
        print("---（1）当前收录电影  （2）影片查询    （3）影片评分---")
        print("此界面输入0可退出程序")
        order1=int(input("请输入选择的功能序号："))
        if order1==1:
            print("")
            menu4()
        elif order1==2:
            print("")
            menu2()
        elif order1==3:
            print("")
            menu3()
    except:
        print("请输入正确的序号")
        print("")
        back1()


#查询界面
def menu2():
    try:
        start()
        print("---------------------------------------------------------分类搜索----------------------------------------------------------")
        print("---（0）返回上一级    （1）影片名称    （2）影片类型    （3）影片产地    （4）影片主演    （5）上映年月    （6）时长---")
        order2=int(input("请输入选择的功能序号："))
        if order2==0:
            print("")
            back1()
        elif order2==1:
            print("")
            searchname()
            print("")
            back2()
        elif order2==2:
            print("")
            type()
        elif order2==3:
            print("")
            bornland()
        elif order2==4:
            print("")
            mainactor()
        elif order2==5:
            print("")
            borntime()
        elif order2==6:
            print("")
            time()
    except:
        print("请输入正确的序号")
        print("")
        back2()


#登录界面
def menu3():
    try:
        start()
        print("----------------------注册/登录---------------------")
        print("---（0）返回上一级    （1）注册用户名    （2）登录用户名---")
        order3=int(input("请输入选择的功能序号："))
        if order3==0:
            back1()
        elif order3==1:
            register()
        elif order3==2:
            log()
    except:
        print("请输入正确的序号")
        back3()

#信息界面
def menu4():
        print("欢迎使用电影评分系统1.0")
        print("")
        moviename()
        print("")
        start()
        print("---（0）返回上一级    （1）查询影片信息    （2）添加影片信息---")
        b = int(input("请输入选择的功能序号："))
        if b == 0:
            print("")
            back1()
        elif b == 1:
            print("")
            menu2()
        elif b== 2:
            print("")
            Add()
        else:
            print("")
            print("请输入正确的序号")
            back4()


#评分界面
def menu5():
    try:
        start()
        print("---（0）返回上一级    （1）电影评分    （2）查看历史评分    （3）查看他人评分    （4）重命名    （5）登出---")
        c=int(input("请输入选择的功能序号："))
        if c==0:
            print("")
            back3()
        elif c==1:
            print("")
            score()
        elif c==2:
            print("")
            review()
        elif c==3:
            print("")
            lookthrough()
        elif c==4:
            print("")
            rename()
        elif c==5:
            print("")
            out()
    except:
        print("请输入正确的序号")
        print("")
        back5()

#启动器
def launcher():
    print("----------carrot作品----------")
    menu1()
launcher()
'''csv.insert(6,'carrot',' ')
csv.insert(7,'apple',' ')
csv.loc[3,'carrot']=89
csv.loc[100]={'电影名':1,'类型':2}
print(len(csv.columns))
a=csv.loc[0,"carrot"]
print(a)
print(list(csv.columns))
print(list(csv['类型']))
A=['动画/冒险']
B=str(A)
C=B.split('/')
print(len(C))
a='2013年2月20日'
b=a.split('年')
c=str(b)
d=c.split('月')
print(d)'''

