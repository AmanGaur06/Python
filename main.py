#String

first_name = "aman"
last_name = "gaur"

#String concatenation

full_name = first_name + " " + last_name
print("My name is "+full_name)

#Integers

age = 21
print("your age is "+ str(age)) # changing the datatype to show the result with string

#Float

height = 167.6
print("your height is "+ str(height)+" cm") #float representation in python (datatype)

#Boolean

human = False
print(type(human))

#multiple assignments

name,age,human = "aman",21,True
print(name)
print(age)
print(human)

yash = aman = nikhil = chauhan = 30
print(aman)
print(yash)
print(nikhil)
print(chauhan)

# String methods

name = "aman gaur"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.find("r"))
print(name.replace("a","n"))
print(name.count("a"))
print(name.isalpha())
print(name.isdigit())
print(name.count("a",0,5)) #include staring support index and ending support index
print(name*5)

#type Casting
#convert one datatype to another datatype

x = 1 # int
y = 2.0 #float
z = "3" #string

x = str(x)
y = int(y)
z = int(z)

print(str(x))
print(y)
print(type(z))


# User Input

name = input("please enter your name : ")
age = int(input("please enter your age : ")) # typeCasting is used here (int)
height = float(input("please enter your age : "))  # typeCasting is used here (float)
age = age+1
print("welcome " + name.upper())
print("your age is "+ str(age)+ " years old")
print("your height is "+ str(height)+" cm tall.")
print("thanks for visiting here")

# Math module

import math

pi = 3.14
x,y,z = 1,2,3
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(math.sqrt(pi))
print(pow(pi,2))
print(max(x,y,z))
print(min(x,y,z))



#Note: we can either use indexing or slicing for the strings. Both purpose is similar.


#Slicing defination

# creating a substring by extracting elements from another string

#[start:stop:step]

#Indexing Note: In indexing we use (:) semicolon and it is an operator

name = "aman gaur"
first_name = name[0]
first_name = name[0:4]
first_name = name[::-1] #reverse a string
first_name = name[::2]
print(first_name)

#Slicing Note: IN slicing we use commas (,) and it is a function

website = "www.https://google.com"
lets_slice = slice(12,-4)
print(website[lets_slice])

#Conditional statements if, elif , else

age = int(input("Please enter your age : "))
if age==100:
   print("You are a century old!")
elif age>18:
    print("You are an adult!")
else:
    print("You are a minor!")

#SIMPLE CALCULATOR PROGRAMS

number_first = int(input("Enter the first Number : "))
number_second = int(input("Enter the second Number : "))
print("choose the operator : + , - , * , / ")
operator = input("Enter the operator : ")
if operator == "+":
    print(number_first+number_second)
elif operator == "-":
    print(number_first-number_second)
elif operator == "*":
    print(number_first*number_second)
elif operator == "/":
    if number_second >0:
        print(number_first/number_second)
    else:
        print("Please choose number other than zero ")
else:
    print("Thank You")


#Logical operators And, Or , Not (Not operator reverse the result if it is true so it change it to false and
# if it is false then it change it to ture.)

temp = int(input("enter the temperature : "))
if temp >= 0 and temp <= 30:
    print("Temperature is good outside!")
elif temp < 0 or temp > 30 :
    print("Temperature is bad outside!")

# if else practice ( lets have some fun )

# (1) program to check whether a number is even or odd enter by the user.

number = int(input("enter the number here : "))
if number%2 == 0 :
    print(str(number)+ " is even")
else:
    print(str(number)+ " is odd")

# (2) write a program whether a number is divisible by 7 or not

number = int(input("Please enter a number : "))
if number%7 == 0:
    print("This number is divisible by 7 ")
else:
    print("Sorry! please enter some other number")


# write a program to display "Hello" when user enter a number which is multiple of five,
# otherwise print "bye".

num = int(input("please enter a number : "))
if num%5 == 0:
    print("Hello")
else:
    print("Bye")

# (3) write a program to calculate the electricity bill(accept number of unit from user)according to the following criteria
#price first 100 units no charge
#Next 100 units Rs 5 charge per unit
#After 200 units Rs 10 charge per unit
#For example if input unit is 350 than total bill amount is Rs 2000

unit = int(input("Please enter the total number of units : "))
if (unit<= 100):
    print("No charge applied")
elif(unit>100 and unit <=200):
    print("Rs 5 per unit charge after 100 units")
    print((unit-100)*5)
else:
    print("Rs 10 per unit charge after 200 units")
    print((unit-200)*10+(100*5))

#While Loop = a statement that will execute a block of code as long as the condition remain's ture.

name = ""
while len(name)==0:
    name = input("Enter your name : ")
print("Hello "+ name.upper())

