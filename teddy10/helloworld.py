message = "Hello world"

print(message)

teddy_age = 12
youth_age = 13

if teddy_age > youth_age :
    print ("Teddy is in youth")
elif teddy_age == youth_age :
    print("Enjoy youth")
else : 
    print("Teddy should be in sunday school")

def print_teddy():
    text = "teddy ia just a baby"
    print(text)
    
print_teddy()

def school_age_calculator(age,name) :
    if age < 5 :
        print("Enjoy the time, ", name , "is only ", age)
    elif age == 5:
        print("Enjoy kindergarden, " , name)
    else : 
        print("They grow up so fast")
        
school_age_calculator(10,"Teddy")     

def add_ten_to_age(age):
    new_age = age + 10
    return new_age

how_old_will_i_be = add_ten_to_age(3)
print(how_old_will_i_be)

#while 
x=0
while (x<5):
   print (x)
   x=x+1 
   
days=["Mon","Tues","wed","Thur","Frid","Sat" , "Sun"]  

for d in days :
   if (d=="Thur"):break
   print(d)
   
   
   import math
   print ("Pie is", math.pi)
   