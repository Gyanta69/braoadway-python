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