#Another way of writing the same code

name = None
while not name:
    name = input("enter your name : ")
print("hello "+ name)

#For Loop : A statement that will execute a block of code a limited amount of times
 while loop = unlimited
 for loop = limited

for i in range(10):
    print(i+1)

for i in "aman gaur": # iterating on each character
    print(i)

for loop for 2 numbers
for i in range(50,100+1,5):
    print(i)


# Happy New Year CountDown with time module
import time
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy New Year!")

# Nested loop : The inner loop finish all its iteration before finishing the outer iteration for the loop.
rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : "))
symbol = input("Enter the symbol : ")
for i in range(rows):
    for j in range(columns):
        print(symbol,end=" ")
    print()

#if else practice
#write a program to accept percentage form user and display the grade according to the following list
# marks grade
# >90   A
# >80 and <=90 B
# >=60 and <=80 C
#below 60 D

percentage = int(input("Enter the percentage : "))
if percentage>90:
    print("Your Grade is 'A' ")
elif percentage>80 and percentage<=90:
    print("Your Grade is 'B' ")
elif percentage>=60 and percentage<=80:
    print("Your Grade is 'C' ")
else:
    print("Your Grade is 'D' ")

#write a program to accept a number form 1 to 7 and display the name of the day like 1 for sunday,2 for tuesday and so on.
num = int(input("Enter the number between 1 to 7 : "))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
elif num ==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("please enter number anywhere between 1 to 7 :) ")

#Last Digit
num = int(input("Enter a number : "))
print(num%10)

#Loop practice
for i in "Myblog":
    print(i)

for i in range(5):
    print(i)

for i in range(10,15):
    print(i)

#program to print first 10 natural numbers
for i in range(10):
    print(i+1)

#write a program to print first 10 even numbers

for i in range(2,22):
    if i%2==0:
        print(i)

#same question with differnt method
for i in range(2,22,2):
    print(i)

#write a program to print fist 10 odd numbers
for i in range(1,20,2):
   print(i)

# Different method for the same question
for i in range(20):
    if (i%2!=0):
        print(i)

#write a program to print first 10 even numbers in reverse order
for i in range(20,0,-2):
   print(i)

#write a prgram to print a table accepted from the user
num = int(input("enter a number : "))
for i in range(1,11):
    print(num*i)


# Loop control statements in python
#Loop control statements = Change a loop execution form its normal sequence
#break    =       used to terminate the loop entirely
#continue =       skips to the next iteration of the loop
#pass     =       does nothing,acts as a placeholder


#example of break
while True:
    name = input("Enter your name : ")
    if name != "":
        break

#continue

phone_number = "123-456-7890"
for i in phone_number:
#    if i == "-":
        continue
    print(i, end="")


#Pass
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)

#LIST = used to store multiple items in a single variable
food = ["hamburger","pizza","pasta","french fries","cake","cookie"]
food.append("muffins")
food.pop()
food.remove("pizza")
food.insert(1,"momos")
food.sort()
food.clear()
for i in food:      #(note: for loop to print all the contents of the list)
   print(i)

# 2D list = a list of list

drink = ["coffee","soda","milkshake"]
dinner = ["hotdog","burger","pizza"]
dessert = ["cake","pudding","ice-cream"]
mainList = [drink,dinner,dessert]
print(mainList[2][2])



#tuples = collections which is ordered and unchangable
# used to group together related data



student = ("aman",21,"male")
print(student.count("aman"))
print(student.index("male"))



#sets = collection which is unordered, unindexed and no duplicates vlaues.

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}
utensils.add("cake")
utensils.remove("cake")
utensils.clear()
utensils.update(dishes)
new = utensils.union(dishes)
print(dishes.difference(utensils)) # it tells about the what is not common between both the sets
print(dishes.intersection(utensils))  #it tells about what is common between both the sets
for i in new:
   print(i)


#Dictionaries = A changable unordered collection of key and value pairs.
# fast because they use hashing,allow us to access a value quickly.



capitals = {'usa':'washington dc','india':'new delhi','china':'beijing','russia':'moscow'}
print(capitals)
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals['india'])
print(capitals.get('germany'))
capitals.update({'germany':'berlin'})# using curly braces while updating the dictionary elements
capitals.update({'usa':'las vegas'})#updating the existing value of a key
for key,value in capitals.items():
   print(key,value)
capitals.pop('china')
capitals.clear()
print(capitals)

#just random things :)
substring= "Hello this is a string"
print(substring[22::-1])



#function = a block of code which executed only when it is called. or Invoking a function



def hello():# here we pass parameters
   print("Hello This Is My First Function")

hello() #here we pass arguments


def hello(name): #parameters
   print("My name is "+name)
