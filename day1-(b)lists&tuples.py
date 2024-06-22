"""  1 string : var ="str'  #index,slicing,nagative ,fun
     2 list :        marks =[]  #[99,98,79,82,87,92,74,93]
     3 tuples:       tup =()
     4 dictionary :  dic = {key:value}
     5 set:          set ={1,2,3,4}
     string & tuples , set are immutable /list & dic are mutable(changeable)"""

#1 list is a Built-in data type that stores set of values
# it can store elements of diffrent types(int,float,str etc)

marks =[99,98,79,82,87,92,74,93]
print(marks) #[99,98,79,82,87,92,74,93]
print(type(marks)) #<class 'list'>
print(marks[0]) #99
print(len(marks)) #8
print(marks[3]) # indexing  help as only access char not replace
print(marks[3:6]) # slicing used to accessing parts
print(marks[-3:-1]) # nagavtive index  [92, 74]

#1 a List methods
list =[ 1,2,7,4,5,3]
list2 =['a','n','s','b','c','d','h']

list.append(6) #none {adds one element at the end
print(list) #[1, 2, 7, 4, 5, 3, 6]

list.sort()#sorts in ascending  (small to big)order
list2.sort()

print(list) #[1, 2, 3, 4, 5, 6, 7]
print(list2) # ['a', 'b', 'c', 'd', 'h', 'n', 's']

list.sort(reverse=True) #sorts in descending  (big to small)order
print(list) #[7, 6, 5, 4, 3, 2, 1]

list2.reverse() #reverses the list
print(list2) #['s', 'n', 'h', 'd', 'c', 'b', 'a']

#insert method
#syntax list.insert(index,element) used to insert element at index
list3 =[2,3,8]
print(list3) #[2, 3, 8]
list3.insert(2,1)
print(list3) #[2, 3, 1, 8]

#remove method
#removes first occurrenec of element
list3.remove(1) #[2, 3, 1, 8]
print(list3)

#pop method
#removes element at index
list.pop(2) #[2, 3, 8]

"""# 2 Tuples 
A built-in type that lets us create immutable sequence of values"""

tup =(2,3,4,6)
tup1 =(1) #python will take that 1 as int

print(type(tup)) #<class 'tuple'>
print(tup[0]) #2
print(type(tup1)) #<class 'int'>
print(tup[1:3])# slicing (3, 4)

#a tuple Methods

tup2 =(2,3,4,5,4,3,3,5,6)
     # 0 1 2 3 4 5 6 7 8
print(tup2.index(5)) #returns index of first occurrence #op= 3
print(tup2.count(3))#counts total occurrences #op= 3

#practice
#1 ask the user to enter names of there 3 fav movies ans stroe them in list
""""
l = []

movies1 = input("Enter your favorite movie name: ")
movies2 = input("Enter your favorite movie name: ")
movies3 = input("Enter your favorite movie name: ")

# Check if all inputs are provided (you may want to enhance this check)
if movies1 and movies2 and movies3:
    l.append(movies1)
    l.append(movies2)
    l.append(movies3)
else:
    print("Please enter all movie names.")

print("Your favorite movies are:", l)

#or
m =[]
mov = input("Enter your favorite movie name: ")
#or 
m.append(input("Enter your favorite movie name: "))
m.append(mov)
mov = input("Enter your favorite movie name: ")
m.append(mov)
mov = input("Enter your favorite movie name: ")
m.append(mov)
print("fav movies are",m)"""

#2 cheak if list contains palindrome(same num of order from last) of elements

"""l7=[1,2,3,2,1]
l8 = l7.reversed()
print(l7)
print(l8)

if (l7 == l8):
    print("it is palindrome")
else:
    print("not a palindrome")"""

list1 = ['m','a','m'] #list

copy_list1 = list1.copy() #create copy of listands store it in var
copy_list1.reverse()      #reverse that var


if(copy_list1 == list1): #cheak if reverse var is == to lsit1
    print("palindrome")
else:
    print("not palindrome")

#3 to count num od student with A grade in tupple
tup3 =('A','B','C','A','A','A')
print(tup3.count('A'))

#store the baove values in list & sort from A-D
list4 =['A','B','C','A','A','A']

list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)

# Example list
my_list = [1, 2, 3, 4, 5]

# Convert list to tuple
my_tuple = tuple(my_list)

# Print the original list and the converted tuple
print("Original list:", my_list) #Original list: [1, 2, 3, 4, 5]
print("Converted tuple:", my_tuple) #Converted tuple: (1, 2, 3, 4, 5)

