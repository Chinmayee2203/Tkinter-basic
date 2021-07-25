from tkinter import *
parent = Tk()
parent.geometry('500x600')
parent.title("Address Book")

datas=[]
#adding functions
#Add info
def add():
    global datas
    datas.append([Name.get(),Number.get(),address.get(1.0,"end-1c")])
    update_book()

#Delete info
def delete():
    del datas[int(lb.curselection()[0])]
    update_book()

#reset
def reset():
    Name.set('')
    Number.set('')
    address.delete(1.0,"end")

#view info
def view():
    Name.set(datas[int(lb.curselection()[0])][0])
    Number.set(datas[int(lb.curselection()[0])][1])
    address.delete(1.0,"end")
    address.insert(1.0,datas[int(lb.curselection()[0])][2])

#update the book
def update_book():
    lb.delete(0,END)
    for n,p,a in datas:
        lb.insert(END,n)


#buttons,label,listbox
Name = StringVar()
Number = StringVar()

#adding frames here
f0 = Frame()
f0.pack(pady=10)

f1 = Frame()
f1.pack()

f2 = Frame()
f2.pack(pady=10)

#name
l1 = Label(f0,text = "Name",font="times 12 bold").pack(side=LEFT)
e1 = Entry(f0,textvariable = Name,width=40,bg = "violet").pack()

#Number
l2 = Label(f1,text = "Number",font = "times 12 bold").pack(side=LEFT)
e2 = Entry(f1,textvariable = Number, width = 40,bg="violet").pack()

#address
l3 = Label(f2,text = "Address",font = "times 12 bold").pack(side=LEFT)
address = Text(f2,width=30,height=10,bg = "violet")
address.pack()

#creating buttons here
b1 = Button(parent,text = "Add",font="times 12 bold",fg = "blue",command=add)
b1.place(x=100,y=270)

b2 = Button(parent,text = "Delete",font="times 12 bold",fg = "green",command=delete)
b2.place(x=100,y=310)

b3 = Button(parent,text = "View",font="times 12 bold",fg = "grey",command=view)
b3.place(x=100,y=350)

b4 = Button(parent,text = "Reset",font="times 12 bold",fg = "red",command=reset)
b4.place(x=100,y=390)

#creating a scrollbar 
s1 = Scrollbar(parent,orient = VERTICAL)
lb = Listbox(parent,yscrollcommand = s1.set,height=12,bg="brown") 
s1.config(command=lb.yview)
s1.pack(side=RIGHT,fill=Y)
lb.place(x=200,y=260)

parent.mainloop()
