### 1.6 习题
```
1.	分别以交互模式和脚本模式。
 	   1) 打印图案 
 	            *
          *   *
        *   *   * 
      *   *   *   * 
 	    2) 计算半径是2.5的圆的面积
 	    3) 输出下列语句
 这是我的第一个Python程序 
 This is my first Python grogram!
2.	假如有100元存入银行，每年利息是5%，在下列程序的最后添加Python代码计算8年后的存款总额。
3.	写出对二进制数17和32的加法运算结果。
4.	将十进制整数765431转换为十六进制，在十六进制形式下，如何将该数的二进制的第17位设置为1？最后写出对应的二进制形式。
5.	请在网上查询一下换行符、回车符、制表符和汉字‘汉’的Unicode编码点（值），然后根据表1-4写出其对应的UTF-8的编码。
```

#### 2.9 习题

```
1.	下面哪些是Python整型数？哪些是浮点数：
    11, 17.5, -39, -2.3, 0.12e4，-3.141759, 0.57721566, 7.5e-3
2.	当你在解释器输入1e1000或 -1e1000显示的值是什么？其含义是什么？type(1e1000)是什么？
3.	如何检查None的类型是什么？
4.	下列那句代码会抛出错误？
A）	"I have " + str(5) + " books"
B）	"I said " + ("Hello " * 2) + "1 world"
C）	True + False
D）	"The correct answer to this question is: " + 2
5.	为了提高程序效率，对于不可变的整数对象，Python解释器开始执行时就为这些对象分配了内存空间，不会被删除回收，因此，多个相同值的整数，可能对应的是同一个对象。相同值的整数是否共享同一个对象，取决于你解释器。例如在jupyter notebook解释执行时，[-5,256]范围的小整数都会共享同一个对象。请在jupyter nbotebook和操作系统命令行执行下列Python代码，看看输出是多少。
print(id(100))
print(id(100))
print(id(1000))
print(id(1000))
a=100
b=100
c=1000
d=1000
print(a==b)
print(a is b)
print(c==d)
print(c is d)
6.	 (选做题) sys模块（模块概念在第3章介绍）的函数getsizeof()可查询一个对象占用内存大小，例如：
import sys   #导入模块sys
sys.getsizeof(3.14)  #调用sys模块中的getsizeof查询3.14占据内存的字节数
输出： 24 
模仿这个程序，在该函数中输入整数3、'h'、'hello'、'hello world'观察输出是多少？
7.	定义2个变量radius和area分别表示圆的半径和面积，其中radius有一个初始值，而area的值通过圆的面积公式计算。然后输出它们的值。
8.	对习题1.6中的存款问题，用一个变量savings表示存款，用一个interest表示年利息如0.05，用一个变量growth_multiplier表示年增长倍数（1+interest），并用指数运算**计算8年后的存款总额保存在结果变量result，最后输出表示存款总额的result值。
9.	下面哪些是不合法的标识符？为什么？
    @name    def    3re   user_1name  pass-word   _x   234
10.	先说出程序输出是什么，再运行这个程序。程序中有几个对象？几个变量？
a = 100
b = a
a= 101
print(b)
11.	list是一个复合数据类型，其中的元素可以是任何对象，对于下面的list对象alist。 
s = 'he'
pi = 3.14
alist = [1,[2,3],s,True, pi]
解决下列的4个问题。
1）输出最后一个元素
2） 输出最后2个元素
3）在最后一个元素前面插入字符串'py'
4）将第3个元素替换为list对象[4,5]
5) 删除前2个元素
12.	指出下列代码中的错误，并说明原因。
a=(1,3.14,'hello',{2,3} )
a[2] = 'hello'
b = {1,3.14,'hello',{2,3}}
b[0] = 2
c = {{2,3}:'hello','hello':{2,3}}
13.	先说明下列语句的输出是什么，然后将双引号表示的字符串换成单引号表示的字符串。
print("Yes!\tI\'m a student .\n"
14.	给定变量x和y，使用字符串格式打印出x和y及其总和的值。例如，如果x = 5且y = 3，则输出结果应该是：5 + 3 = 8。
15.	如何检验(25,)表示的是一个tuple而(25)表示的是一个整数？
16.	每个学生包括姓名和分数，用姓名作为键，分数作为值，用一个dict存储一组学生数据，并通过键值修改或输出某个学生的分数。
17.	下列代码有哪些错误？原因是什么？
a = (2, 3.14, 'python', [4,5])
b = {2, 3.14, 'python', [4,5]}
a[3][0] = 'he'
a[1] = 'abc'
b[3][0] = 'he'
print(a[-5])
print(a[-3])
print(b[3])
18.	编写程序从键盘输入矩形的长宽，输出矩形面积。
19.	下列print语句有没有错误？没有错误时，输出是什么？
print(3.14/2+True)
print(2*'hello')
print(2+'hello')
20.	下列代码可将一个字符串用'.'拆分成一个数据元素是字符串的list对象。
s = '10.3.9.12'
alist= s.split('.')  #split()函数以分隔符'.'拆分字符串
print(alist)
21.	IP地址是由4个整数构成的一个字符串，如'10.3.9.12'，编写一个程序，从键盘输入一个ip地址，按照下列步骤将它转化为一个整数输出。
1) 将字符串表示的ip地址的每个整数转化为二进制字符串，例如：
10 00001010 3 00000011 9 00001001 12 00001100
2) 再拼接为一个更长的二进制字符串：00001010 00000011 00001001 00001100
3) 最后将这个二进制字符串转换为整数。
22.	下列代码可以将一个整数转化为一个ip地址的4个整数。运行这个程序，并改写为从键盘输入一个整数，输出一个形如'10.3.9.12'字符串形式的ip地址。 
a = 123456789
a,b = a%256,a//256
b,c = b%256,b//256
c,d = c%256,c//256
print(d,c,b,a)
23.	整数和浮点除法有什么区别？整数除法和浮点除法的运算符分别是什么？
24.	以下操作的结果如何？解释为什么：
1.5 + 2
1.5 // 2.0
1.5 / 2.0
1.5 ** 2
25.	下列运算的结果是什么？为什么? （优先级和结合律）
15 + 20 * 3      13 // 2 + 3      31 + 10 // 3 
20 % 7 // 3      2 ** 3 ** 2                
26.	执行下面的语句会发生什么？为什么？
1 // 0 
27.	下面是用于判断一个年份是否是润年的表达式，请给该表达式添加圆括号，以清楚表示运算符的计算次序
year % 4 == 0 and year % 100 != 0 or year % 400 == 0
28.	下列哪些类型是可变的(mutable)哪些是不可变的(immutable)？如何验证？
list, dict, set,byte array,int, float, complex, string, tuple, frozen set,bytes
29.	下列代码有什么错误？为什么？
a=(1,2,3,[4,5,6])
a[0] = 10
a[3] = 30
a[3][2] = 'he'
30.	下列代码有什么错误?请改正：
number = input("请输入一个数: ")
print(type(number))
print(number+30)
31.	下面的代码未正确的缩进，请修改正确。
if score < 60: 
print(‘不及格’) 
else:
print(‘及格’)

i=0
while i<10:
print(i)
32.	根据 “四年一闰，百年不闰，四百年再闰” ，即“闰年是年份能被4整除且不能被100整除，或者能被400整除”这一规则，写一个程序判断一个年份是否闰年？
33.	编写程序，从键盘输入一个人的身高和体重，根据BMI指数公式，输出这个人是否肥胖的判断结果。
附： BMI指数 = 体重除以身高的平方
 根据BNI指数判断一个人肥胖的公式是：
  低于18.5：过轻
  18.5-25：正常
  25-28：过重
  28-32：肥胖 
  高于32：严重肥胖
34.	编写程序，从键盘输入摄氏温度，将其转化为华氏温度并输出
35.	从键盘输入一个一元二次方程 的系数，根据不同情况（无根、一个根、2个根）而输出不同的信息。
36.	打印金字塔图案,假设行数从键盘输入，打印输出如下的金字塔。
          *
        *   *
      *   *   *
    *   *   *   *
37.	从键盘输入一个弧度x，计算正弦函数sin（x）的值。要求最后一项的绝对值小于10-5，并统计出此时累计的多少项。 sin(x)的近似计算公式为：
 
38.	模仿整数之和的程序，将统计学生平均成绩的程序改写成用break语句终止循环体的执行
39.	编写一个程序，判断从键盘输入的一个整数是否是质数 
40.	猜数字游戏：假设程序中设置了一个１到１００之间的正整数num，程序让用户从键盘输入一个猜想的数字guess，如果guess等于num，那么就显示成功的祝贺信息，如果失败就提示用户继续输入，直到超过的猜测次数（比如8次）就提示失败的信息！请完善下面的程序
 num = 37
 i = 0
 success = 0 #是否成功的标志
 while i<8:
   guess= int(input("请输入猜测的数字："))
   ?  
 
 if(success)
    print("很遗憾，猜测失败！")
continue
41.	编写程序计算1到1000之间的所有奇数之和。
42.	请去掉“猜数字游戏”中的success标志变量，使用循环语句的else子句改写“猜数字游戏”。
43.	编写一个程序对一个班级所有学生的某门课进行成绩分析，一个学生的数据包括：学号、姓名、平时成绩、实验成绩、期末成绩、总评成绩。总评成绩是平时成绩、实验成绩和期末成绩的加权平均，学生成绩数据、成绩的加权系数等都从键盘输入，程序包括：成绩录入、修改、查询、权系数的查询和修改、计算总评成绩、统计不同分数段的人数和百分比、最高分和最低分之差等。程序一直运行，直到用户输入一个特殊的退出按钮才退出。
如下是一个大致的框架，可在此基础上编写你的代码。
print('请输入代表不同命令的字母：')
help_info =('''
     'i' or 'I':'录入一个学生信息'
     'q' or 'Q':'按姓名查询学生信息'
     'm' or 'M':'按学号修改学生信息'
     'w' or 'W':'显示/修改加权系数'
     'c' or 'c':'计算所有学生的总评、统计信息'
     's' or 'S':'显示所有学生信息'
     't' or 'T':'显示统计信息'
     'x' or 'X':'显示统计信息'
     ''')
print(help_info)
student_infos = []
while True:
    cmd = input("请输入一个命令：")
    if cmd=='x' or cmd=='X': break 
    elif cmd=='i' or cmd=='I': 
        id = input("请输入学号：")
        name = input('请输入姓名:')
        score_ = float(input('请输入平时成绩:'))
        score_exp = float(input('请输入实验成绩:'))
        score_test = float(input('请输入期末成绩:'))
        student_infos += [[id,name,score_,score_exp,score_test,0]]
    elif cmd=='s' or cmd=='S': 
        #print(student_infos)
        for s in student_infos:
            print(s)
    pass
也可以用到后面要学习的list和str类型的方法简化上述的代码，如：
	假设用一个list对象(上述代码中的student_infos)存储所有学生的信息，可以用list的append()函数在最后添加一个元素，如：
student_infos.append([id,name,score_,score_exp,score_test,0])
	可以用str的split()函数将输入的字符串分割成多个字符串。当然，也可以一个一个的调用input()函数。
 id,name,score_,score_exp,score_test =
 input("请输入:学号、姓名、平时成绩、实验成绩、期末成绩：").split(' ') 
 score_ = float(score_) 
 score_exp = float(score_exp) 
 score_test = float(score_test)
```

