# Python3 program to
# demonstrate defining
# a class

class Dog:
	pass


obj = Dog()

class Dog:

# ckass attribute 
attr1 = "mammal"

#instance attribute
def __init__(self , name ):
    self.name = name 
    
 #driver code  
 #object instantiation
Bobby = Dog("Bobby")
Snoppy = Dog("Snoppy")

#Accessing class attributes
print("Bobby is a {}".format(Bobby.__class__.attr1))
print("Snoppy is also a {}".format(Snoppy.__class__.attr1))

#Accesssing instance attributes 
print("My name is  {}".format(Bobby.name))
print("My name is  {}".format(Snoppy.name))

    
