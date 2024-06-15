x = 4
y ="Zobaer"
print(x)

#Casting: It's heppend when we specify any type of variable
a = int (4)
b = str (4)
c = float (4)

print ("Int = ",a, "\nString = ",b, "\nFloat = ",c)

#Get the type of this variable

A = 4
B = 4.5
C = "My String"
print(type(A))
print(type(B))
print(type(C))

#Variable names
my_variable = "Zobaer"
My_Variable = "Zobaer"
print(my_variable)
print(My_Variable)

#Assign Multiple varible in one line 
d = e = f = 40
print(d, e, f)

X, Y, Z = "Audi", "Marcedes", "Rolls Royce"
print(X)
print(Y)
print(Z)

#Unpack from lists or array
Cars = ["Toyata", "Marcedes", "Honda"]
x, y, z = Cars
print(x)
print(y)
print(z)

#Output variables
firstName = "S. S. Zobaer"
lastName = " Ahmed"
print("My name is",firstName+lastName)

#N:B: For number "+" is worked as a assignment operator
num1 = 4
num2 = 5
print(num1+num2)

#N:B for different types of datatype we have to use ","
num = 4
string = "Code Lovers"
print(num, string)

#Global Variable
comment = "Awesome" #global variable

def myFunc():
    global comment #global keyword define the variable as global
    comment = "fantastic"
    print("DSA is "+comment)
myFunc()
print("Python is " +comment)