#### 3.9 习题

```
1.	下列关于函数正确的是（ ）
A. 函数是用于创建对象的             B. 函数使代码执行更快 
C. 函数是完成特定工作的代码片段     D. 上述陈述都对
2.	下列代码的输出是什么？
     def printJob(name,job):
        print(name)
        print("你的工作是：",job)     
     printJob("hwdong","教小白精通编程")
3.	如果函数中没有return，则函数返回的是（ ）
 A.  0               B. None
 C.  任意整数        D. python的函数必须包含return语句
4.	完善下面的根据BMI指数判断一个人是否超重(BMI指数小于25，表示未超重，否则就超重)的函数。并编写代码：从键盘输入身高和体重，测试这个函数。
def overweight_by_BMI(name ,height,weight):
      bmi = ?     # 用bmi变量表示BMI指数
      if ? :
         print(name,"没有超重")
      else    
         print(name,"超重了")
      print("你的BMI指数是:",bmi)
      return bmi
5.	下列代码是否有错误？为什么？输出是什么？
x = "global"
def fun(x):
    x = x*2
    print(x)

fun(x)
print(x)
6.	编写一个非递归的函数接受一个整数参数n，返回这个n对应的斐波那契（Fibonacci）序列，可以用一个list保存这个序列，例如Fib(100)返回的Fibonacci序列是：
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
然后，从键盘输入一个整数，调用这个函数并打印结果。
7.	定义一个求一元二次方程的函数，方程的系数作为3个参数，返回一个无解、1个解或2个解的结果。并从键盘输入方程系数，测试函数是否能够正确求解。
8.	编写一个函数，计算传入字符串中的数字、字母、空格和其他字符的个数
9.	写一个函数，将传入的list对象的元素每间隔3个选择一个元素，构造并返回一个tuple对象。例如：
输入：[1,2,3,4,5,6,7,8,9]，输出：(1,4,7)
10.	将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”。假设所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符。
11.	重新实现习题2.40的学生成绩分析程序，用一系列函数完成单独的功能。如专门的函数用于输入一个学生的信息。
12.	编写一个函数，不调用内置的排序函数，对3个数进行排序和输出，并附带一个默认参数reverse=False，表示默认从小到大排序，当该形参对应的实参为True时，则从大到小排序。
13.	编写一个可以求多个数的乘积的函数Product()，可以接受1个或多个数作为参数。运行示例如下：
print(‘Product(3)’ , Product(3)) 
print(‘Product(3,4)’ , Product(3,4))
print(‘Product(3,4,5)’ , Product(3,4,5))
…
14.	编写一个函数Student()，除学生名外，还接受可变数目信息和关键字信息，返回将学生信息以list对象形式返回。运行示例如下：
Student(‘Li’,23)
Student(‘Li’,21,’男’,class=’计科3班’,’city’= ‘Shanghai’,’phone’=’12381233451’)
15.	递归函数是（  ）
A. 在程序中调用所有函数的函数       B.  调用自身的函数
C. 调用除自身以外的所有函数的函数   D. Python没有递归函数的概念
16.	写一个函数输入一个整数n，输出n行的Pascal 三角形，如图所示：
               1
            1     1
         1    2     1
      1    3    3      1
   1    4    6    4      1
1    5    10    10    5    1
17.	下列程序的输出是什么？
result = lambda x: x * x
print(result(5))
A. lambda x: x*x             B. 10
C. 25                        D. 5*5
18.	下列代码的输出是什么？
numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x , numbers))
print(newNumbers)
A. [1, 3, 6]              B. (1, 3, 6)
C. [2, 6, 12]             D. (2, 6, 12)
19.	改写前面的“猜数字游戏”程序，用随机数模块random的随机数函数随机生成一个“待猜的数字”。
20.	用普通函数和Lambda函数定义下列函数：
1）2个输入参数，返回这2个数的平方和的根。
2) 可接受任意个数的数，并计算这些数的平均值。如果没有输入任何数，则平均值为0。
3）输入一个字符串，返回一个不包含重复字符的字符串。
21.	利用 map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
例如，输入： [‘adam’, ‘LISA’, ‘barT’]，输出： [‘Adam’, ‘Lisa’, ‘Bart’]
22.	假如要输出math模块中的常数pi,下列正确的是( )
A. print(math.pi)                              B. print(pi)
B. from math import pi
   print(pi)
C. from math import pi
   print(math.pi)
23.	下列哪个运算符用于从一个包导入一个模块？
A.  .运算符    B.    * 运算符    C. -> 运算符     D.  , 运算符
```

