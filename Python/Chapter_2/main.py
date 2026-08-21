# letter = '''Dear <|Name|>,
# YOU R SELECTED,
# Today's <|Date|>''' 
# name = input("ENTER YOUR NAME\n")
# date = input('ENTER TODAYS DATE\n')
# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", date)
# print(letter)

# a = "if i were u i were never let u  go"
# detct = a.find("  ")
# print(detct)

# a = "if i were u i were never let u  go"
# detct = a.replace("  "," ")
# print(detct)

# a = input("First")
# b = input("Second")
# c = input("Third")
# d = input("Fourth")
# all = [a,b,c,d]
# print(all)

# a = [2,32,23,1]
# a.sort()
# print(a)

# a = int(input("First\n\t"))
# b = int(input("Second\n\t"))
# d = [a,b]
# e = (a+b)
# print(d)
# print(e)

# a = (2,32,32,32,2,)
# b = a.count(32)
# print(b)

# a = input("FIRST\n")
# b = input("SECOND\n")
# c = input("THIRD\n")
# set = {a,b,c}
# print(set)

###################################################################
# a = {
#     "boy": "ladka",
#     "girl": "ladki"
# }
# print(a.keys())
# b = input("Enter YOur PRoblem key")
# print("ur ans is", a[b])

######################################################################
# a = {}
# b = input("enter your favourite language b bruh")
# c = input("ENTer your favourite language c bruh")
# a['b bruh'] = b
# a['c bruh'] = c
# print(a)

# a = 22 
# if (a>9):
#     print("greater")
# else:
#     print("lesser")

# b = int(input("YOur age"))
# if (b>=18):
#     print("yes")
# elif(b<18):
#     print("okh")
# else:
#     print("noo")

#################################################################
# a = input("enter first number; ")
# b = input("enter second number; ")
# c = input("enter third number; ")
# d = input("enter fourth number; ")

# if (a>b):
#     f1 = a
# else:
#     f1 = b
# if (c>d):
#     f2 = c
# else:
#     f2 = d

# if (f1<f2):
#     print(f2 , " is greatest ")
# elif (f2<f1):
#     print(f1 , "is greatest")

'''TAKING THE PERCENTAGE 30 OR 40 TO PASS IN EACH SINGLE SUBJECT'''
# maths = int(input("enter marks of maths:\n"))
# english = int(input("enter marks of english:\n"))
# sst = int(input("enter marks of sst:\n"))
# if (maths>40 and 30):
#     print("pass")
# elif (maths<30 and 40):
#     print("fail")
# if (english>40 and 30):
#     print("pass")
# elif (english<30 and 40):
#     print("fail")
# if (sst>40 and 30):
#     print("pass")
# elif (sst<30 and 40):
#     print("fail")

'''TAKING THE PERCENTAGE 30 OR 40  TO PASS IN ALL SUBJECTS '''
# MATHS = int(input("ENTER YOUR MARKS:\n"))
# ENGLISH = int(input("ENTER YOUR MARKS:\n"))
# SST = int(input("ENTER YOUR MARKS:\n"))
# if (MATHS<33 or ENGLISH<33 or SST< 33):
#     print("fail")
# elif (MATHS + ENGLISH + SST)/3 > 40:
#     print("pass")


# text = "your have a chance to win a ASUS LAptop and another one is YOUR paytem has credited 20000 plz click in this link and get your reward!!!"
# if (" a chance to win "in text):
#     print("this is a spam")

# if ("YOUR paytem has credited "in text):
#     print("this is a spam")

# if ("you have been chosen for" in text):
#     print("this is not  a spam")
# else:
#     print("this is a spam")


# a = input("enter your name\n")
# if (len(a) is 10):
#     print("correct")
# else:
#     print("incorrect")

# a = ("gojo sotaru", "kakashi hatake", "anya")
# if ("anya" in a):
#     print("anya is in there \n\t but ")
# if ("gojo" in a ):
#     print("goju is in there ")
# else:
#     print("gojo is not in there")


# marks = int(input("enter ur percentage"))
# if marks>=90:
#     print("excellent")
# elif marks>=80:
#     print("A")
# elif marks>=70:
#     print("B")
# elif marks>=60:
#     print("c")
# elif marks>=50:
#     print("D")
# else:
#     print("fail")

# list = ['amensia', 'anxiety','low confident']
# a = 0
# while a<len(list):
#     print(list[a])
#     a = a+1

