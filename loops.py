#loops consume alot of memeory so we normally avoid them
#suppose we are going to count to 5
#1st number is included but the last number isn't. The number before the last valus becomes the upper limit.
for x in range (1,6):
    if x == 3:
        #skip 3 and count the rest
        continue
    else:
        print(x)

for x in range (1,6):
    #x acts as a tempoarary value representing value in a given rage in this case each value in (1,6)
    if x == 5:
        #stop there
        break 
    else:
        print(x)

integers = [10,20,30,40,50]
fruits = ["sugarcane","pineapple","mango","grapes"]
for fruit in fruits:
    if fruits == "pineapple":
        print("pineapple is sweet")
        break

#go into list of friuts and print each fruit in the fruits list
for fruit in fruits:
    print(fruit)

for item in fruits:
    print (item)

for ozzy in fruits:
    print(ozzy)

for number in range(10):
    if number % 2 == 0:
        print (number)

for number in range(10):
    if number % 2 != 0:
        print(number)

#while loops prints as long as condition is true. Used for imbepended systems.
#for loop is easily controllable