"""Function and Recursion
block of statements that preform a specific task
EX:
def func_name(para 1,para 2)": #function definition 
    some work 
    return val
    
func_name(arg1,arg2...)"""#function call
def sum1(a,b):
    sum =a+b
    print(sum)
    return sum
sum1(10,10)

def sum2(a,b):
    sum =a+b
    print(sum)
sum2(10,10)

#function definition
def cal(a,b):  #fparamrters
    return a + b
sum = cal(10,33)#arguments
print(sum)

def word():
    print("hey")

word()
word()
word()
word()


def avg(a,b,c):
    sum = a+b+c/3
    print(sum)

avg(10,10,10)

#Built-in function
print()
len()
type()
range()

#practice
#1 print len of list

list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]


def l(lst):
    a =len(list)
    print(a)

l(list1)
l(list2)

name = ["sakshi","raj","sai"]
s_name =["yadav","yadav","yadav"]

print(name[0],end="")
print(name[1],end="")
print(name[2],end="")

def print_len(list):
    for item in list:
        print(item,end="")
        print("hehe")

print_len(name)
print_len(s_name)


#cal_fact
def fact(n):
    fact1= 1
    for i in range(1,n+1):#range() function, the ending value is exclusive,
        fact1 *= i
    return fact1

f= fact(10)
print(f)


def converter(usd_val):
    inr_val =usd_val*83
    print(usd_val,"USD=",inr_val,"INR")

converter(6)


def num(a=9):
    if (a%2==0):
        print("EVEN str")
    else:
        print("ODD str")
    return a

num()


#recursion
#when a function calls itself repeatdly

#ex
def show(n):
    if(n==0):#base case
        return
    print(n)
    show(n-1)
    print("end")

show(3)

#call stack is used in recusion
#call(function call) stack (one upon other)
#whn we call one function on other

#fact! of n
def play(n):
    if(n == 1 or n == 1):
        return 1
    return play(n-1)*n
a =play(4)
print(a)

#cal the sum of first n num

def cal(n):
    if(n==0):
        return 0
    return cal(n-1)+n


"""
cal(3) calls cal(2) + 3.
cal(2) calls cal(1) + 2.
cal(1) calls cal(0) + 1.
cal(0) returns 0 (base case).

cal(0) returns 0.
cal(1) + 1 = 0 + 1 = 1.
cal(2) + 2 = 1 + 2 = 3.
cal(3) + 3 = 3 + 3 = 6

sum = cal(3)
print(sum)
"""
#recursive function to print all elements in list
def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx + 1)

list4 = [1, 2, 3, 4, 5, 6]

print_list(list4)