#### 4.8 习题

```
1.	下面哪个是不正确的？
A. x = 0b101           B.  x = 0x4f5    C. x = 19023   D.  x = 03964
2.	下面的代码输出是什么？
print(1j)
A. <type 'float'>   B. <type 'dict'>    C.   <type 'unicode'>    D.   <type 'complex'>
3.	下面的说法是否正确？
Python有2种数值类型：integer整数和有符号数 
A. True B. False
4.	写一个语句，以二进制、十进制、八进制、十六进制形式输出一个整数23。
5.	语句print(0.2 + 0.2 == 0.5)的输出是
A. True          B. False       C. 机器依赖        D. 错误Error   
6.	下面哪句是错误的？
A.   float(‘inf’)           B.  float(‘nan’)          
C.   float(’56’+’78’)       D.  float(‘12+34’)
7.	编写一个函数Sin(x)按照第二章的34题计算正弦函数sin(x)的值, 用math模块的函数pow()和factorial()计算指数和阶乘，调用下列代码测试你的Sin(x)函数。并和math模块自带的sin(x)函数的结果进行比较。
print(Sin(math.pi/2))    # returns 1.0
print(Sin(math.pi/4))    # returns 0.7071067811865475
8.	下面哪个命令可创建一个list对象？
A.  list1 = list()          B. list1 = []      
C. list1 = list([1, 2, 3])    D.  上述都可以
9.	插入5成为alist的第3个元素，应该用哪个命令?
A.  alist.insert(3, 5)       B. alist.insert(2, 5)
C.  alist.add(3, 5)         D. alist.append(3, 5)
10.	下列代码的输出是（ ）?
lst=[[1,2],[3,4]]
print(sum(lst,[]))
A.	[[3],[7]]              B. [1,2,3,4]
c)	Error                D.	[10]
11.	下列代码的输出是( )
x=[[1],[2]]
print(" ".join(list(map(str,x))))
A.	[1] [2]               B.	[49] [50]       
C.	Syntax error          D.	[[1]] [[2]]
12.	下列代码的输出是什么?
a=[2,5,7]
a.append([17])
a.extend([3,11])
print(a)
13.	下列代码的输出是什么?
a=list((45,)*4)
print((45)*4)
print(a)
14.	下列代码的输出是什么？
matrix = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]] 
for i in range(0, 4):
    print(matrix[i][1], end = " ")
15.	下列代码的输出是什么？
points = [[1, 2], [3, 1.5], [0.5, 0.5]]
points.sort()
print(points)
16.	下列代码的输出是( )
def change(var, lst):
    var = 1
    lst[0] = 44
k = 3
a = [1, 2, 3]
change(k, a)
print(k)
print(a)
A. 3                B. 1              C. 3               D. 1
   [44, 2, 3]           [1,2,3]            [1,2,3]              [44,2,3]
17.	下列代码的输出是（）
L=["hello", "yes!", "a123"]
[n for n in L if n.isalpha() or n.isdigit()]
A.  [‘hello’, ‘yes’, ‘123’	]            B. [‘hello’]
C.  [‘hello’, ‘a123’]                  D. [‘yes!’, ‘a123’]
18.	下列代码的输出是什么？
[j for i in range(2,5) for j in range(i*2, 10, i)]
19.	编写程序：用list表示两个矩阵，计算它们的乘积并放入另外一个list对象中。哪个答案能打印如下的结果?
C:\Hwdong\String.doc
A. str='C:\Hwdong\Stri\ng.doc'         B. str='''C:\\Hwdong\string.doc'''
   print(str)                               print(str)      
C. str='C:\\Hwdo\ng\St\ring.doc'       D. str='C:\\Hwdong\String.doc'
   print(str)                               print(str)       
20.	下列语句的输出是（）
print("\x48\x49!")
A. \x48\x49!     B. 4849         C. 4849!     D.  48  E.  49!   F. HI!
21.	下列代码的输出是（）
str='hello world'
print (str[::-1])
A. world         B.   dlrow olleh        C.  hello world      D. hello
22.	下列代码的输出是什么?
str='Python is easy to learn, C is hard'
print(str.rfind('s'))
print(str.rfind('r'))
L = len(str)
print(str.count('is', -(L-2), -1))
print(str.endswith("rd"))
23.	web网页中的标记都是以"<>"开头和结尾的，中间的部分就是标记的内容，例如：<a href="string1">string2</a>表示的是一个超链接。编写代码抽取其中的内容即string2。
24.	下列语句的输出是( )。
print("Hello {name1} and {name2}".format('foo', 'bin'))
A. Hello foo and bin         B. Hello {name1} and {name2}
C. Error                     D. Hello and
25.	下列程序的输出是：
print('The sum of {0:b} and {1:x} is {2:o}'.format(2, 10, 12))
A. The sum of 2 and 10 is 12              B. The sum of 10 and a is 14
C. The sum of 10 and a is c               D. Error
26.	下列代码的输出是( )
print('abcdefcdghcd'.split('cd', 2))
A.  [‘ab’, ‘ef’, ‘ghcd’]             B. [‘ab’, ‘efcdghcd’]
C. [‘abcdef’, ‘ghcd’]                D. none of the mentioned
27.	编写程序，输入一个字符串，返回一个首尾各2个字符组成的字符串，例如’’string’返回的字符串是‘stng’，如果原字符串长度小于2，则返回一个空串。
28.	从键盘输入多个逗号隔开的字符串，将它们拼接成一个字符串。如输入：
'hello','world','abc'产生的是'hello world abc'。
29.	假如要修改tuple对象test的第3个元素为‘Python’,下面哪个是正确的？
A.  test[2] = 'Python'     B. test(2) = 'Python'  C. test[3] = 'Python'
D. 不能修改tuple的元素
30.	下列代码输出是什么？
my_tuple = (1, 2, 3, 4)
my_tuple.append( (5, 6, 7) )
print(len(my_tuple))
A. 5     B. 7     C. 2  D. Error 
31.	下列代码的输出是什么? ( )
d = {}
d[(1,2,4)] = 8
d[(4,2,1)] = 10
d[(1,2)] = 12
sum = 0
for k in d:
    sum += d[k]
print (len(d) + sum)
A. 30        B. 24       C. 33      D.12
32.	下列代码的输出是什么( )？
a = ('hello',)
n = 2
for i in range(int(n)):
    a = (a,)
    print(a)
A.	错，tuples是不可修改的   B.	 ((‘hello’,),)
                                    (((‘hello’,),),).
C. 	((‘hello’,)’hello’,)            D.    ((‘hello’,)’hello’,)
                                    (((‘hello’,)’hello’,)’hello’,)
33.	下列代码输出是什么（）
a,b=6,7
a,b=b,a
a,b
A.	(6,7)         B. Invalid syntax
C.	(7,6)         D. 没有任何输出
34.	下列代码的输出是什么?
a=(1,2)
b=(3,4)
print(a+b)
A. (4,6)                        B. (1,2,3,4)   
C. 错，因为tuple是不可修改的   D. 上述说法都不对
35.	关于set，正确的说法是（）
A.  一个set是数据元素的无序集合           B. set中的元素是唯一的.
C. 不同于tuple，可以修改set中的元素        D. 上述说法都对
36.	下面哪个创建set对象的语句是错误的？
A.    set([[1,2],[3,4]])         B. set([1,2,2,3,4])
C.    set((1,2,3,4))            D. {1,2,3,4}
37.	下列代码输出是什么()?
a={4,5,6}
b={2,8,6}
a+b
A.    {4,5,6,2,8}        B.    {4,5,6,2,8,6}
C.    Error错误，因为set对象无法使用+运算符
D.    Error错误，因为出现了重复的6
38.	下面哪一句产生的是集合x,y的对称差？
A.  x | y        B. x ^ y         C. x & y    D. x – y
39.	下面代码的输出是( )
a=[1, 4, 3, 5, 2]
b=[3, 1, 5, 2, 4]
print(a==b)
set(a)==set(b)
A  True        B. False        C. False         D. True
False          False           True             True
40.	下列程序的输出是( )
a={3,4,5}
a.update([1,2,3])
a
A.    错，set类型没有update()方法          B. {1, 2, 3, 4, 5}
C.    错, list不能加到set里                D. 错, list中有重复元素
41.	下列代码的输出是什么( )?
d = {0: 'a', 1: 'b', 2: 'c'}
for x, y in d:
    print(x, y)
A. 0 1 2    B. a b c        C. 0 a 1 b 2 c       D. 上述说法都不对
42.	下列代码的输出是什么( )?
d = {0: 'a', 1: 'b', 2: 'c'}
for x, y in d.items( ):
    print(x, y)
A. 0 1 2    B. a b c        C. 0 a 1 b 2 c       D. 上述说法都不对
43.	下列代码的输出是什么(  )?
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  
print(squares.pop(4))  
print(squares)
A. 16                                  B. 16
   {1: 1, 2: 4, 3: 9, 5: 25}              {1: 1, 2: 4, 3: 9, 4:16, 5: 25}
C. 4                                  D. 4
   {1: 1, 2: 4, 3: 9, 5: 25}              {1: 1, 2: 4, 3: 9, 4:16, 5: 25}
44.	下列代码的输出是什么( )?
a={1:"A",2:"B",3:"C"}
b={4:"D",5:"E"}
a.update(b)
print(a)
A.	{1: ‘A’, 2: ‘B’, 3: ‘C’}                    B. dict没有update()方法
C.	{1: ‘A’, 2: ‘B’, 3: ‘C’, 4: ‘D’, 5: ‘E’}    D. {4: ‘D’, 5: ‘E’}
45.	下列代码的输出是什么( )?
a={}
a[2]=1
a[1]=[2,3,4]
print(a[1][1])
A.	[2,3,4]        B.  3       C.	2        d. 	An exception is thrown
46.	写一个程序将如下的多个字典合并为一个字典。
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
合并为 {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
47.	网上有一篇Painless Q Learning的文章介绍了一个 “机器人”如果从一个建筑物的任意一个房间走出建筑物的探索问题。如图10-4是建筑物的房间布局：
   
10-4 走出房间问题
将房间作为图的顶点，将2个房间之间的门作为边，可以构造如图所示的一个图。边上的权值表示从一个门走向另外一个门的奖励。针对这个问题，请修改build_T_table函数，用于初始化该问题的数据，然后运行main()函数，观察执行结果。注意：目标状态走向自身的这个边在程序中可以忽略。
```