hello("aman gaur") #arguments


#Note : The parameters ans Arguments should match in numbers

def hello(first_name,Last_name): #multiple parameters
   print("Hello my name is "+first_name+" "+Last_name)

hello("aman","gaur") #multiple arguments

def hello(firstName,lastName,age):
   print("Hello my name is "+firstName+" "+lastName)
   print("I am "+str(age)+" year's old")
hello("aman","gaur",21) #passing interger with string

#Return statements = function send python values/objects back to the caller
#these values/objects are known as function return vlaue.

def multiply(num1,num2):
   result = num1*num2
   return result
print(multiply(6,8))

#another method in less line of code

def multiply(num1,num2):
   return num1*num2
x = multiply(6,8) #stored the caller into a variable
print(x) #print the variable in which value is stored

# Keyword Arguments = arguments preceded by an identifier when we pass them to a function
#The order of the arguments doesn't matter, unlike positional arguments
#Python knows the game of the arguments that our funtion receives.

def hello(first,middle,last):
   print("hello "+first+" "+middle+" "+last)

hello("code","bro","dude") # position of the arguments should match


# Matching position
def name(first,middle,last):
   print("Hello "+first+" "+middle+" "+last)
name(first="bro",middle="code",last="dude")

#Nested function calls = function calls inside other function calls
#innermost function calls are resolved first
#returned vlaue is used as arguments for the next outer function

