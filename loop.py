# loop
# for loop
# for loop used in string , list dict and so on
a = [1,2,3,4,5]
for i in a :
    print(i)
for i in "broadway":
    print(i)

# loops  list of string
a = ["Prayan","khadka","Budhanilkantha"]
for i in a :
    print(i)

# set data
set_data = {1,2,3,4,5,6,6,7,3}
for i in set_data:
    print(i)

a = [1,2,3,4,5]
for i in a :
    if(i==1):
        print("1 is found")

#range
 # range(1=startvalue,3=endvalue,1=stepvalue)
for i in range(2,12,2):
    print(i)


for i  in range (0,6,1):
        print(i)

a =int(input("Enter a number"))
if(a==2):
     for a in range(0,10,2):
          print(a)
elif(a==3):
     for a in range(0,10,3):
          print(a)

# table of 2
for i in range(1,11,1):
     result =f'2 x {i} = {2*i}'
     print(result)

#to ask a user input and show it's table
num = int(input("Enter a number: "))

for i in range(1, 11):
    result = f"{num} x {i} = {num * i}"
    print(result)

#append
    a = []
    for i in range(1,11):
        a.append(i)
    print(a)

language =['python','c++','django','swift','PHP','pandas']
for i in range(0,len(language),1):
     print(language[i])

# nested loop
     for i in ['broadway','python']:
          for j in range(0,1,1):
               print(i,j)

for i in range(1,3,1):
     print(i)
     for j in range(1,10,1):
          if j == 2:
               break
          print("j ko value",j)
          