#### 5.7 习题

```
1.	下列程序的输出是什么？
class C:
  def Print(self, line='Python'):
    print(line)

a = C()
a.Print('Java')
2.	Python的__init__()函数的作用是（）
A. 为使用一个类而初始化             B. 对象实例化时调用的函数
C. 调用时，初始化数据属性的值为0    D. 上面的说法都不对
3.	下列代码的输出是（）
class Point:
    def __init__(self, x = 0, y = 0):
      self.x = x+1
      self.y = y+1

p1 = Point()
print(p1.x, p1.y)
A. 0 0         B. 1 1      C. None None       D. x,y
4.	解释属性name, surname 和 profession之间的区别，并说明不同实例中这些属性的可能值。
class Smith:
 surname = "Smith"
 profession = "smith"

 def __init__(self, name, profession=None):
     self.name = name
     if profession is not None:
         self.profession = profession
5.	对于下面的表示二维平面上的点的类Point，补充完善__str__() 函数，使得对一个Point变量p，print(p)函数打印(x,y)格式。另外，重载定义+、-、<、==运算符，使得对两个点p、q，可直接使用p+q或p-q得到一个新的Point对象，可以用p<q或p==q比较它们的大小或是否相等。
class Point:    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        #补充你的代码， 
        #...
6.	下列程序的输出是什么？ ( )
class A():
    def disp(self):
        print("A disp()")
class B(A):
    pass
obj = B()
obj.disp()
A.非法的继承语法       B. 创建对象错误，缺少参数
c) 什么也不输出        D. A disp()
7.	下列程序的输出是什么？ ( )
class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y
def main():
    obj = der()
    print(obj.x, obj.y)
A.	错，调用方法的语法错了
b)	程序没任何错误，但不输出任何信息
c)	1 0
d)	1 2
8.	如果一个类从2个不同的类派生，称为（）
A. 多层继承    B.多继承   C. 层次继承  D. Python继承
9.	下列程序的输出是什么？
class C1:
    def __init__(self):
        self.x = 1
class C2(C1):
    def __init__(self):
        super().__init__()
        self.x = 2
class C3(C2):
    def __init__(self):
        super(C3,self).__init__()
        self.x = 3
        
a = C1()
b = C2()
c = C3()
print(a.x,b.x,c.x)
10.	下列程序的输出是什么？
class C1:
    def __init__(self):
        print('C1')   
    def f(self):
        print('f in C1')   
    
class C2:
    def __init__(self):
        print('C2')
        super().__init__()
    def f(self):
        print('f in C2')  
       
class C3(C1, C2):
    def __init__(self):
        print('C3')
        super(C3,self).__init__()
    def g(self):
        print('g in C3')  
        print('call f in C2') 
        C2.f(self)
        
c = C3()
c.f()
c.g()
11.	模仿下面的类circle（圆）的代码，完善定义表示二维几何图形的类Polygon（多边形）、Rectangle（矩形）、正方形（Square）、三角形（Triangle）。假设类shape是类的直接（间接）基类。
class Shape:
   def paint(self): pass
   
class Circle(Shape):
   def __init__(self, x, y, r):
      self.x = x
      self.y = y
      self.r = r
      
   def paint(self): 
      print("画半径是{}、圆形在({},{})的圆",self.r,self.x,self.y)

class Polygon(Shape):
   #...
class Rectangle(Polygon):
   #...
class Square(Rectangle):
   #...
class Triangle (Polygon):
   #...
12.	定义一个Person类，包含name（姓名）、sex（性别）、age（年龄）、address（住址）、email（电子邮箱）、phone（电话号码）等信息，然后在此基础上定义Student（学生）、Staff（员工），然后在Staff基础上定义Teacher（教师）。Student假设有一个dict属性记录其每门课程的学分，Staff假设至少有一个salary属性表示其薪水，Teacher有一个list对象存储其能教授的所有课程。在这些类的基础上写一个简单的学校人员管理程序，包含输入、查找、修改、删除、显示等操作。
13.	实现二叉树的其他操作，如求一个二叉树的叶子结点数目、复制一颗二叉树、判断二叉树是否是相等或具有相似结构等等。
14.	在BiTreeNode类的基础上，实现一个较为完善的二叉搜索树类BST，其中包含插入、查找、删除、修改、打印等操作，这些操作都作为BST类的方法而不是外部函数实现。
```

