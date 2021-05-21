from tkinter import *
from tkinter import messagebox

easy = Tk()
easy.geometry("500x500")
easy.title("Medical Practice")
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

    if var.get() == "Influenza": # Calculating Influenza
        if int(confee.get()) >= 600:
            influ_answer = 350.50 + int(confee.get())
            paid.config(text="Amount Paid For Treatment: " + str(influ_answer))
        elif int(confee.get()) < 600:
            influ_answer = 350.50 + int(confee.get())
            discount = (influ_answer * (2/100)) + influ_answer # Discount
            messagebox.showinfo("Message", "2% discount")
            paid.config(text="Amount Paid For Treatment: "  + str(discount)) #Discount will be included

# To clear entries
def clear_all():
    sick_entry.delete(0, END)
    time.delete(0, END)
    doc.delete(0, END)
    confee.delete(0, END)

# Creating Labels and Entries

sick = Label(easy, text="Sickness Code")
sick_entry = Entry(easy, bd=1)
treat = Label(easy, text="Duration Of Treatment")
week = Label(easy, text="Weekly/Months")
time = Entry(easy, bd=1, width=8)
prac = Label(easy, text="Doctors Practice Number")
doc = Entry(easy, bd=1)
scan = Label(easy, text="Scan/Consultation Fee")
confee = Entry(easy, bd=1)
paid = Label(easy)



# Creating Buttons
cancer = Radiobutton(easy, text="Cancer", variable=var, value="Cancer")
influenza = Radiobutton(easy, text="Influenza", variable=var, value="Influenza")
calculate = Button(easy, text="Calculate", command=sickness)

clear = Button(easy, text="Clear", command=clear_all)


# Placing Labels, Entries and Buttons
sick.place(x=40, y=50)
sick_entry.place(x=250, y=50)
treat.place(x=40, y=90)
week.place(x=330, y=90)
time.place(x=250, y=90)
prac.place(x=40, y=140)
doc.place(x=250, y=140)
scan.place(x=40, y=190)
confee.place(x=250, y=190)
paid.place(x=40, y=300)
cancer.place(x=40, y=220)
influenza.place(x=40, y=260)
calculate.place(x=40, y=350)
clear.place(x=200, y=350)


# Keeps program running
easy.mainloop()
