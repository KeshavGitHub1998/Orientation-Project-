from tkinter import *

#creating main object
MainObj=Tk()

#creating the geometry
#MainObj.geometry("500x250+100+10")

MainObj.configure(background='black')

#fm = Frame(MainObj,bg="blue")
#fm.pack(side=TOP, expand=NO, fill=NONE)



#assigning title
MainObj.title("Aagman Page")

#heading line /title
LabTitle=Label(text="Aagman Page",font=('arial',"30","bold"),bg='black',fg='green2').pack(fill=X)

#main labels
LabUserName=Label(text="UserName",font=('times',"20",'italic'),bg='black',fg='green2',width=200,height=2).pack()

#teking entry
VarUserName=StringVar()
text=Entry(textvariable=VarUserName,fg='black',bg='green2',font=('times','10','bold'),width=100).pack()

#main labels
LabPassword=Label(text="Password",font=('times',"20",'italic'),bg='black',fg='green2',width=200,height=2).pack()

#teking entry
VarPassword=StringVar()
text=Entry(textvariable=VarPassword,fg='black',bg='green2',font=('times','10','bold'),width=100).pack()

#buttons
ButLogIn=Button(text="LogIn",bg="black",fg="white",width=100).pack()
ButRegister=Button(text="Register",bg="black",fg="white",width=100).pack()
ButForgotPass=Button(text="Forgot Password",bg="black",fg="white",width=100).pack()

#ending mainloop
MainObj.mainloop()