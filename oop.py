#Programming paradigm
#this is a way of/frameworks/arrangements of writing instructions
#i.e functional/structural, event driven, and oop etc.
'''
Functional/structural is a way of writing computer instructions
based on functions and the flow of statements
more suitable for mathematical problems
'''
'''
Event driven is a way of writing computer instruction that 
will be based on the actions of the user
'''
'''
oop(object oriented programming) 
this is a way of writing instructions basing on real world things
here we write software for computational problems 
for real world things(data)
e.g money,tress,car,motorcycles,clothes
these things are called objects 
but all objects are got from a single class (the first of everything makes a class)
classes of objects are identified by a phrase "is a"
'''
#a class is a blue print of an object
#a blue print is an original copy/ carbon copy of something
#classes in programming are identified in singular 
#an object is an instance of a class
#classes provide attributes/features/properties/characteristics
#the values to the property create an object

#a class is also an example of a block of code
#class name must start with an upper case as the first letter
class Woman():
    #these are the properties for Woman class
    name = "Joy"
    #age isn't quoted because is a number/integer
    age = 18
    location = "Munyonyo"
    skin_color = "Brown skin girl"

#we are creating a new object for class Woman 
Woman.name = "Denise"
Woman.age = 19
Woman.location = "Gayaza"
Woman.skin_colour = "Dark skinned"

#classes are identified in singular
class Student():
    name = "Rodney"
    programe = "CSE Python"
    school = "Refactory"
    age = 19

'''
we have 2 categories of classes namely;
user defined and inbuilt classes
and we have corresponding types namely;
static and dynamic classes 
'''
#here we are accessing the Woman attributes
print(Woman.name)
print(Woman.location)

class Employee():
    name = "Valary"
    role = "CEO"
    staff_id = "0006473538483547"

class Food():
    name = "Salad"
    ingredients = "chicken, lettuce, tomatoes, olive oil, pieces of toast"
    amount = "one huge circular bowl"

class Cloth():
    name = "jeans"
    type = "wide leg jeans"
    colour = "blue"
    material = "denim"

class Fruit():
    name = "banana"
    colour = "yellow"
    amount = "one bunch"

class Laptop():
    name = "macbook"
    model = ""

#methods
'''
methods of a class refers to the things an object 
of a class does to itself or others
'''
# a behaviour refers to how an object does something to itself or others
#a function in a class is what we call a method
#an an individual statement in a fuction is what we call behaviours in a method


