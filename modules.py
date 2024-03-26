import encapsulation
from class1 import parent as parent1 # This  as keyword is used to give alias name to the module
obj = encapsulation.Car()
print(obj.model)

obj = parent1()
print(obj.parent1)

