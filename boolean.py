#print("odd or even")
p=int(input("enter given number:"))
if p%2==0:print("given number is even")
else:print("given number is odd")                
#print("max num")
a=int(input("enter number1:"))
b=int(input("enter number2:"))
c=int(input("enter number3:"))
if a>b and a>c:print("maximum value is:",a)
elif b>a and b>c:print("minimum value is:",b)
else:print("maximum value is:",c)
#print("leap year or not")
d=int(input("enter year:"))
if d%4==0:print("year is leapyear")
else:print("non leapyear")
