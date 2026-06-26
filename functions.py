#PEMDAM
#function/routine is a named block of code that performs a specific task(one thing)
#A function is a named group of statements that performs a specific task
#consider a for loop put in something with an identification
#example
#stuff
#A function is defined/declared (created) by a keyword called def followed by a valid name of a function(variable syntax)
#A function is self contained(This mean variables within a function cannot be accessed outside that given function by default)
#def is a keyword specifying creation of a function. def is short for define since a function is defined
#the function is not automaticallly considered but ignored until its called(We call a function by its name using parenthesis)
def stuff ():
    num1, num2 = 10, 20
    #when accessing values do not use quotes since it'll be displayed the way it is and not the values
    print(num1 + num2)
#these are independent statements with no identity
#num1, num2 = 100, 200
#print(num1 + num2)
#this a function call. This makes the function above to be executed in the terminal
#technically this is called to invoke a function (also know as calling a function)
stuff ()

def add ():
    number1, number2 = 15, 30
    print(number1 + number2)
add ()
 
#functions with other arithmetic operators
def multiply ():
    num1, num2 = 2,50
    print(num1 * num2)
multiply ()

def modulus ():
    num1, num2 = 200,50
    print(num1 % num2)
modulus ()

def division ():
    num1, num2 = 100,50
    print(num1 / num2)
division ()

def power ():
    num1, num2 = 3,3
    print(num1 ** num2)
power ()

#when you create a function, the computer creates a big chunck of memory that can expand based on the items in this function
#a function is a unit of memory thats big enough to store more units of memory. It also similar to a folder
#categories of funtions. in python we have 2 categories of function that is;
#1. user defined functions(functions like the ones above created individually and call them)
#2. inbuilt functions/ predefined functions (these function come already with python, with no knowledge od how they were defined ,but we can call them)
#this is an inbuilt functions and so are all the predefined function we've been using earlier.
#all variable with parenthesis are inbuilt functions
#print() isn't static 
#append () and pop() are static functions
#we have 2 typs of functions amongst the 2 categories
# static functions these are functions with hard coded valuse which always give the same exact values whenever we call them. all our examples above are statice values.
#this is for user defined functions 
# dynamic functions are functions that always give different results whenever its called upon.

#the parameters(US)/ formal parameters(UK) are what we put inside of the parenthesis. they have to 2 or more to be a dynamic function
def addition (num1, num2):
    print(num1 + num2)
#these values used when calling a dynamic function are called arguments(US)/ actual parameters(UK)
addition(12, 13)
addition(20, 40) 

def subtraction (num1, num2):
    print(num1 - num2)
subtraction(8, 6)
subtraction(100, 70)

def multiplication (num1, num2):
    print(num1 * num2)
multiplication(16, 5)
multiplication(300, 4)

def division (num1, num2):
    print(num1 / num2)
division(8, 4)
division(100, 25)

def exponential (num1, num2):
    print(num1 ** num2)
exponential(2, 6)
exponential(3, 8)
 
def modulus (num1, num2):
    print(num1 % num2)
modulus(64, 6)
modulus(29, 7)

#function that accepts input
def 
