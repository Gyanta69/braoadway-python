class Test():
    x = 10
    print("i am a class")

    def __str__(self):
        return "i am a return function"
    def test(self):
        return  "this is a test1"
obj = Test()
print(obj)

# calling class properties
print(obj.x)
print("===============================")
print(obj.test)

class Test2():
    def __init__(self):
        self.a = 12
        self.b = 50 
        print("init is a constructor")
    def __str__(self):
        return f'{self.a + self.b}'
    
obj = Test2()
print(obj)
      
