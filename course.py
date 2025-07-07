#operations :
print (3 + 3)
print (3 - 3)
print (3 * 3)
print (3 / 3) #result float

#print(3 + "hello") this gives you an error
print(3 * "hello") #you can multiply an interger with a string the result will be hellohellohello
#variables
print(3) #interger
print(3.0) #float
print ("string") #string
#inputs
input = input('what is your name') #ask the user for an input
print('my name is ' , input) # you can concat variables using ,
#functions
#some util funtions
print('hello'.upper()) #turns hello to HELLO
print('HELLO'.lower()) #turns HELLO to hello
print('hello'.replace('o','abc')) # replace o in hello with abc
print(abs(-1)) #returns the absolute value of -1
print(len("123")) #returns the length of 123
print (max(1,2,3)) #returns the max of 1,2,3
print (min(1,2,3)) #returns the min of 1,2,3
print (type(1)) #returns the type of the variable
print (int ("1")) #returns a string into a number 
print(pow(2, 2))#power funcgtion
print(round(1.4253,2)) # round the value 
#container
_tuple =('hello' , 1 ,('hello', 1)) #tuple cannot change
_list =['hello', 1 , 1] # list can be changed
_list.append('hello again') # append value to the list(we cannot apped a value to a tuple)
_set ={'hello', 1, 2 , 3}#set every entry is unique
set_of_list= set(_list) #returns the list into a set (remove the 1)
print(set_of_list)
_dictionary ={'name':"hello","age":1}#dictionary key value
#how to get values from containers
alphabet_list =['a','b','c','d','e']
alphabet_tuple=('a','b','c','d','e')
print(alphabet_list[0]) #returns a
print (alphabet_list[-1]) #returns e
print (alphabet_list[0:3])#return a,c,d
#if statements 
# if 1>0 :
#     print ('hello1')
# elif 2>0 :
#     print ('hello2')
# else :
#     print ('hii')
#while statements
i = 0
while i <= 2 :
    print (i)
    i += 1
print (i)    
#for statements
test_list = [1,3,365,23]
for x in test_list:
    print(x)
test_dictionary = {'name':'savage','age': 21}
for x in test_dictionary.items():
    print (x)
#functions
def hello_function (hello = 'hello' , times = 1):
    i=0 
    for i in (range(times)):
       print(hello)
    return 0
hello_function('hello',5)
#f-string
print(f'hello i am {20} years old')
#single line if statement
age = 21 if 1 > 0 else 22
print(age)
#list comprehension
list_two = [i * 2 for i in range(0,10)]
listgg= [ f'{i}{j}' for i in ('A','B','C','D','E') for j in range(0,5) if f'{i}{j}' != "C3"]
print (listgg)
print(list_two)
#lambda function
age = lambda age:age*2
#Classes
class MyClass :
    def __init__(self,msg): #constructor of the class
        self.msg=msg
    def __str__(self): #print function
        return(self.msg)    
message=MyClass('hello') #creating an object from MyClass
print(message)
#inheritance
class Animal:
    def __init__(self,age,name):
        self.age=age
        self.name=name
class Dog(Animal):
    def __init__(self,age,name,height):
        super().__init__(age,name) #the dog class get the attributes of the animal class using super method
        self.height=height
#modules
from math import sqrt
print (sqrt(4))