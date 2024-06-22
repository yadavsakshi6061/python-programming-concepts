#day2
""" Dictionary in python
dic are used to store data values in key:values pairs
they are unordered,Converted tuple: (1, 2, 3, 4, 5)
mutable(changeable),
don't allow duplicate keys """

#EX       #key  : value
dict ={ "name":"sakshi","SGPA":9.33,"marks":[22,22,33]}
print(dict)

#1 dic
info ={
    "key":"values",   #key can be(string,int,float,bool,tuple etc)
    "name":"sakshi",
    "leaning":"coding",
    "age":22,
    "is_adult":True,
     "marks":9.33,
     "sub":['c','java','python'],
     22:33
}
print(info)
print(type(info)) #<class 'dict'>

#access values by keys
print(info["key"]) #values
print(info["sub"]) #['c', 'java', 'python']

#to asign new values
info["name"] ="sakshi yadav"
print(info)

#we can add key,value pair
info["ph:num"] =889326987
print(info) #...'ph:num': 889326987}

#we can also craete empty dic
null_dic ={}
print(null_dic) #{}

#2 Nested DIC we can make the value of key as dic  itself

student ={
    "name":"sakshi",
    "subject":{
        "python":98,
        "html":97,
    "css":77
    }
}

print(student)
#{'name': 'sakshi', 'subject': {'python': 98, 'html': 97, 'css': 77}}
print(student["subject"])
#{'python': 98, 'html': 97, 'css': 77}
print(student["subject"]["python"]) #98


#3 Dic methods
goals  = {"python":"coding",
          "html":"structural",
          "css":"presentational",
          "javascript":"functional",
          "framework":{
                       "django":"python",
              "Flask":"python"}
          }

print(len(goals)) #5

#mydic.keys() returns all key
print(list(goals.keys()))
#op - dict_keys(['python', 'html', 'css', 'javascript', 'framework'])

#mydic.values() returns all values
print(goals.values())
#op - dict_values(['coding', 'structural', 'presentational', 'functional', {'djan..

#mydic.items() returns all(key,val)pairs as tuples
print(goals.items())
#op - dict_items([('python', 'coding'), ('html', 'structural'), ('

#mydic.get("key") returns the key according to values
print(goals.get("framework"))
#op - {'django': 'python', 'Flask': 'python'}

#mydic.update(newDict) insert the specified items to the dic
goals.update({"API":"protocol"})
print(goals)
#....'API': 'protocol'}

#print(goals["java"]) #error
print(goals.get("java")) #none

"""Set in python
set is the collection of the unordered items 
each element in the set muct be unique 
& set is immutable but set {elements are mutable}"""

collections ={1,2,3,4,"sakshi","yadav",4,4,4}

print(collections) #{1, 2, 3, 4, 'yadav', 'sakshi'} no duplictn values
print(type(collections)) #<class 'set'>
print(len(collections)) #6

# 1 empty set
collections1 = set()
print(type(collections1)) #<class 'set'>

collections2 = {}
print(type(collections2)) #<class 'dict'>

#2 set methods
# note: set is mutable but the elements are immutable

#add
collections1.add(2) #adds the elemnet
collections1.add(4)
collections1.add("sakshi")
print(collections1) #{'sakshi', 2, 4}

#remove
collections1.remove(2) #removes the element
print(collections1) #{'sakshi', 2, 4}

"""hashable means immutable(not changeable"""
#clear
collections1.clear()
print(collections1) #set()

#pop
collections3 ={"sakshi","yadav","raju","hasband surename"}
print(collections3) #{'sakshi', 'hasband surename', 'raju', 'yadav'}

print(collections3.pop()) #removes a random value
#yadav #any values can be pop

#union - combines both set values & returns new
"""set1= 1,2,3,4
   set2=1,5,3,5
   union = 1,2,3,4,5"""

set1 = {1,2,3,4,5}
set2 = {2,6,3,2,1}

print(set1.union(set2)) #{1, 2, 3, 4, 5, 6}

#intersection -  combines common values & returns new

"""set1= 1,2,3,4
   set2=1,5,3,5
   intersection = 1,3 """

set1 = {1,2,3,4,5}
set2 = {2,6,3,2,1}

print(set1.intersection(set2)) #{1, 2, 3}

#practice
# 1 store following words
dic1 = {'cat':"a small animal","table":["a piece","lists of facts"]}
print(dic1)
#op - {'cat': 'a small animal', 'table': ['a piece', 'lists of facts']}

#2  given list of subj for student,
set3 = {"python","java","C++","python","javascript","java","python","C++"}
print(set3)
print(str(len(set3)) + "classroom are needed by all students")
#op - 4classroom are needed by all students

#3 enter 3 sub from user and store in dict
dict1 ={}

sub1 = input("enter sub1")
sub2 = input("enter sub2")
sub3 = input("enter sub3")

dict1.update({"sub1":sub1})
dict1.update({"sub2":sub2})
dict1.update({"sub3":sub3})

#or
"""if (sub1 and sub2 and sub3):
    dict1.update({"sub1":sub1})
    dict1.update({"sub2":sub2})
    dict1.update({"sub3":sub3})
else:
    print("enter the subs")"""

print(dict1) #op - {'sub1': '1', 'sub2': '1', 'sub3': '1'}

#4 store 9 and 9.0 as seprate values
#i way
set3 ={9,"9.0"}
print(set3) # op -{'9.0', 9}

#way
set4 = {("foat",9.0),("int",9)}
print(set4) # op -{('foat', 9.0), ('int', 9)}
