def function_name():
    print("test function")

function_name()

def return_func():
    return 5+2
print(return_func())

a = return_func()
print(a)

def loop():
    a = []
    for i in range(1,3,1):
        a.append(i)
        return a

print(loop())

#Argument
#position argument  
def add_number(a,b,c):
    return a + b
print(add_number(1,2,3))

#Question 1 related to position argument
def funct_1(a,b,c):
    if(a==1):
        return a+b
    elif(a==2):
        return a-b
    elif(a==3):
        return a*b
    else:
        return "Wrong method"
print(funct_1(2,2,3))


# default argument
def add_function(a,b=6):
        return a+b
print(add_function(5))
print(add_function(5,7))

def force(m,g=9.8):
    return m * g
print("force on earth",force(20))
print("force on moon",force(20,1.92))
print("force on moon",force(20,5))

#keyword argument
#map the argument based on keyword
def funct_2(fname,lname):
    return fname+lname
a = funct_2(lname="Pragyan",fname="Khadka")
print(a)

# Aribatrary arguments,*args
#stores althe value given by the user
def args_function(*args):
    print("Test function")
args_function(1,2,3,4,5,6,7,7,9)

def  child(*character):
    for i in range(0,len(character)):
        print("name is",character[i])
child("pragyan","broadway","test")


def add_number(*args):
    result = 0  
    for i in args:
        result = result + i
    print(result)
add_number(1,2,3,4,5)

# Aribatrary keyword arguments,*args
def test_function(a,*args,**kwargs):
    print(a)
    print(args)
    print(kwargs)
test_function(1,2,3,4,10,5,6,name="Pragyan",test=True)



