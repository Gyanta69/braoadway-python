# WAP to ask user 3 input
# i = int(input("Enter a number: "))
# l = []

# for i in range(1,len(l),1):
#     for j in range(1,11,1):
#         result = f'{i} x {j} = {i*j}'
#         print(result)
#         l.append(result)
#     print(' ')
#Assignment
num = []
for i in range(1,6):
    enteredNum = int(input('Enter a number: '))
    num.append(enteredNum)
noRepeat = set(num)
for enteredNum in noRepeat:
    print(' ')
    print(f'Multiplication table of {enteredNum} is :') 
    
    for i in range(1,11):
       output = (f'{enteredNum} x {i} = {enteredNum*i}')
       print(output)
print(' ')
print("The values stored in list is",num)
       

