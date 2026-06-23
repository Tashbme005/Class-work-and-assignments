#an operator is a symbol, character or anything in a statement that tells a computer what to do using an operand.
#an operand is a value an operator acts upon
a=7
b=3
#adds
print("sum",a+b)
#divides
print("floor div", a//b)
#gives the remainder after dividing
print("modulo", a%b)
#gives a power
print("power",a**b)
#= after an arithmetic operator assigns that new value to the variable before both of them
#new a = 7 + 7
a+=7
print(a)
#a = 14
print(a+b)
#14 + 3
print(a*b)
#14*3
a-=7
#new a = 14 - 7= 7
print(a)
a*=2
#new a = 7*2
print(a)
a/=2
#a = 1
print(a)
#use logic not math. 1 cannot be divided among 3 so it remains 1
a%=3
#a = 1
print(a)
a*=7
# a = 1*7 = 7
print(a)
#this means equal to
print(a==b)
#assigns the value of a to x
x=a
print(x)
# assigns the value of b to y
y=b
print(y)
# asks if x is equal to y
print(x==y)
#asks if x is no equal to y
print(x!=y)
print(x>y)
#if x is greater and less than y
print(x<y)
#if y is greater than x
print(y>x)
#picks out only the true and ignore the false. this depends on the statement being true or false
# true since x is greater than y
print(x>=y)
#gives false because x is greater than y
print(x<=y)
#x = 7 and y = b
print(x<5 and y<5)
print(x<1 or y>1)
z=[10,20,30,40]
print(10 in z) 
