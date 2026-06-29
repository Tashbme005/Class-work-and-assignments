#when we have 2 words do not leave a space rather may one word uppeer case or put an underscore in between
#this is static since its user defined
def myname():
    print("My name is Shatrah")

myname()

#this is dynamic because the values can be changed
def mynamev2(name):
    print("My name is",name)

mynamev2("Mark")
mynamev2("Ozzy")

def mynamev3(name, age):
    #this is direct referencing
    print("My name and age are:",name, age) 
    #we have used an 'f' formater
    print(f"My name is:{name},and my age is:{age}")

#17 is not in quotes because it an interger/number.
mynamev3("Shatrah", 17)

#the parameter should also be matching the argument list. 
#This means that every time we call a function it should have 2 arguments.
#A funtion was meant to work with others however its conservative in nature eg one solution can require a group of functionalities

#we are using the return to connect these function together
def grosspay(pay):
    #the return statement allows a function to share a value outside of it
    #it also marks the end of execution of a function
    return pay
    
def tax(rate):
    return rate

def cal():
    tax_amount = grosspay(700000) * tax(0.3)
    return tax_amount

def netpay():
    print(grosspay(700000) - cal())

netpay()


