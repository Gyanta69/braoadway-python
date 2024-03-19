#Syntax
'''
class parent():
    x = 11
class child(parent):
    a = 55

obj = child(parent)
print(obj.a)
print(obj.x)
'''
# 1.
'''
class Parent1(): #class name
    def test_parent(self): # method name
        return "This is from parent class"


class Child1(Parent1): # parent1 class inherited 
    def test_child(self):
        return "this is from child class"
    
obj = Child1()# creating an object
print(obj.test_parent())
print(obj.test_child())

print("==========================================================================================")
'''
#2.
'''
class Parent2():
    def __init__(self,x,y) -> None: # constructor
        self.a = x
        self.b = y#variables
    def test_parent(self):#methods
        return "This is from parent class"


class Child2(Parent2):#inheritance
    def test_child(self):
        return "this is from child class and tha value is"  + str(self.a)
    
obj = Child2(1,2)#object
print(obj.test_child())

print("=======================================================================================")
'''
#3.
'''
class Parent3():
    def __init__(self) -> None:
        self.a = 11
        self.b = 34
    def test_parent(self):
        return "This is from parent class"

class Child3(Parent3):
    def __init__(self, c, d) -> None:
        self.x = c
        self.y = d
        Parent3.__init__(self)# calling parent class constructor

    def test_child(self):
        return "this is from child class and tha value is"  + str(self.a)
    
obj = Child3(1,2)
print(obj.test_child())

print("=======================================================================================")'''
#4
'''
class Parent4():
    def __init__(self,x,y) -> None:
        self.a = x
        self.b = y
        
    def add(self):
        return self.a + self.b

    
class Child4(Parent4):
    def sub(self):
        return self.a - self.b
        
obj = Child4(40,20)
print(obj.add()) 
print(obj.sub())  
'''
#5
#Multiple Inheritance
'''
class Parent5():
    x = 11
class Parent6():
    a = 44
class Child6(Parent5,Parent6):
    z = 22
object = Child6()
print(object.a)
'''
#6
'''
class Parent7():
    x = 11
class Parent8(Parent7):
    z = 22

class Child7(Parent8):
    a = 56
object = Child7
print(object.x)
print(object.z)'''



    