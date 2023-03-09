name = "Dennis Ankora"
phone_number = 246885010
age = 21

print(name)
print(phone_number)
print(age)  


#list 
name_of_student = ["dennis","ama","kofi"]
#add name to list4
name_of_student.append("adwoa")
#taking data from the list
third_student=name_of_student[2]
print(third_student)

#python dictionary
Dennis_info = {
    "name":"mike",
    "age": 12,
    "hobbies" : {
    "outdoor": ["footbal", "baskestball"],
    "indoor": ["tabletennis","uno"]
    }
}
hobbies = Dennis_info["hobbies"]
print(f"my hobbies are {hobbies}")

outdoor = hobbies["outdoor"]
print(f"my outdoor hobbies are {outdoor}")

#adding to an empy list
Student_grade = {}
Student_grade["Mike"] = "A"
print("student_grade")

#input 
age = input("What is your age?\n")
print(f"Your age is {age}")
