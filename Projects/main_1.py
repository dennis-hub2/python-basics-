from tkinter import *
from tkinter import StringVar

#assign root to imported file
root = Tk()

#the size
root.geometry("500x300")

#define function
def getvals():
    print("Accepted")

#Creating Heading add gird(row=number of row of tile   and column=number of column of tilte)
Label(root, text="Relationship Registration Forms", font="ariel 15 bold ").grid(row=0, column=3)

#creating the field name
First_Name = Label(root, text="First Name")
Last_Name = Label(root, text="Last Name")
Age = Label(root, text="Age")
Telephone = Label(root, text="Telephone")
Qualification = Label(root, text="Qualification")

#Arranging the field name
First_Name.grid(row=1, column=2)
Last_Name.grid(row=2, column=2)
Age.grid(row=3, column=2)
Telephone.grid(row=4, column=2)
Qualification.grid(row=5, column=2)

#making variable for storing data
First_Namevalue = StringVar
Last_Namevalue = StringVar
Agevalue = IntVar
Telephonevalue = IntVar
Qualificationvalue = StringVar
checkvalue = IntVar

#making the Entry point
First_Nameentry = Entry(root, textvariable =First_Namevalue)
Last_Nameentry = Entry(root, textvariable =Last_Namevalue)
Ageentry = Entry(root, textvariable =Agevalue)
Telephoneentry = Entry(root, textvariable =Telephonevalue)
Qualificationentry = Entry(root, textvariable =Qualificationvalue)

#Packing the entry field(In a box form)
First_Nameentry.grid(row=1, column=3)
Last_Nameentry.grid(row=2, column=3)
Ageentry.grid(row=3, column=3)
Telephoneentry.grid(row=4, column=3)
Qualificationentry.grid(row=5, column=3)

#creating a check button
chechbtn =  Checkbutton(text="remember me?", variable=checkvalue)

#packing the check button
chechbtn.grid(row=6, column=3)

#Submit button
Button(text="Submit", comman=getvals).grid(row=7, column=3)


root.mainloop()