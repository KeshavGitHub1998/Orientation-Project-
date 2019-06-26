from tkinter import *

#creating main object
MainObj=Tk()

#creating the geometry
#MainObj.geometry("500x250+100+10")

MainObj.configure(background='black')

#fm = Frame(MainObj,bg="blue")
#fm.pack(side=TOP, expand=NO, fill=NONE)



#assigning title
MainObj.title("Registeration ")

#heading line /title
LabTitle=Label(text="Registeration",font=('arial',"25","bold"),bg='black',fg='green2').grid(row=1)

#making labels and entries
LabName=Label(text="Full Name",font=('times','15'),bg='black',fg='green2').grid(row=2,column=1)
EName=StringVar()
EntryName=Entry(textvariable=EName).grid(row=2,column=2)


LabCallNum=Label(text="Calling Number",font=('times','15'),bg='black',fg='green2').grid(row=3,column=1)
ECallNum=StringVar()
EntryCallNum=Entry(textvariable=ECallNum).grid(row=3,column=2)


LabWhatsappNum=Label(text="Whatsapp Number",font=('times','15'),bg='black',fg='green2').grid(row=4,column=1)
EWhatsappNum=StringVar()
EntryWhatsappNum=Entry(textvariable=EWhatsappNum).grid(row=4,column=2)


LabEmail=Label(text="E-Mail address",font=('times','15'),bg='black',fg='green2').grid(row=5,column=1)
EEmail=StringVar()
EntryEmail=Entry(textvariable=EEmail).grid(row=5,column=2)


LabHighSchool=Label(text="High School",font=('times','15'),bg='black',fg='green2').grid(row=6,column=1)
EHighSchool=StringVar()
EntryName=Entry(textvariable=EHighSchool).grid(row=6,column=2)


LabHomeTown=Label(text="Home Town",font=('times','15'),bg='black',fg='green2').grid(row=7,column=1)
EHomeTown=StringVar()
EntryHomeTown=Entry(textvariable=EHomeTown).grid(row=7,column=2)


LabEnrollNum=Label(text="Enrollment Number",font=('times','15'),bg='black',fg='green2').grid(row=8,column=1)
EEnrollNum=StringVar()
EntryEnrollNum=Entry(textvariable=EEnrollNum).grid(row=8,column=2)


LabOSDevice=Label(text="OS in Device (iOS/Android/Windows/other)",font=('times','15'),bg='black',fg='green2').grid(row=9,column=1)
EOSDevice=StringVar()
EntryOSDevice=Entry(textvariable=EOSDevice).grid(row=9,column=2)


LabDepartment=Label(text="Department(ASET/ABS/ASL/ASAP,etc.)",font=('times','15'),bg='black',fg='green2').grid(row=10,column=1)
EDepartment=StringVar()
EntryDepartment=Entry(textvariable=EDepartment).grid(row=10,column=2)


LabCourse=Label(text="Course (B.Tech Cse/B.Com / Bsc)",font=('times','15'),bg='black',fg='green2').grid(row=11,column=1)
ECourse=StringVar()
EntryCourse=Entry(textvariable=ECourse).grid(row=11,column=2)


LabSpec=Label(text="Specialisation(Computer Science/Hons./NA)",font=('times','15'),bg='black',fg='green2').grid(row=11,column=1)
ESpec=StringVar()
EntrySpec=Entry(textvariable=ESpec).grid(row=11,column=2)


LabBloodGroup=Label(text="Blood Group",font=('times','15'),bg='black',fg='green2').grid(row=12,column=1)
EBloodGroup=StringVar()
EntryBloodGroup=Entry(textvariable=EBloodGroup).grid(row=12,column=2)



LabPassword=Label(text="Password for TACAPP",font=('times','15'),bg='black',fg='green2').grid(row=21,column=1)
EPassword=StringVar()
EntryPassword=Entry(textvariable=EPassword).grid(row=21,column=2)


'''
LabName=Label(text="Full Name",font=('times','15'),bg='black',fg='green2').grid(row=7,column=1)
EName=StringVar()
EntryName=Entry(textvariable=Ename).grid(row=7,column=2)'''

ButSubmit=Button(text="Submit",font=('times','10'),bg='black',fg='white').grid(row=22,column=1)

#ending mainloop
MainObj.mainloop()