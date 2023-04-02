""""
addition = +
subtraction = -
multiplication = *
power = **

Mathimatical Operator
PEMDAS (p=parentences e=exponent m=mutiplication d=division a=addition s=subtraction)

Logical Operators
and, or, <, >, <=, >=, ==, !=(not equal to), not
"""

# a = 6
# # print(a==5)
# # print(a>5)
# print(a>=5)

gender = "Female"
age = 12
print(gender=="Male" or age==12)
print(gender=="Male" and age==12)
print(gender=="Female" or age!=12)

#NOT(!)>AND(&&)>OR(||)

#Conditional statments
age = int(input("Age"))
if age <= 0:
  print("Invalid age")
else: 
  if age >= 18 and age <= 79:
    print("You can drive")