#### 6.3 习题

```
1.	open()函数中的文件模式参数“r, a”的含义是什么（  ）?
A) 读，追加    B) 追加、读    C)  A和B都对   D)  A和B都不对
2.	二进制读写模式是哪一个？(   )
A)  wb+         B)  w        C)  wb         D)  w+
3.	下面哪句是正确的？（）
A) 当以读模式打开一个不存在文件时，会出现错误
B) 当以写模式打开一个不存在文件时，会创建一个新文件
C)  当以写模式打开一个存在文件时，存在的文件会被新文件替换
D) 上述都对
4.	下列代码做什么(  )?
f = open("test.txt")
A) 以读写方式打开test.txt
B) 以读方式打开test.txt
C) 以写方式打开test.txt
D) 以读或写方式打开test.txt
5.	写一个程序找出一个文件中最长的单词。
6.	编写一个程序，从键盘上输入一组学生的信息（假如每个学士有姓名、学号和分数3个数据项），要求一个学生的信息在一行中输入，将所有学生的信息写入到一个文本文件中，再从文件中读取并显示所有学生的信息，要求每个数据项占据固定的宽度并左对齐。然后修改第3个学生的信息，并将修改后的学生信息写到文件中，并再次读入显示所有学生数据以验证数据是否正确的被修改了。
7.	编写一个程序，从键盘输入一组三维坐标点数据，将这些数据写入到一个二进制文件中，然后单独读取第3个坐标点的数据，修改后再写入到文件中。
```

