# arithematic operators
a=6
b=7
c=2
print(a+b) # addition

print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division

# assignment operators
a=6-5
b*=6
c+=3 ## means increment c by 3  and assign it to c
d=10 
d/=2
print(a)
print(b)
print(c)
print(d)

#comparsson operators
print(a==b) # equal to
print(a!=b) # not equal to
print(a>=b)
print(a<=b) # less than or equal to
print(a>b)
e=5>=5
print(e)

# logical operators
e = True or False
print(e)
# Logical Operator Truth Table in Python
# truth table for logical operations
print("╔════════╦════════╦══════════╦═════════╦════════╗")
print("║   A    ║   B    ║ A and B ║ A or B ║ not A ║")
print("╠════════╬════════╬══════════╬═════════╬════════╣")

truth_values = [True, False]

for A in truth_values:
    for B in truth_values:
        print(f"║ {str(A):<6} ║ {str(B):<6} ║ {str(A and B):<8} ║ {str(A or B):<7} ║ {str(not A):<6} ║")

print("╚════════╩════════╩══════════╩═════════╩════════╝")
# Logical operations with variables
print(a>5 and b<10) # and operator
print(a>5 or b<10) # or operator 
print(not(True))