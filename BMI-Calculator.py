# Imports all from Tkinter GUI Package
from tkinter import *

# Initialization
app = Tk()
ma = IntVar(None)
he = IntVar(None)
b = IntVar(None)


# Calculates Body Mass Index (BMI) with user inputs, then put the user in one of four categories
# Also check if the values entered are not zero

def calculate_bmi():
    try:
        bmi = float(mass.get()) / (float(height.get()) * float(height.get()))
        b.set(bmi)
    except ZeroDivisionError:
        ma.set(None)
        he.set(None)
        b.set(None)
        return
    if bmi < 18.5:
        resLabelText.set("you are categorised as Underweight")
    if 18.5 < bmi < 24.9:
        resLabelText.set("you are categorised as Normal")
    if 25 < bmi < 29.9:
        resLabelText.set("you are categorised as Overweight")
    if bmi > 30:
        resLabelText.set("you are categorised as Obese")
    return

########################### Graphical User Interface (Tkinter) ###########################################

#  Sets size and title 
app.geometry("350x200+100+100")
app.title("BMI Calculator")

# Label and test box for mass in kg
mLabelText = StringVar()
mLabelText.set("Enter your weight in kg: ")
massLabel = Label(app, textvariable=mLabelText)
massLabel.pack()

mass = Entry(app, textvariable=ma)
mass.pack()

# Label and text box for height
hLabelText = StringVar()
hLabelText.set("Enter your height in meter: ")
heightLabel = Label(app, textvariable=hLabelText)
heightLabel.pack()

height = Entry(app, textvariable=he)
height.pack()

# Button and label and textbox for BMI calculation
button = Button(app, text="Calculate BMI", command=calculate_bmi)
button.pack(padx=15, pady=15)
bmiLabelText = StringVar()
bmiLabelText.set("Your BMI is: ")
bmiLabel = Label(app, textvariable=bmiLabelText)
bmiLabel.pack()

bmi = Entry(app, textvariable=b)
bmi.pack()
resLabelText = StringVar()
resLabelText.set(" you are categorised as: ")
resLabel = Label(app, textvariable=resLabelText)
resLabel.pack()

# Starts the GUI 
app.mainloop()