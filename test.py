a=33
b=200

if b>a :

 print ("b is greater than a")

if 5 > 2 :
  print("Five is greater than two!")

x = 5 
y = "Hellow world!"

print(x)
print(y)

#this is how you comment

#creating variables

x = "Teddy"
y = "Thendo"
print(x)
print(y)

#casting

x = str(3)     # x will be '3'
y = int(3)     # y will be 3
z = float(3)   # z will be 3.0

#printing the type of class
x = 5
y = "Marageni"
print(type(x))
print(type(y)) 

#string variables can be declared either by using single or double quotes

#variables are case-sensitive

#variable names

myvar = "T"
my_var = "E"
_my_var = "D"
myVar = "D"
MYVAR = "Y"
myvar2 = "BEAR"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#Camel Case myVariableName = "TED"
#Pascal Case MyVariableName = "TEDDY"
#Snake Case my_variable_name = "TEDDYBEAR"

#many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 

#global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 



"""
SETTING DATA TYPES
x = "Hello World" 	str 	
x = 20 	int 	
x = 20.5 	float 	
x = 1j 	complex 	
x = ["apple", "banana", "cherry"] 	list 	
x = ("apple", "banana", "cherry") 	tuple 	
x = range(6) 	range 	
x = {"name" : "John", "age" : 36} 	dict 	
x = {"apple", "banana", "cherry"} 	set 	
x = frozenset({"apple", "banana", "cherry"}) 	frozenset 	
x = True 	bool 	
x = b"Hello" 	bytes 	
x = bytearray(5) 	bytearray 	
x = memoryview(bytes(5)) 	memoryview 	
x = None 	NoneType

SETTING THE SPECIFIC DATA TYPE
x = str("Hello World") 	str 	
x = int(20) 	int 	
x = float(20.5) 	float 	
x = complex(1j) 	complex 	
x = list(("apple", "banana", "cherry")) 	list 	
x = tuple(("apple", "banana", "cherry")) 	tuple 	
x = range(6) 	range 	
x = dict(name="John", age=36) 	dict 	
x = set(("apple", "banana", "cherry")) 	set 	
x = frozenset(("apple", "banana", "cherry")) 	frozenset 	
x = bool(5) 	bool 	
x = bytes(5) 	bytes 	
x = bytearray(5) 	bytearray 	
x = memoryview(bytes(5)) 	memoryview
"""

#RANDOM NUMBER
import random

print(random.randrange(1, 10))

#Multiline Strings use double or single qoutes
a = """Hi my name is Thendo Charmaine Marageni. 
I am an aspiring data analyst."""
print(a) 

#Strings are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "banana":
  print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

#if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt) 

#if statements
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Slicing
  b = "Hello, World!"
print(b[2:5])

#Slice From the Start
b = "Hello, World!"
print(b[:5])

#Slice To the End
b = "Hello, World!"
print(b[2:])

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

#Upper Case
a = "Hello, World!"
print(a.upper())

#Lower Case
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format

#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 


"""
Escape Characters
\' 	Single Quote 	
\\ 	Backslash 	
\n 	New Line 	
\r 	Carriage Return 	
\t 	Tab 	
\b 	Backspace 	
\f 	Form Feed 	
\ooo 	Octal value 	
\xhh 	Hex value
"""

#Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9) 
