""""Loops in python
loops are used to repeat instruction
EX : while to send email for 1lp ppl
*for  loops
*while loops"""

#EX  print hello world 5 times
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")

#dis file stored ,raedably etc

#1 while loop
#while condition: here condn is check and exucte  until True
#EX1
#while  True: #this will excute and never becomes fales
    #print("hello")

#EX2
count = 1
while count <= 5:         #1,2,3,4,5,6(FALES) OUT OF THE LOOP
    print("Hello cherry") #H,H,H,H,H
    count += 1            #2,3,4,5,6

print(count) #6
#OP-
#Hello cherry
#Hello cherry
#Hello cherry

""" note 
iterator = with  var(1,j,k) we itratar 
iteration = whn it run in loop ex 1 itration ,2 itraion """

#EX3
i = 1
while i <= 3:
    print("Hello cherry women")
    i += 1

#EX4 print num 5 to 1 rev and 5 to 1
i = 5
while i >= 1:    # 5,4,3,2,1,0(fales)                     #op 5 4 3 2 1
    print(i)     # 5,4,3,2,1
    i-=1         # 4,3,2,1,0

i = 1               #op 1 2 3 4 5
while i <=5:
    print(i)
    i+=1

#practice
#1 print num 1 - 100
i = 1
while i <= 20:
    print(i)   #1234.....20
    i+=1

#2 print the num 20 to 1
j = 20
while j >= 1:
    print(j)  #20,19,19,17...1
    j-=1

#3 print multiplication table of num n #1 X 1 = 1
"""n = int(input("Enter the n num:"))
while n <= 10:
    print(n, "x", n+1 ,"=",)"""
n = int(input("Enter the n num:"))
i=1
while i <= 10:
    print(n*i)
    i += 1

#4 print elements of following list using loop

l = [1,4,9,16,25,36,49,64,81,100]

print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])
print(l[6])
print(l[7])
print(l[8])
#or
"""i=0
while i <= len(l):
    print(l[i])
    i+=1"""
#str
ls = ["sak","yadav","divya","eva","pk","bhu"]
j=0
while j < len(ls):
    print(ls[j])
    j += 1

#5 serach for the num x in this tuple using loop
tup = (1,4,9,16,25,36,49,64,81,36,100)
x = 36
k = 0 #insliz
while k < len(tup):
    if(tup[k]== x):
        print("found",k)
    k+=1

"""Break & continue 
#break = used to terminate the loop whn encountered
#continue = terminates execution in the current iteration & continues execution
of loop with the next itration """""

p =1
while p <= 5:
    print (p)
    if(p==3):
        break # 1.2.3 break
    p+=1

print("end")

q =1            #1
while q <= 5:   #1<=5
    if(q==3):   #1==3  2==3 no  3==3 yes enter if (3 skip)
        q += 1  #3+1 =4
        continue
    print(q) #1,2,4,5
    q += 1

r = 1
while r <= 10:
    if(r%2 != 0):  # != 2,4,6,8,10
        r += 1      # == 1,3,5,7,9
        continue #skip
    print(r)
    r += 1

"""for loop is python are used for sequential traversal (1 by 1)
for traversing list,string,tuples etc
EX  list =[1,2,3]
 for      el       in      list:
 loop    var    keyword          """

list2 =[1,2,3,4,5,5,6,6] #op 1,2,3,4.....
list3 =["apple","orange","mango","cherry"] #apple,orange,mango....
for val in list2:
    print(val)

for val2 in list3:
    print(val2)

#2 for loop with else
st2 ="sakshi"
for el in st2:
    print(el)
else:
    print("end")

"""#print elements of following list using loop
ele = [1,2,3,4,5,6]
x = 5
idx = 0
for i in  ele:
    if(i == x):
        print("num found",idx)
        idx += 1
    else:
        print("num not found")"""

"""  #range()
 range function returns a sequence of num,
*  starting from 0 by default
*  increments ny 1 (by default)
*  stops before a specified number
syntax : range(start?,stop,step?)"""

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])

for i in seq:
    print(i)

for i in range(10):
    print(i)

#range(start?,stop,step?)
for i in range(0,10,2):
    print(i)

#practice using for and range

#1 print num from 1 to 100

for i in range(1,101):  #1,2,3,4,5,6.....100
    print(i)

print("end")
#2 print num from 100 to 1


for j in range(100,1,-1): #100,99,98,97,98....1
    print(j)

#3 print the multiplication table of num n

n = int(input("Enetr the num:"))
for i in range(1,10):
    print(n*i)

#pass statement
#pass is a null statements that does nthg
#it is used as a placeholder for future code
# ex for el in num:
#pass

for i in range(5):
    pass
print("some work")

#practice

#1 find the sum of first n num (using while)
n=5 #1+2+3+4+5=15
sum = 0
for i in range(1, n+1):
    sum += i #1,3,6,10,15

print(sum)

#2 find the factorial n num
n=5 #1*2*3*4*5 =120
fact = 1
for i in range(1, n+1):
    fact *= i

print(fact)