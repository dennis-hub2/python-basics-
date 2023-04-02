""""
Write a code for a grading system 
"""
#Intro
print("Welcome to ESA Grading System.")

#Score input
Score = int(input("Your Score? "))

#true if score is 90 or more than 90 but less than 100
if Score >= 90 and Score <= 100: 
    print("Grade A")

#true if score is 80 or more than 80 but less than 90
elif Score >= 80 and Score <= 89:
    print("Grade B")

#true if score is 60 or more than 60 but less than 80
elif Score >= 60 and Score <= 79:
    print("Grade C")

#true if score is 40 or more than 40 but less than 60
elif Score >= 40 and Score <= 59:
    print("Grade D")

#true if score is less than 0 or more than 100
elif Score < 0 or Score > 100 or Score >= 101:
    print("Invalid format..... Check your score and type again.." )
else:
    print("Grade F")