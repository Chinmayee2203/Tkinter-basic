from tkinter import *
from tkinter import messagebox as mb
import json

class Quiz:
    def __init__(self):
        #initializing the question number to 0
        self.q_no = 0
        #assigns questions to display_ques function
        self.display_title()
        self.display_ques()
        #select_opt will hold an integer value
        self.select_opt=IntVar()
        #display radio buttons and options for the current question
        self.opts=self.radio_buttons()
        self.display_opts()
        #display next and exit buttons
        self.buttons()
        #counter for right answers
        self.correctans=0
        #no. of questions
        self.data_size = len(question)

    #method used to display result 
    #after counting the right and wrong answers
    def calculate_result(self):
        #calculate the wrong count
        wrongans = self.data_size - self.correctans
        correctans = f"correct : {self.correctans}"
        wrongans = f"wrong : {wrongans}"

        #calculate the percentage of correct answers
        score = int(self.correctans/self.data_size * 100)
        result = f"Score :{score}%"

        #display this result in a messagebox
        mb.showinfo("Result",f"{result}\n{correctans}\n{wrongans}")

    def check_ans(self, q_no):
        if self.select_opt.get() == answer[q_no]:
            return True
    
    #On clicking, checks if the answer is correct and increases correct count by 1
    # and if it is the last question, displayes the result
    def next_btn(self):
        #if the answer is correct
        if self.check_ans(self.q_no):
            self.correctans += 1
        self.q_no += 1
        
        #if the q_no size is equal to data size 
        #i.e, it has reached the end
        #then display the result
        if self.q_no == self.data_size:
            self.calculate_result()
            #destroy the GUI
            parent.destroy()
        else:
            self.display_ques()
            self.display_opts()
               
    #defining the Next and Exit buttons here
    def buttons(self):
        nextbutton = Button(parent,text="NEXT",bg = "green",width=10,command = self.next_btn)
        nextbutton.place(x=350,y=400)
        exitbutton = Button(parent,text="EXIT",bg = "red",width=10,command = parent.destroy)
        exitbutton.place(x=550,y=400)

    #method for deselecting the radiobuttons
    #display options available for question number and
    #updates the options for the current question of the radio buttons
    def display_opts(self):
        val = 0
        #deselect the options
        self.select_opt.set(0)

        #loops over the options to be displayed for the radio buttons
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val += 1

    #method to print the current question
    def display_ques(self):
        q_no = Label(parent,text = question[self.q_no],bg="grey",fg="white",width=50,font="arial 18 bold",anchor="w")
        q_no.place(x=50,y=100)

    #displays the title here
    def display_title(self):
        title =Label(parent,text="The Capital Quiz",width=50,font="arial 20 bold",fg="yellow",bg="black")
        title.place(x=0,y=2)
    
    #displaying the radio buttons for the questions
    def radio_buttons(self):
        ypos = 150
        #initialize with empty list
        q_list=[]
        while len(q_list)<4:
            radbtn = Radiobutton(parent,text = " ",variable=self.select_opt,
            value= len(q_list)+1,font="arial 15",bg="grey",fg="black")
            #add the buttons to the list
            q_list.append(radbtn)
            radbtn.place(x=50,y=ypos)
            ypos += 30
        return q_list
    

#creating the gui window
parent = Tk()
parent.geometry("800x450")
parent.title("MyQuiz")
#adding background image
bg = PhotoImage(file = 'quizbg3.png')
bg_label = Label(parent,image = bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#loading data from the json file
with open('data.json')as f:
    data=json.load(f)
question = (data['question'])
answer= (data['answer'])
options  =(data['options'])
#creating an object here
quiz= Quiz()
parent.mainloop()
