"""File I/O python
python can be used to perform operation on a file (read and write)
Type of all files
1. text files: .txt, .docx, .log etc .(stored in char form)
2. binary files: .mp4, .mov ,.png , .jpeg etc.(0,1)

# 1 & 2 are at the end bytes
#ROM{random access memory}= fast excution, valatile(data will be deleted) OR files can be used.

#open , read ,close file
we we have to open the file before read and write
EX:
    #function
f = open("file.name",mode)
         #sample.txt #r: read mode
         #demo.docx  #w: write mode
"""
#read method

f = open("para.txt","r")

data = f.read() #reads entire file
data1 = f.read(2) #reads word by word
data2 = f.readline(2) #reads one line at a time

print(data)
print(data1)
print(data2)


# write method

f = open("para.txt","w")
h = open("para.txt","a")

data = f.write("then i will move to html css javascript")

f.close()
h.close()

#opration
f = open("para.txt","r+")
#r+ reading and writing     note pointer at start - no truncate
#w+  writhing and reading   note - truncate
#a+  open the file          note pointer placed at end

""""
#character          meaning
'r'          open for reading (default)
'w'          open for writing, truncating the file first
'x'          create a new file and open it for writing
'a'          open for writing, appending to the end of the file if it exists
'b'          binary mode
't'          text mode (default)
'+'          open a disk file for updating (reading and writing)"""


#with syntax
                      #giving diff name
with open("para.txt","r") as j:
    data= j.read()
    print(j)

with open("para.txt","w") as j:
    j.read("new data")

"""deleting a file method
using os module 
module (like  a code library) is a filr written by another programmer that generally has a 
function we can use ."""

#EX
import os

#os.remove("para.txt")



