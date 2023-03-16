"""
Write a python script that takes input from a user and display it 
to the user in a well formatted output(use the concept of list)
Detail:
Name, Age, Class, Gender, Telephone
"""
#after every input add the value to the userDetail
userDetails = []
userInput = input("What is your name: ")
userDetails.append(userInput)

userInput = input("Enter age: ")
userDetails.append(userInput)

userInput = input("Enter class: ")
userDetails.append(userInput)

userInput = input("Enter your Gender: ")
userDetails.append(userInput)

userInput = input("Telephone: ")
userDetails.append(userInput)


#outputing it in a well format
print(f"\nYour name is {userDetails[0]}\nYour age  {userDetails[1]}.\nYour class {userDetails[2]}.\nYour Gender {userDetails[3]}.\nYour Telephone {userDetails[4]}.\n")

"""
pushing it on git
git add .
git commit -m "My first Assignment"
git push
"""