#### 7.4 习题

```
1.	找出下面程序中的语法错误，并解释错误的原因。
1）myfunction(x, y):
     return x + y
2）else:
     print("Hello!")
3）if mark >= 50
     print("You passed!")
4）if arriving:
      print("Hi!")
   esle:
      print("Bye!")
5）if flag:
   print("Flag is set!")
2.	找出下面的运行时错误(逻辑错误)
1）product = 0
for i in range(10):
    product *= i
2） sum_squares = 0
for i in range(10):
    i_sq = i**2
sum_squares += i_sq
3） nums = 0
for num in range(10):
    num += num
3.	一个try-except块可以有多少异常处理语句(except statements)？
A.  0         B. 1    C. 多于1个        D.多于0个
4.	打开一个不存在的文件会发生什么？（）
A. 创建一个新文件        B. 什么也不发生 
C.抛出一个exception      D.上述说法都不对
5.	 try-except-else的else子句什么时候执行？( )
A. 总会执行               B. 异常出现时才执行      
C. 没有异常发生时才执行   D. 当except块中发生异常时才执行
6.	下列代码的输出是什么？( )
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

A.   1         b.    2    C. 3    
D. 错，在一个try-finally有多于一个return语句
7.	下列代码的输出是什么？
number = 5.0
try:
    r = 10/number
    print(r)
except:
    print("Oops! Error occurred.")
A. Oops! Error occurred.     B. 2.0
C.2.0 Oops! Error occurred.   D. None object
8.	下列代码做什么？
try:
  # code that can raise error
   pass
  
except (TypeError, ZeroDivisionError):
  print("TWO")
A. 只要出现异常exception(不管什么异常）就打印TWO
A. 不出现异常exception时就打印TWO
C. 出现TypeError 或 ZeroDivisionError异常就打印TWO 
D. 当TypeError和 ZeroDivisionError异常都出现时才打印TWO 
9.	对字符串strtext = “Welcome”，下面哪句会产生TypeError
A.  strtext[1]= ‘r’
B.  print (strtext[0])
C.  print(strtext.strip())
D.  print (strtext.lower())
E.  None of these
10.	下列代码的输出是（）
def  Test():
    try:
        print(20)
    finally:
        print(30)
Test()
A.  30       B.  20       C.  30      D.  20       E.  None
    20          30                       5        
14. 下列代码的输出是（）
try:
    print("throw")
except:
    print("except")
finally:
    print("finally")
A.  finally     B.  throw     C.  finally    D.  Syntax error    E.  except
except        finally        throw                         finally
```

