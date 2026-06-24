names = ["Isabella","Valary","Roger","John"]
#checking for the name thats not in the list
#"if" and most conditions statements are a block of code because they have 2 or more statements that perform a specific task.
if names != "Osman":
    print(names)

if "Osman" not in names:
    print("Osman")

name1 = "Osman"
if "O" in name1:
    print("O is in the name Osman")

#conditins with alternatives or options in case the first condition ccn't be found.
#for true or false we use if and else both are block od codes.
numbers = [10,20,30,40,50,60]
if 80 in numbers:
    print("80 is found")
else:
    print("80 is not found")

countries = ['Uganda',"Kenya","Tanzania","Rwanda","Burundi"]
if "Somalia" in countries:
    print("Somalia is in EA")
else:
    print("Somalia is not in EA")

#if...elif...else
#used in cases where we have more than 2 conditions that are related to each other
daysoftheweek = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
#this will be ignored because its not true
if daysoftheweek[0] == "Monday":
    print("Monday is the first day of the week")
elif daysoftheweek[1] == "Monday":
    print("Monday is the second day of the week")
#this will also be ignored because its not true
elif daysoftheweek[2] == "Monday":
    print("Monday is the first day of the week")
else:
    print("Monday is not a day of the week")

