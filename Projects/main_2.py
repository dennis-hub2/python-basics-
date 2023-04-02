#making a pizza bill


#first make an intial bill to be 0
bill = 0

#Welcom msg

print("Welcome to ESA pizza Delivery")

# Ask user for pizza size
size = input("What size pizza do you want (Small, Medium, Large)? ")

# Ask user if they want extra cheese
extra_cheese = input("Do you want extra cheese (Yes/No)? ")

# Ask user if they want pepperoni
extra_pepperoni = input("Do you want pepperoni (Yes/No)? ")

# Calculate pizza price based on size
if size == "Small":
    bill += 55
elif size == "Medium":
    bill += 85
else:
    bill += 120

# Add extra charge for extra cheese
if size == "Small" and extra_cheese == "Yes":
    bill += 5
elif size == "Medium" and extra_cheese == "Yes":
    bill += 10
elif size == "Large" and extra_cheese == "Yes" :
    bill += 15
else:
    bill += 0
# Add extra charge for extra pepperoni
if size == "Small" and extra_pepperoni == "Yes":
    bill += 5
elif size == "Medium" and extra_pepperoni == "Yes":
    bill += 10
elif size == "Large" and extra_pepperoni == "Yes" :
    bill += 15
else:
    bill += 0

# Print total bill
print(f"Your total bill is", bill)
