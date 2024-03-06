'''
if condition
syntax
if(condition)
   if block
'''
if (2 ==2):
    print("hello")
else:
    print("else block")

if(5>3):
    print("5 is greater than 4")

a = 5
b = 8
if(a>b):
    print("a is greater than b")
else :
    print("a is smaller than b")

'''
Multiple if condition
Syntax
if(condition):
    if block
elif(condition):
    elif condition
elif(condition):
   elif condition:    
else:
    else block
'''
if (2==3):
    print("2 and 3 are not equal")

elif(4==5):
    print("4 and 5 are not equal")
elif(5>5):
        print("5 is greater than 3")
else:
     print("else block")

a = int(input("Enter a number"))
b = int(input("Enter another number"))
if (a > b):
     print(f'{a} is greater than {b}')
elif(a == b):
     print(f'{a} is smaller than {b}')
else:
     print(f'{a} is equal to {b}')




'''
nested if condition
if(condition):
    if (condition):
        nested if condition
    elif (condition):
        nested elif condition
    else:
        nested else condition
    
    
 
'''


x = int(input("Enter a number"))
y = int(input("Enter second number"))
z = int(input("Enter second number"))

if(x>y):
     print("x is greater than y")
     if(x>z):
         print("x is greater than z")
         if(y>x):
              print("y is greater than x")
              if(y>z):
                   print("y is greater than z")
                   if(z>x):
                        print("z is greater than x")
                        if(z>y):
                             print("z is greater than y")
else:
     print("hello world")






         
     