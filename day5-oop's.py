"""OOP in python
To map with real world scenarios, we started using objects in code.
This is called object oriented programming
Procedral - seq code
function  - redundancy < , reusablity >
oop       - we can also: redundancy < , reusablity >

class  :1st we create class [ class is bluePrint for creathing objects ]
object :"""

#creating class
class Student:
    name = "Sakshi"

s1 = Student()
print(s1)   #op - <__main__.Student object at 0x0000014C58275850>
print(s1.name) #Sakshi

s2 = Student()
print(s2.name) #Sakshi

class Car:
    color = "pink"
    brand = "BMW"

c1 = Car()
print(c1.color)
print(c1.brand)

"""
__init__ Function
constructor  is called in every new obj
All class have a function called __init__(),which is always executed 
when the object is being initiated"""

class Student2:
    college_name ="jain" #when we know the value is comman , class attr
    name = "anonymous" #class attr , when we have same name then obj attr is printed
    #default  constructor
    def __init__(self):
        pass
    #parameterzied constructor
    def __init__(self,name,marks):  #we have to pass the self arrg
        print("Adding new student database")
        self.name = name
        self.marks = marks


#s3 = Student2() #<__main__.Student object at 0x000001C7E1C8B7A0>
#print(s3) #<__main__.Student object at 0x000001C7E1C8B7A0>
s3 = Student2("sakshi",89) #data is called attibutes
print(s3.name,s3.marks)

s4 = Student2("Nida",89)
print(s4.name,s4.marks)

print(s4.college_name) #jain
print(Student2.college_name) #jain

"""
Methods
class is colletion of data(attr) and methods
Method are function that belongs to objects"""

#ex for method
class Student3:
    college1_name ="jain"

    #parameterzied constructor
    def __init__(self,name1,marks1):  #we have to pass the self arrg        self.name1 = name1
        self.name1 = name1
        self.marks1 = marks1

    def wlcm(self):
        print("wlcm student",self.name1)

    def get_marks(self):
        return self.marks1


s7 = Student3("sak",99)
print(s7.name1,s7.marks1)
s7.wlcm()  #calling the method
print(Student3.get_marks1())

#crete student class that takes name and marks of 3 sub as aruguments
#in constructor then create a mentod to print the average



class Std:
    def __init__(self,name9,marks7):
        self.name9 = name9
        self.marks7 = marks7

    def avg(self):
        sum = 0
        for val in self.marks7:
            sum += val
        print("hi",self.name9,sum/3)

s5 =Std("sakshi",[99,98,97])
s5.avg() #hi sakshi 98.0

s5.name2 ="Sak"
s5.avg() #hi Sak 98.0


"""
Static Methods
methods that dont use the self parameter(work at class level)
@staticmethod -> convert a function to be static methods 
*when to use > This is comman for all class(obj)
             > whn there is no use of class attr or instances attr 
             EX: 
             @staticmethod 
             def start():
                    print("str")
"""

class Hello:
    @staticmethod #decorator
    def hello():
        print("hello")


s0 =Hello()
s0.hello()
