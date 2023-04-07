#using for loops in python (start, stop, step)
for numbers in range(1,21,):
  print(numbers)

#even numbers from 1 to 20
for numbers in range(2,21,2):
  print(numbers)

# in the reversed form
for numbers in range(20, 1, -1):
  print(numbers)

# if one paramenta, the number is the stop
for numbers in range(21):
  print(numbers)
# printing a word among word
name = "joe"
print(name[2])

for numbers in name:
    print(name)

student = ["Joe", "Peniel", "Nessa", "Abena"]
print(student[1])

# using the for loop for 2x table
for numbers in range(1,13,):
    print(f"2 * {numbers} = {2 * numbers}")


"""
puting items in a list using for loop
"""
Students = []
for number in range(5):
  userInput = input("Enter your name: ")
  Students.append(userInput)
print(Students)


