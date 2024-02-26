
# f string is a part of format method
fName = 'Pragyan'
lName = 'Khadka'
fString = 'My name is {} {}'
print(fString.format(fName, lName))  # format method takes the arguments given by the user and places them in the string where the {} placeholders are

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
item_1 = 'Bags'
item_2 = 'Purse'
price_1 = 300
price_2 = 200
w = 'Item one is {} and item two is {} and the price is {} and {}'
print(w.format(item_1 , item_2 , price_1 , price_2)) 

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
item_1 = 'Bags'
item_2 = 'Purse'
price_1 = 300
price_2 = 200.499
w = 'Item one is {0} and item two is {1} and the price is {2} and {3:.2f}' # here .2f indicates decimal values 
print(w.format(item_1 , item_2 , price_1 , price_2)) 


#Can use the index numbers if we want same values more than once
age = 18
name = "Pragyan"
txt = "My name is {1}. {1} is {0} years old."
print(txt.format(age, name)) 

'''item_1 = 'Bags'
 item_2 = 'Purse'
 price_1 = 300
 price_2 = 200.499
 w = 'Item one is {1} and item two is {1} and the price is {2:.2f} and {2:.2f}' 
 print(w.format(item_1 , price_1))'''

#fstring
result = f'pragyan{fName}'
print (result)

# a = int(input("Please enter a first number"))
# b = int(input("Please enter a Second number"))
# result = f'result of {a} and {b} is {a+b}'
# print(result)
# assigning one value to multiple variable
a,b,c = 1
a = 1
b = 1
c = 1