# for i in range(12):
#     if i % 3:
#         continue
#     print(i)

'''printing table of 5 by different types'''
# for a in range(5, 55):
#     if a % 5:
#         continue
#     print(a)

# for a in range(5, 55, 5):
#     print(a)


# for a in range(1,11):
#     print(a*5)

# b = int(input("enter 5"))
# for a in range (1, 11):
#     print(f"{b} X {a} = {b*a}")

'''solving the above prob by while loop'''
# a = 0
# while a<=45:
#     a = a+5 
#     print(a)


# a = int(input("a number"))
# prime = True
# for i in range (2, a):
#     if (a%i == 0):
#         prime == False
# if prime:
#     print('this is prime number')
# else:
#     print("this is not prime number")

# n = 4
# for i in range (4):
#     print("*" * (i+1))

# n = 1
# for i in range (1):
#     print("  *  ")
#     print(" *** ")
#     print("*****")

# for i in range (1):
#     print("   *\n  ***\n*******")
#     break

# def maximum(a,b,c):
#     if (a>b):
#         if (a>c):
#             return a
#         else:
#             return c
#     else:
#         if (b>c):
#             return b
#         else:
#             return c

# m=maximum(3,59,2) 
# print("value " + str(m) + " is greatest")

# def convert(f):
#     return (f*(5/9))-32
# f = int(input("iern"))
# convert = convert(f)
# print(convert)

# def fck(f):
#     if f>34:
#         print("sfckoff",end=" ")
#         print("jhgfdfghj")
# f = int(input("sfwd"))
# fck = fck(f)
# print(fck)


# def con(i):
#     return i*2.54
# i = 7
# con = con(i)
# print("inche into cm is ", con)

# def tb(n,):
#     for t in range (1,11):
#         print(f"{n} X {t} = {n*t}")
# n = 5
# tb = tb(n)   

# def st(n):
#     for i in range(3):
#         print("*" * (n-i)) # first i = 0, then 1, then 2
# print(st(3))

# def sum(n):
#     return n * ( n +  1 )*2  
# n = 5
# sum = sum(n)
# print(sum)

#####################################################@
# def one_two(one ,two):
#     h = one.replace(two,"")
#     return h.strip()
# three = "   i am d boy   "
# four = one_two(three,"i am")
# print(four)

################################################################
# a = int(input('enter'))
# k = 1
# for i in range (1 , a+1):
#     k = k*i
# print(f"the factorial of{a} is {k}")

# b = int(input("enter"))
# for a in range(-10,0): #only print reverse table when the number(b) is in (-)
#     print(f"{b} X {a} = {b*a}")

############################################################################### --> new function found '''reversed(ranged)'''
# b = int(input("enter"))
# for a in reversed(range(0,11)): 
#     print(f"{b} X {a} = {b*a}")

######################################################
# n = int(input("enr"))
# a = n * ( n +  1 )*2
# while n<a:
#     if True:
#         print(a)
#         a == 1
#         break

# a = 1
# for i in range(3):
#     print("*" *(a+i))

# a = 1
# for i in range(3):
#     if a<i:
#         print("* " *(a+i))
#         print("*  " * (a*1),"*" * (a*1))
#         print("* " *(a+i))
#         i == 1
#         break

#############################################################################################
# import os 
# if os.path.exists('Chapter_2'):
#     with open('poems.txt',"a") as f:
#         f.write("twinkle")
# else:
#     os.mkdir('poems')
# with open("poems.txt") as f:
#     f.read()

# with open('poems.txt') as f:
#     # f.read()
#   while 'twinkle' in f:
#     print('twinkle is in')
#     if f == 1:
#       break

# class programmers():
#     worknCom = 'microsoft'
#     def __init__(self,programmer1Name,language, experience):
#         self.programmer1Name = programmer1Name
#         self.language  = language
#         self.experience = experience
#     def __str__(self):
#         return f"programmer's name {self.programmer1Name}\nprogrammer language is {self.language}\nexperience of programmer is {self.experience}\n"
#     def __init__(self,programmer2Name,language2,experience2):
#         self.programmer2Name = programmer2Name
#         self.language2 = language2
#         self.experience2 =  experience2    
#     def __str__(self):
#         return f"programmer's name {self.programmer2Name}\nprogrammer language is {self.language2}\nexperience of programmer is {self.experience2}\n"    
# p = programmers('dj',"python",3)
# p2 = programmers('djop',"java",'none')
# print(p)
# print(p2)
