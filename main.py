# Importing tkinter
import tkinter as tk
from tkinter import Label, LabelFrame, Button, Entry, END, messagebox
# defining tkinter
bmi = tk.Tk()
bmi.title("BMI Calculator")
# Defining functions
numberInput = tk.StringVar(bmi)
def bmi_actual():
    actuality = float(label_1.get()) / (float(label_2.get()) / 100)**2
    bmi_actual.set("%0.2f" % bmi_actual)

def bmi_ideal_male():
    male = float(0.5 * label_1.get() / (float(label_2.get() / 100)))**2 + 11.5
    bmi_ideal_male.set("%0.2f" % bmi_ideal_male)

def bmi_ideal_female():
    female = float(0.5 * label_1.get() / float(label_2.get()/ 100))**2 + 0.03 * float(label_3.get()) + 11
    bmi_ideal_female.set("%0.2f" % bmi_ideal_female)

def print_answers():
    print("Selected Option: {}".format(value_inside.get()))
    return None

def clear():
    label_1.delete(0, END)
    label_2.delete(0, END)
    label_3.delete(0, END)

def close():
    return bmi.destroy()

# Making the structure
label_1 = Label(bmi, text = "Height: ").grid(column=1,row=1)
entry_1 = Entry(bmi, textvariable = numberInput ).grid(column=2, row=1)
label_2 = Label(bmi, text = "Weight: ").grid(column=1,row=2)
entry_2 = Entry(bmi, textvariable = numberInput).grid(column=2,row=2)
# Making an option menu


# Finishing up the structure
label_3 = Label(bmi, text = "Age: ").grid(column=3,row=3)
entry_3 = Entry(bmi, textvariable = numberInput).grid(column=4,row=3)
button = Button(bmi, text = "Calculate Your Body Mass Index", command=lambda:[bmi_actual(), bmi_ideal_male()]).grid(column=2,row=5)
label_4 = Label(bmi, text = "BMI: ").grid(column=1,row=6)
label_5 = Label(bmi, text = "Ideal BMI: ").grid(column=3,row=6)
entry_4 = Entry(bmi, textvariable = numberInput).grid(column=2,row=6)
entry_5 = Entry(bmi, textvariable = numberInput).grid(column=4,row=6)
button_2 = Button(bmi, text = "Clear", command=clear).grid(column=1,row=7)
button_3  = Button(bmi, text = "Exit", command=close).grid(column=3,row=7)

bmi.mainloop()
