# python inbulit dattypes
# list / arrays
a = 12

# list in python can accept any datatypes
b =[1,2,3,4,5,5.5,'Pragyan','Khadka'] #This is a list

print (b[6])

color = ["red", "Green", "Yellow", "Black", "white"]
print(color[1])
print(color[2])
print(color[3])
print(color[4])
print(color[1])

#negative indexing
color = ["red", "Green", "Yellow", "Black", "white"]
#         -5      -4        -3       -2      -1
print(color[-1])
print(color[-2])
print(color[-3])
print(color[-4])

#inbuilt list method

#append(to add value from last)
color = ["red", "Green", "Yellow", "Black", "white"]
color.append (1) 
print(color)
color.append ([1,2,3,4,5]) # you can also append a list
print(color)
color.append("Grey")
print(color)

#insert (To add value from the beginning)
color = ["red", "Green", "Yellow", "Black", "white"]
#          0       1         2        3        4
color.insert(0,"Black")
print(color)

# to concade a list
a = [1,2,3,4,5]
b = [3,4,5,6,7,8]
# len is used to calculate the length of a list
print(len(a))
print(a+b)

a = [] # empty list 
print(type(a))
print(len(a))

# extend
color = ["red", "Green", "Yellow", "Black", "white"]
extendcolor = ["Violet","Haze","Indigo"]
color.extend(extendcolor) # extend method is used add two different variable inside a list  
print(color)


# ADDING VALUES IN A LISTS
empty_list = []
print("Ans before adding in list:",empty_list)
a = input("Enter a number ")
b = input("Enter a number ")
c = input("Enter a number ")
empty_list.append(a)
empty_list.append(b)
empty_list.append(c)
print("Ans after adding in list:",empty_list)

