# 1 str1
str1 = 'sakshi'
str2 = "raju"     #ex Str2 = 'my bag's are styleish'  """error"""
                  # Str2 = "my bag's are styleish"
str3 = '''yadav'''

print(str1)

#2 escape  seq char (tab,nextline etc )
str3 = " my name is sak, whts is ur name?"
print(str3)
#ex \n = next line
str4 = " my name is sak \n whts is ur name?"
print(str4)

#ex \t = tab space
str5 = " my name is sak \t whts is ur name?"
print(str5)

#3 string operation
#a concatenation ex = "sak"+"shi  = "sakshi"
str6 ="sak"
str7 ="shi"
final_str = str6 + " " + str7
print(final_str) #sakshi

#b lenght of str funtion(in built)
#len(str)
len1 = "sakshi"
print(len(len1)) #6

#4 Indexing
""" SAKSHI_hii
    0123456789 position  str[0]=#S , str[1] =#1 ....
    index help as only access char not replace"""
name = "sakshi raju yadav"
ch = name[1] #a
print(ch)
print(name[7]) #7

#5 Slicing
"""Slicing is used to accessing parts of string
ex = str[starting_idx:ending_idx] #ending idx is not included """

str = "sakshi"
      #012345
print(str[0:len(str)]) #sakshi
print(str[0:]) #sakshi
print(str[:4]) #saks
print(str[0:3]) #sak

#a negavtive index ex:-1
str9 = "sakshi"
       #-6-5-4-3-2
print(str[-5:]) #akshi

#7 string Functions
days ="mon Tues wendes thus Fri satur"
print(days.endswith("day")) #Fales= returns true is str ends with substr
print(days.capitalize())  #Mon tues wendes thus fri satur
                        #capitalizes 1st char
print(days.replace('monday','sunday')) #mon Tues wendes thus Fri satur
print(days.find('mon')) #return 1st index od 1st occurrence
print(days.count("u")) #count the occurrence of substr in string

#practice
#1 input user name and print len
name = input("Enter your name:")
print(len(name)) #sakshi = 6

#2 find the occurrenace of 'S' in 'string'
str6= "sakshi"
print(str6.count('s')) #2

#8 conditionsl statment
"""diff bwt if and elif is the elif will cheak its con only if (if)state is fales 

#1 s = 8
if (s>4):
    print("s is greatter")
else:
    print("s is smaller")

#2 light =input("Enter light color")
if(light == "Red"):
    print("stop")
elif(light == "yellow"):
    print("Ready")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

#3 90 to 100 =A,80 to 89 =B,70 to 79 =C
marks =int(input("enter sub marks to know your Grad"))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")"""

#b nesting
#ex
age = 95
if(age >= 18):
    if(age >= 70):
        print("can not1 drive")
    else:
        print("can drive")
else:
    print("can not2 drive")

#practice
#1
num3=int(input("Enter you num"))

if (num3 % 2 == 0):
    print("even num")
else:
    print("odd num")

#2 find bigest num
a = int(input("enter 1st num"))
b = int(input("enter 2nd num"))
c = int(input("enter 3rd num"))

if(a > b and a > c):
    print("a is greatest")
elif(b>c):
    print("b is greatest")
else:
    print("c is greatest")

#3
num7 =int(input("enter ur nam"))

if (7 % num7 == 0):
    print("is multiple of 7")
else:
    print("is not multiple of 7")
