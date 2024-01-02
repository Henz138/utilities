# import tkinter as tk
from tkinter import *

root = Tk()
root.title("Cool App")
root.geometry('600x500+400+100')
root.resizable(False,False)
bgcolor = "#02333f"
fgcolor = "white"
root.config(bg=bgcolor)

#water rates
wr1 = 24.33
wr2 = 25.39
wr3 = 35.60
wr4 = 49.20
wr5 = 53.81
wr6 = 67.89
wr7 = 72.75

#sewer rates
sr1 = 12.08
sr2 = 15.29
sr3 = 17.13
sr4 = 25.42

def sewer_calc(units):
    if units <= 6:
        temp_sewer= units*0.00
    elif units <=10:
        temp_sewer= (units-6)*sr1
    elif units <=15:
        temp_sewer=(units-10)*sr2+(48.32)
    elif units <=20:
        temp_sewer=(units-15)*sr3+(124.77)
    elif units <=30:
        temp_sewer=(units-20)*sr4+(210.42)
    else:
        temp_sewer=(units-30)*sr4+(464.62)

    sewer_label.configure(text='Your sewer bill will be: R {:.2f}'.format(temp_sewer) +' (exVAT).')
    
    


def calculate():
    demand_levy= 33.97
    units = float(e.get())
    if units <= 6:
        temp_water= units*0.00
    elif units <=10:
        temp_water= (units-6)*wr1
    elif units <=15:
        temp_water=(units-10)*wr2+(97.32)
    elif units <=20:
        temp=(units-15)*wr3+(97.32+126.95)
    elif units <=30:
        temp_water=(units-20)*wr4+(97.32+126.95+178)
    elif units <=40:
        temp_water=(units-30)*wr5+(97.32+126.95+178+492)
    elif units <=50:
        temp_water=(units-40)*wr6+(97.32+126.95+178+492+538.10)
    else:
        temp_water=(units-50)*wr7+(97.32+126.95+178+492+538.10+678.9)
    
    total_water = temp_water + demand_levy

    sewer_calc(units)


    water_label.configure(text='Your water bill will be: R {:.2f}'.format(total_water) +' (exVAT) including demand levy.')
    e.delete(0, END)
    farewell_message.configure(text="Thank you for using this app. Please save water.")


my_text = Label(root, text=" Welcome to the City Of Joburg utilities calculator.",
               font=('Verdana', 14, 'bold'), bg=bgcolor, fg=fgcolor)
my_text2 = Label(root, text="Enter water consumption in kl: ", font=('verdana',12) ,bg=bgcolor, fg=fgcolor, anchor="center")


my_text.grid(row=0, column=0,padx=5,pady=25)
my_text2.grid(row=1, column=0, rowspan=3, columnspan=1,padx=10, pady=20,)

e = Entry(width=20, font=('verdana',12), justify="center", bg="white")
e.grid(row=4, column=0, padx=5, pady=20)
water_label = Label(font='Verdana', bg=bgcolor, fg=fgcolor)
sewer_label = Label(font='Verdana', bg=bgcolor, fg=fgcolor)
farewell_message = Label(font='Verdana', bg=bgcolor, fg=fgcolor)

calc_button= Button(text="OK", font=("verdana",12), cursor="hand2", command=calculate)
calc_button.grid(row=5, column=0, pady=15)
water_label.grid(row=8, column=0, padx=5, pady=0)
sewer_label.grid(row=9, column=0, padx=5, pady=0)
farewell_message.grid(row=15, column=0, padx=5, pady=45)

'''
image1 = PhotoImage(file="Water-DropsPNG.png")
my_img =Label(image=image1)
my_img.place(x=400, y=20)
''' 

root.mainloop()
