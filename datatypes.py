#differnt data type in python(differant groupings or categories of data or unit of mmemeory that carry the same memory size of data)
#data types are the classicification of data items.
#1.numeric data type
#all numbers from 0 to infinity sre integers. Any number with a decimal is a float. 
num1=4
num4=16
#2.string data type
#All value in single or double quotations are known as strings.
#all alphabetical words or letters are in this data type
name="Shatrah"
stuff='12'#this is not 12 but rather 1 and 2 since its in a string.
num3=12#not a string
num2=0.8#not a string
#3.sequece data type
#a group of value located in one memory variable.
lang=["python","java", "c++", "javascript",12,20,12.5,[1,2,3]]
#In python,one or more values in square brackets is called a list since its in one memory unit.
#a list can have more than one data type. it can also have sub list within it
#mapping data type
#boolean data types
#set data types
empty = []

fruits = ["apples","jackfruit","pineapple", "watermelon", "dragonfruit"]
#these are a pair of parenthesis
#if you have a list,the first item is always in postion zero 
print(fruits)
print(fruits[0])
print(fruits[3])
#the whole list in purple is in position 3 because it follows element indexing rules
numbers = [1,2,3,[10,20],30,[40,[60,70]]]
#each square bracket carries a position
print(numbers[3][0])
print(numbers[5][1][0])
print(numbers[5][1][1])
#In python we can move backwards through list element
#we start from -1 and backwards
print(fruits[-1])
print(numbers[-1][-1][-1])
#pop removes the last element of the list
#append adds elements where the pop removed
#python is dynamically expandable overtime
#instruction are excuted line by line or statement by statement
print(fruits.pop())
fruits.append("kiwi")
print(fruits)
#list is a data type where new values can ba added or removed after its done prgramatically. We call this being mutable
#tuple its like a list that stores more than one valus and it uses parenthesis as its brackets
#example
names = ("shatrah","leone","arthur")
#we use the same indexing as those in lists
print(names[0])
print(names[-1])
#the difference between a tuple and a list is that things in a tuple are stored permanently. So the pop can't work.
#the computer will continue excuting because of the current error in 56 so we commented it out.
#print(names.pop())