# """"
# Relational Operators.
# NOT(!)>AND(&&)>OR(||)
# """
# # a = 12
# # b = 9
# # print(a > b)

# """"
# basic if statement with relational and logical operators
# """

# first_num = int(input("Enter first number: "))
# second_num = int(input("Enter second number: "))

# #if (condition):
# if(first_num > second_num):
#     print(f"{first_num} is greater than {second_num}")
# #elif (condition):
# elif second_num > first_num :
#     print(f"{second_num} is greater than {first_num}")

# #else:
# else: 
#     print("they are equal")



""""
Making a short code..
1. Transfer Money
2. MomoPay and Pay Bills
3. Airtime and Bundles

#transfer Money
1. Momo user
2. Non.momo user
3. Send with care
"""

print("""
1. Transfer Money
2. MomoPay and Pay Bills
3. Airtime and Bundles
""")

userInput = int(input())

if userInput == 1 :
    print("""
    # Transfer Money
    1. Momo user
    2. Non.momo user
    3. Send with care
    """)

    userInput = int(input())
    # nested if statement
    if userInput == 1:
        print("Momo user")
    elif userInput == 2:
        print("Non Momo user")
    elif userInput == 3:
        print("Send with care")
    else:
        print("Invalid Input......try again...")

elif userInput == 2:
    print("MomoPay and Pay Bills")
elif userInput == 3:
    print("Airtime and Bundles")
else:
    print("Invalid user....try again...")
    