num = input("enter a number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

#same thing but within 1 line of code and this is called nested functions
num = print(round(abs(float(input("enter a whole number : ")))))


#Variable Scope = the region that a variable is recognized
# A variable is only available from inside the region it is created.
# A global and locally scoped versions of a variable can be created.

# no global variable is defined here
def display_name():
   name = "aman" #local variable can only be access within the function body block of code
   print(name)

print(name)

name = "aman" # global variable is defined in this region
def display_name():
   name = "aman_gaur" # Local variable is also defined in this region
   print(name)
print(name)#it print global variable
display_name()  #it print local variable within the function body block of code

#if local variable is not available then it will access global variable
# global variable (available inside and outside functons)


# *args = parameters that will pack all arguments in tuple
# useful so that function can accept varying amount of arguments

def add(*args):
   sum = 0
   for i in args:
       sum += i
   return sum
print(add(1,2,3,4,5,6))

#tuple are orderd and immutable

def add(*stuff):
   sum = 0
   stuff = list(stuff) # we change the tuple into list so that we can change the item in it
   stuff[0] = 0 # we set the 0th index value to 0 instead of having 1 passed as an argument
   for i in stuff:
       sum += i
   return sum
print(add(1,2,3,4,5,6))


# Kwargs = Keyword arguments / parameter that will pack all the arguments into a dictinary
# useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
   print("hello "+ kwargs['first']+" "+kwargs['last'])
hello(first="aman",last="gaur")

#or
def hello(**kwargs):
   print("hello",end=" ")
   for key,value in kwargs.items():
       print(value,end=" ")
hello(title = "Mr.",first = "aman",last = "gaur")


#String format

#STR.format() = optional method that gives users
#more control when displaying output
animal = "cow"
item = "moon"
print("The {} jumped over the {}".format(animal,item))
# Here we use {} as a placeholder to fill the animal and item variable but we can directly write the string or the indexing vlaue of the variable in the placeholder
# like mentioned below
print("The {0} jumped over the {1}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item)) # positional arguments
print("The {animal} jumped over the {item}".format(animal ="cow",item ="moon"))
# keyword Arguments we can use the value within the format method multiple times
 # another method but in a clean way

text = "The {} jumped over the {}"
print(text.format("cow","moon")) # we can use the variable also instead of direct string values

#padding with string format
name = "aman"
text = "Hello my name is {:10}".format(name)
text = "Hello my name is {:>10} and i am 21 year's old".format(name)
text = "Hello my name is {:>10} and i am 21 year's old".format(name)
text = "Hello my name is {:^10} and i am 21 year's old".format(name)
print(text)
print("Hello my name is aman")

# Number formating

pi = 3.1415926
print("The value of {:.2f} is : ".format(pi))
print("The value of {:.3f} is : ".format(pi)) # here it also round the number and f is for floating point number


#Random Module
import random # random module import
x = random.randint(1,6) # randomly provides a number between a range given in parameters

import random
y = random.random() #provides a random floating number between 0 and 1
print(y)

myList = ['rock','paper','scissors']
z = random.choice(myList)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"a","b","c","d","e"]
random.shuffle(cards) # not stored in a variable it wont work
print(cards)

#Most Important
# Exception handling = events detected during executions that interrupt the flow of a program

# creating a two number program
try:
   num1 = int(input("enter a number : "))
   num2 = int(input("enter a number : "))
   result = num1/num2
except ZeroDivisionError as e: # if zero is provided in the input
   print(e)
   print("you can't divide by zero.")
except ValueError as e: # if instead of numbers any other value is provided in the input
   print(e)
   print("Please enter a number here.")
except Exception: # single exception is not good to handle all the exception occurs in the program
   print("something went wrong :(")
else: # if no exception occus then only we print the result
   print(result)
finally: # This finally block will execute no matter any exceptions occurs or not
   print("Thanks for using our services :)")

# File detection in python
# for this we need to import os module
import os
path = "C:\\Users\\agaur\\OneDrive\\Desktop\\abc"
if os.path.exists(path):
   print("This thing exists")
   if os.path.isfile(path):
       print("This is a file")
   elif os.path.isdir(path):
       print("This is a directory")
else:
   print("This thing not exists")

# Read A file in python
#how to read or open a file in python


try:
   with open('C:\\Users\\agaur\\OneDrive\\Desktop\\test.txt') as file: # with open helps in opening the file and then also automatically close it but in this case an exception will occurs if file is not present
        that's why we use try and except block to handle the exception
       print(file.read())
except FileNotFoundError:
   print("There is no such file available")

# How to 'write' or 'append' into a file
text = "\nThis will append in the existing document."
with open('C:\\Users\\agaur\\OneDrive\\Desktop\\test.txt','w') as file:
   file.write(text)

# Append in the file

with open('C:\\Users\\agaur\\OneDrive\\Desktop\\test.txt','a') as file:
    file.write(text)
text = "this is a new text"
with open('C:\\Users\\agaur\\OneDrive\\Desktop\\test.txt','a') as file:
    file.write(text)
    file.close()
with open('C:\\Users\\agaur\\OneDrive\\Desktop\\test.txt','r') as file:
    print(file.read())

# copy a file in python

# copyfile() = copies contents of a file
#copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (file's creation and modification times)

import shutil
shutil.copyfile('C:\\Users\\agaur\\OneDrive\\Desktop\\test.txt','C:\\Users\\agaur\\OneDrive\\Desktop\\copy.txt') # in arguments we just need 2 of them a (source and destination)

import os
path = 'C:\\Users\\agaur\\OneDrive\\Desktop\\copy.txt'
if os.path.exists(path):
    print("this file exists") # result this file exists
else:
    print("this file doesn't exists")


#Move a file in python

import os
source = 'text.txt' # created one variable for source
destination = 'C:\\Users\\agaur\\OneDrive\\Desktop\\text.txt' # created another variable for the destination variable
try:
   if os.path.exists(destination): # checking if already file available at the destination
       print("file is already there")
   else:
       os.replace(source,destination) # if not then the source file will be moved to the set destination path
       print(source + " was moved")
except FileNotFoundError:
   print(source+" was not found")

 # Deleting a file in python
import os
import shutil
path = 'newFolder'
try:
   os.remove(path) # to delete a file
   os.rmdir(path) # to delete an empty directory/folder
    shutil.rmtree(path) # to delete a directory having files in it. (use it with cautious)

except FileNotFoundError:
   print("file not found")
except PermissionError:
   print("you do not have permission to delete that file")
except OSError:
   print("you cannot delete that using that function")
else:
   print(path +" file deleted successfully")

#Modules in python = A file containing python code or functions or classes.
# used with modular programming which is to separate program into parts


# from message import *
#import message as msg # import another module and access it in main module
#msg.hello() # we can import the code from different python file/modules like here we call hello and bye function
#msg.bye() # we can also write this for our convenience


# A simple rock,paper and scissors game
import random
while True:

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Choose form rock,paper or scissors : ").lower()
    if player == computer:
        print("computer : ", computer)
        print("player : ", player)
        print("Tie!")
    elif player == 'rock':
        if computer == 'paper':
            print("computer : ", computer)
            print("player : ", player)
            print("you lose!")
        if computer == 'scissors':
            print("computer : ", computer)
            print("player : ", player)
            print("you win!")
    elif player == 'paper':
        if computer == 'scissors':
            print("computer : ", computer)
            print("player : ", player)
            print("you lose!")
        if computer == 'rock':
            print("computer : ", computer)
            print("player : ", player)
            print("you win!")
    elif player == 'scissors':
        if computer == 'rock':
            print("computer : ", computer)
            print("player : ", player)
            print("you lose!")
        if computer == 'paper':
            print("computer : ", computer)
            print("player : ", player)
            print("you win!")
    play_again = input("Do you want to play again 'Yes' or 'No' : ").lower()
    if play_again != "yes":
        break
print("Bye!")