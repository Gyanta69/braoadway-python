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
#multi level inheritance
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

#7
'''
class Parent5():
    x = 11

class Parent6():
    def __init__(self) -> None:
     self.a= 44 
    def parent6_test(self):
       print("This is parent 6 method" + str(self.a))

class Child6(Parent5,Parent6):
    def __init__(self) -> None:
        self.z = 22
        Parent6.__init__(self)

    def child_test(self):   
       print(self.a) 
object = Child6()
print(object.parent6_test())
'''
#8
'''
class Parent7():
    def __init__(self) -> None:
        self.a = 3
        self.b = 4
    def add(self):
        return f'This is parent 7{self.a+self.b}'
    
class Parent8(Parent7):
    def __init__(self) -> None:
        Parent7.__init__()
    def diff(self):
        return f'This is parent 8 {self.a-self.b}'
       
class Child7(Parent8):
    def __init__(self) -> None:
        Parent8 .__init__(self)
obj = Child7()
print(obj.add())
'''
#9
'''
'''

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def test(self):
        return"This is orignal test"
    
class B(A):
    def test(self):
        return "This is from class B "
obj = B()


    