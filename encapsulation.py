class PublicClass():
    __pro = 10  
    def __test(self) -> None:
        print(self.__pro)

obj = PublicClass()


class Car():
    model = 'tesla'
    __model = 'test is private'
    private_model = __model

    def public_method(self):
        return "This is a public method"
    
    def _test_private_method(self):
        return "This is a private method"
    
    def test_private_method(self):
        return self._test_private_method()

obj = Car()
print(obj.private_model)
print(obj.public_method())
print(obj._test_private_method()) 

class Clothes():
    fabric = 'cotton'
    __type = 'Sweaters'
    private_type = __type

    def fabric_selection(self):
        return "The fabric has been selected"

    def type_of_clothes(self):
        return "The type of clothes has been selected"

    
    

    
