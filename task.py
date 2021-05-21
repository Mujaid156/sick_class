from tkinter import *
from tkinter import messagebox

easy = Tk()
easy.geometry("500x500")
easy.title("Medical Practice")
easy.config(bg="#9eeb10")
frame = Frame(easy)


var = StringVar()

# Calculations for Medicine pracitice
class Sick():
    def sickness(self):
        self.MSickID = sick
        self.MDurationOfTreatment = treat
        self.MDoctorsID = prac
        self.medcancer = 400
        self.medinflu = 350.50

# Calculating price for treatment Cancer
def sickness():
    if var.get() == "Cancer":
        if int(confee.get()) > 600:
            messagebox.showinfo("Message", "Sorry we cannot treat you") # Error message will display
        elif int(confee.get()) < 600:
           cancer_answer = int(confee.get()) + 400
           paid.config(text="Amount Paid For Treatment: " + str(cancer_answer))

    if var.get() == "Influenza":
        if int(confee.get()) >= 600:
            influ_answer = 350.50 + int(confee.get())
            paid.config(text="Amount Paid For Treatment: " + str(influ_answer))
        elif int(confee.get()) < 600:
            influ_answer = 350.50 + int(confee.get())
            discount = (influ_answer * (2/100)) + influ_answer
            messagebox.showinfo("Message", "2% discount")
            paid.config(text="Amount Paid For Treatment: " + str(discount))

# To clear entries
def clear_all():
    sick_entry.delete(0, END)
    time.delete(0, END)
    doc.delete(0, END)
    confee.delete(0, END)

def exit_program():
    return easy.destroy()

# Creating Labels

sick = Label(easy, text="Sickness Code", bg="#9eeb10")
treat = Label(easy, text="Duration Of Treatment", bg="#9eeb10")
week = Label(easy, text="Weekly/Months", bg="#9eeb10")
prac = Label(easy, text="Doctors Practice Number", bg="#9eeb10")
scan = Label(easy, text="Scan/Consultation Fee", bg="#9eeb10")
paid = Label(easy, bg="#9eeb10")

# Creating entries
sick_entry = Entry(easy, bd=1)
time = Entry(easy, bd=1, width=8)
doc = Entry(easy, bd=1)
confee = Entry(easy, bd=1)

# Creating Buttons
cancer = Radiobutton(easy, text="Cancer", variable=var, value="Cancer", bg="#9eeb10")
influenza = Radiobutton(easy, text="Influenza", variable=var, value="Influenza", bg="#9eeb10")
calculate = Button(easy, text="Calculate", command=sickness)
exit = Button(easy, text="Exit", command=exit_program)
clear = Button(easy, text="Clear", command=clear_all)


# Placing Labels
sick.place(x=40, y=50)
treat.place(x=40, y=90)
week.place(x=330, y=90)
prac.place(x=40, y=140)
scan.place(x=40, y=190)
paid.place(x=40, y=300)

# Placing entries
sick_entry.place(x=250, y=50)
time.place(x=250, y=90)
doc.place(x=250, y=140)
confee.place(x=250, y=190)

# Placing Buttons
cancer.place(x=40, y=220)
influenza.place(x=40, y=260)
calculate.place(x=40, y=350)
clear.place(x=240, y=350)
exit.place(x=400, y=350)


# Keeps program running
easy.mainloop()
