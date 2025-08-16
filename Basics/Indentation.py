import keyword

print("hello world")
    # print("I am coder")
"""
     print statement has tab indentation, but it doesn't belong to a new)
     block of code. Python expects the indentation level to be consistent within the
     same block. This inconsistency causes an IndentationError.
"""
"""

#input/output
name=input("Enter your name: ")
print("hello, " ,name)

#maultiple I/O
Name='Rahul'
Age=25
marks=90.5
print(Name,Age,marks)

x,y,z=input("Enter x,y,z: ").split()  #bydefault user input taking as a String
print(x,y,z)
"""

"""
x=int(input("Enter x: ")) #Typecasting to int
print(type(x))

#output using Format
amount= 150.750
print("Amount: ${:.10f}".format(amount))

#Using f-String
Name='Tusar'
age=90
print(f"Age: {age} and Name: {Name}")

#using % operator
num=int(input("Enter num: "))
add=num+10
print("The sum is %d" %add)
"""

import keyword
print(keyword.kwlist)




