from tkinter import *
parent = Tk()
parent.title("Menu")

parent.geometry("600x550")
bg = PhotoImage(file = 'coffee-cappuccino-cafes-rain-wallpaper-preview.png')
bg_label = Label(parent,image = bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#calculating the price here
def calculate():
    dic1 = {'Cappuccino' : [e1,3.50],
            'Cafe Americano' : [e2,2.50],
            'Espresso': [e3,4.25],
            'Caramel Macchiato':[e4,4.25],
            'Iced Coffee':[e5,3.50],
            'Hot Chocolate':[e6,5.50,],
            'Cafe Mocha':[e7,4.50],
            'Iced Latte':[e8,3.25]}
    
    total = 0
    for key,val in dic1.items():
        if val[0].get()!="":
            total+= int(val[0].get())*(val[1])

    showcalc = Label(parent,text ="Total bill is- " + str(total),font="times 18")
    showcalc.place(x=200,y=455,anchor="s")
    #destroy it
    showcalc.after(1000,showcalc.destroy)
    parent.after(1000,calculate)

#adding restaurant name label
labelrest = Label(parent,text = "MyCafe",font="Arial 25 bold",bg="grey")
labelrest.place(x=300,y=40,anchor="center") 

#adding menu labels
labelhead = Label(parent,text="Menu",font = "times 20 bold",bg="grey")
labelhead.place(x=100,y=70,anchor="center")

#menu card
l1 = Label(parent,text = "Cappuccino                $3.50")
l1.place(x=50,y=110,anchor="w")
l2 = Label(parent,text = "Cafe Americano         $2.50")
l2.place(x=50,y=130,anchor="w")
l3 = Label(parent,text = "Espresso                    $4.25")
l3.place(x=50,y=150,anchor="w")
l4 = Label(parent,text = "Caramel Macchiato   $4.25")
l4.place(x=50,y=170,anchor="w")
l5 = Label(parent,text = "Iced Coffee                $3.50")
l5.place(x=50,y=190,anchor="w")
l6 = Label(parent,text = "Hot Chocolate           $5.50")
l6.place(x=50,y=210,anchor="w")
l7 = Label(parent,text = "Cafe Mocha               $4.50")
l7.place(x=50,y=230,anchor="w")
l8 = Label(parent,text = "Iced Latte                  $3.25")
l8.place(x=50,y=250,anchor="w")

#billing it
billhead = Label(parent,text = "Select the item",font = "times 20 bold",bg="grey")
billhead.place(x=460,y=70,anchor="center")

l11 = Label(parent,text ="Cappuccino")
l11.place(x=460,y=110)
e1=Entry(parent)
e1.place(x=430,y=130)
l22 = Label(parent,text ="Cafe Americano")
l22.place(x=460,y=155)
e2=Entry(parent)
e2.place(x=430,y=175)
l33 = Label(parent,text ="Espresso")
l33.place(x=460,y=200)
e3=Entry(parent)
e3.place(x=430,y=220)
l44 = Label(parent,text ="Caramel Macchiato")
l44.place(x=460,y=245)
e4=Entry(parent)
e4.place(x=430,y=265)
l55 = Label(parent,text ="Iced Coffee")
l55.place(x=460,y=290)
e5=Entry(parent)
e5.place(x=430,y=310)
l66 = Label(parent,text ="Hot Chocolate")
l66.place(x=460,y=335)
e6=Entry(parent)
e6.place(x=430,y=355)
l77 = Label(parent,text ="Cafe Mocha")
l77.place(x=460,y=380)
e7=Entry(parent)
e7.place(x=430,y=390)
l88 = Label(parent,text ="Iced Latte")
l88.place(x=460,y=415)
e8=Entry(parent)
e8.place(x=430,y=435)

#execute calculation after 1 sec
parent.after(1000,calculate)

parent.mainloop()
