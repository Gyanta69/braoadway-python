# i = 3
# while (i == 3):
#     print("test")
#     i = 4


games_play = "yes"
while(games_play=="yes"):
    promot = print(promot)
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    c = int(input("Enter number for above operation"))
    if ( c == 1 ):
        print( a + b)
    elif( c == 2 ):
        print( a - b )
    else:
        print("wrong command")
        break
    games_play = input("Do you want to restart,yes for continue")

import random
a = random.randrange(1,15)
print(a)
n= int(input("Enter a number for guessing:"))
counter = 0
while(a!= n):
    counter = counter + 1
    print(f'{n} is not a random number')
    n = int(input("Enter a nummber for guessing"))
print(f'{n} is a random number tries {counter + 1} times to guess the number')
'''
'''
#Program to print numbers from 0 to 10 and 10 to 0 using while condition
i = 0
while(i<11):
    print(i)
    i = i + 1
while(i>0):
    print(i)
    i = i - 1

#nested
i = 0
j = 10
while(i<11):
    while(j>=0):
        print(j)
        j = j-1
    print(i)
    i = i + 1

a = []
for i in range(1,10,1):
    a.append(i)
print(a)
# List comprehension
a=[i for i in range(1,10,1)]
print(a)


def game():
    a = '''
        1:Operations Task
        2: Random Number'''
    print(a)
    number = int(input("Enter a number:"))
    if number == 1 :
        return arth_oper()
    else:
        return random_game()
game()