#### 8.7 习题

```
1.	如何从一个list对象创建一个迭代器对象？
A. 将给定的list对象传递给iter()函数    B. 用一个for循环
C.用一个 while 循环                    D. 无法从list对象创建一个可迭代对象
2.	包含了yield语句的函数是（）
A. 可迭代的            B.生成器函数
C. 匿名函数            D.上述说法都不对
3.	在?处补充代码完善下面的生成器函数，使得可以生成一对整数之间的所有整数。
def counter(low, high):
    current = low
    while current <= high:
        ？
for c in counter(3, 8):
    print c
4.	下列程序的输出是( )
my_list = [1, 3, 6, 10]
a = (x**2 for x in my_list)
print(next(a), next(a))
A. 1 3           B. 1 9         C. 1 9 36 100       D. 1
5.	写一个程序，接受1个或多个文件名作为参数，输出文件中字符个数少于60的那些行。
6.	写一个函数，输入一个整数n和一个文件名，将这个文件分割成每个文件都是n行的多个文件（除最后一个文件可以少于n行）。
7.	8.3.1中用如下的代码来装饰say()和hello()函数，从而给say()和hello()函数添加了功能。
wrapper(say)     
wrapper(hello)    
但调用say()和hello()的代码都要替换成上面的调用形式，为此，在wrapper()外层又定义decorator()函数来返回装饰say()和hello()函数，使得调用say()和hello()函数的代码不会受到任何影响。
say = decorator(say)      
hello = decorator(hello) 
那么，为什么不可以直接用如下形式包装say()和hello()函数呢？
say = wrapper(say)
hello = wrapper(hello) 
8.	哪个函数是装饰器函数？
def mk(x):
    def mk1():
        print("Decorated")
        x()
    return mk1
def mk2():
    print("Ordinary")
p = mk(mk2)
p()
A.  p()   B. mk()    C. mk1()    D. mk2()
9.	假如f是一个装饰器函数，下面2个代码片段是否是等价的？（ ）
片段1：
@f
def f1():
     print(“Hello”)
片段2：
def f1():
     print(“Hello”)
f1 = f(f1)
A. True B. False
10.	下列代码的输出是( )
def d(f):
    def n(*args):
        return '$' + str(f(*args))
    return n
@d
def p(a, t):
    return a + a*t 
    
print(p(100,0))

A. 100    B. $100      C. $0    D. 0
11.	运行下列的代码，并给student()函数添加位置参数(name和age)、可变参数(如address、class、mobile)和字典参数（如每门课对应的成绩：{‘C’:80,’Python’:90,’DS’:70.8}），并在student ()函数中输出这些参数。
   def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

@make_bold
@make_italic
@make_underline
def student():
    return "a student"
print(student())    # 输出： "<b><i><u>a student</u></i></b>"
12.	定义表示日期的Date类，其中的属性的读写都采用@property。
13.	请为上述的Date类写一个类方法，用于修改Date类的类属性default_date。
14.	结合生活中的例子说明“深拷贝”的含义。
```
