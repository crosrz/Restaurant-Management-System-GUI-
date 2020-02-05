import tkinter
import time
import random

mainWindow = tkinter.Tk()

mainWindow.title("Restaurant Management System")
mainWindow.geometry('1000x480-8-200')
text_Input = tkinter.StringVar()
operator = ""

Tops = tkinter.Frame(mainWindow)
Tops.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', expand=True)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', expand=True)

# ======================Time====================
localtime = time.asctime(time.localtime(time.time()))

# ======================System Information=================
labelInfo = tkinter.Label(Tops, font=('arial', 30, 'bold'), text="FoodMantra", fg="Steel Blue", bd=10, anchor='w')
labelInfo.grid(row=0, column=0)
labelInfo = tkinter.Label(Tops, font=('arial', 15, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
labelInfo.grid(row=1, column=0)


# ==================Calculator=====================


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


def Ref():
    x = random.randint(12908, 508763)
    randomRef = str(x)
    rand.set(randomRef)

    CoF = float(Fries.get())
    CoD = float(Drinks.get())
    CoFilet = float(Filet.get())
    CoB = float(Burger.get())
    CoC = float(Chicken.get())
    CoCheese = float(Cheese.get())

    CostofFries = CoF * 0.99
    CostofDrinks = CoD * 1
    CostofFilet = CoFilet * 2.99
    CostofBurger = CoB * 2.87
    CostofChicken = CoC * 2.35
    CostofCheese = CoCheese * 2.35

    CostofMeal = '{0} {1:.2f}'.format("$", (CostofFries + CostofDrinks + CostofFilet +
                                            CostofBurger + CostofChicken + CostofCheese))
    PayTax = ((CostofFries + CostofDrinks + CostofFilet +
               CostofBurger + CostofChicken + CostofCheese) * 0.2)
    TotalCost = (CostofFries + CostofDrinks + CostofFilet +
                 CostofBurger + CostofChicken + CostofCheese)
    Ser_Charge = ((CostofFries + CostofDrinks + CostofFilet +
                   CostofBurger + CostofChicken + CostofCheese) / 99)
    Service = '{0} {1:.2f}'.format("$", Ser_Charge)
    OverAllCost = '{0} {1:.2f}'.format("$", (PayTax + TotalCost + Ser_Charge))
    PaidTax = '{0} {1:.2f}'.format("$", PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    mainWindow.destroy()


def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    Chicken.set("")
    Cheese.set("")
    Drinks.set("")
    Cost.set("")
    Service_Charge.set("")
    Tax.set("")
    SubTotal.set("")
    Total.set("")


# ---------------------Calculator Display----------------------


txtDisplay = tkinter.Entry(rightFrame, font=('arial', 10, 'bold'), textvariable=text_Input, bd=10, insertwidth=4,
                           bg='powder blue', justify='right')
txtDisplay.grid(columnspan=4)

btn7 = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                      text="7", bg="powder blue", command=lambda: btnclick(7)).grid(row=2, column=0)
btn8 = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                      text="8", bg="powder blue", command=lambda: btnclick(8)).grid(row=2, column=1)
btn9 = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                      text="9", bg="powder blue", command=lambda: btnclick(9)).grid(row=2, column=2)
addition = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                          text="+", bg="powder blue", command=lambda: btnclick("+")).grid(row=2, column=3)

btn4 = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                      text="4", bg="powder blue", command=lambda: btnclick(4)).grid(row=3, column=0)
btn5 = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                      text="5", bg="powder blue", command=lambda: btnclick(5)).grid(row=3, column=1)
btn6 = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                      text="6", bg="powder blue", command=lambda: btnclick(6)).grid(row=3, column=2)
subtraction = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                             text="-", bg="powder blue", command=lambda: btnclick("-")).grid(row=3, column=3)

btn1 = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                      text="1", bg="powder blue", command=lambda: btnclick(1)).grid(row=4, column=0)
btn2 = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                      text="2", bg="powder blue", command=lambda: btnclick(2)).grid(row=4, column=1)
btn3 = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                      text="3", bg="powder blue", command=lambda: btnclick(3)).grid(row=4, column=2)
multiplication = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                                text="*", bg="powder blue", command=lambda: btnclick("*")).grid(row=4, column=3)

btn0 = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                      text="0", bg="powder blue", command=lambda: btnclick(0)).grid(row=5, column=0)
btnClear = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                          text="C", bg="powder blue", command=btnClearDisplay).grid(row=5, column=1)
btnEqual = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                          text="=", bg="powder blue", command=btnEqualsInput).grid(row=5, column=2)
division = tkinter.Button(rightFrame, padx=8, pady=8, bd=4, fg='black', font=('arial', 10, 'bold'),
                          text="/", bg="powder blue", command=lambda: btnclick("/")).grid(row=5, column=3)

# ---------------------------------- Restaurant Info 1 ----------------------------
rand = tkinter.StringVar()
Fries = tkinter.StringVar()
Burger = tkinter.StringVar()
Filet = tkinter.StringVar()
Chicken = tkinter.StringVar()
Cheese = tkinter.StringVar()
Drinks = tkinter.StringVar()
Cost = tkinter.StringVar()
Service_Charge = tkinter.StringVar()
Tax = tkinter.StringVar()
SubTotal = tkinter.StringVar()
Total = tkinter.StringVar()

lblReference = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0, column=0)
txtReference = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=rand, bd=10, insertwidth=4,
                             bg="powder blue", justify='right')
txtReference.grid(row=0, column=1)

lblFries = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="Fries", bd=16, anchor='w')
lblFries.grid(row=1, column=0)
txtFries = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=Fries, bd=10, insertwidth=4,
                         bg="powder blue", justify='right')
txtFries.grid(row=1, column=1)

lblBurger = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="Burger", bd=16, anchor='w')
lblBurger.grid(row=2, column=0)
txtBurger = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=Burger, bd=10, insertwidth=4,
                          bg="powder blue", justify='right')
txtBurger.grid(row=2, column=1)

lblFilet = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="Filet", bd=16, anchor='w')
lblFilet.grid(row=3, column=0)
txtFilet = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=Filet, bd=10, insertwidth=4,
                         bg="powder blue", justify='right')
txtFilet.grid(row=3, column=1)

lblChicken = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="Chicken", bd=16, anchor='w')
lblChicken.grid(row=4, column=0)
txtChicken = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=Chicken, bd=10, insertwidth=4,
                           bg="powder blue", justify='right')
txtChicken.grid(row=4, column=1)

lblCheese = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="Cheese", bd=16, anchor='w')
lblCheese.grid(row=5, column=0)
txtCheese = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=Cheese, bd=10, insertwidth=4,
                          bg="powder blue", justify='right')
txtCheese.grid(row=5, column=1)

# ---------------------------------- Restaurant Info 2 ----------------------------


lblDrinks = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=Drinks, bd=10, insertwidth=4,
                          bg="powder blue", justify='right')
txtDrinks.grid(row=0, column=3)

lblCost = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="Cost of Meal", bd=16, anchor='w')
lblCost.grid(row=1, column=2)
txtCost = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=Cost, bd=10, insertwidth=4,
                        bg="powder blue", justify='right')
txtCost.grid(row=1, column=3)

lblService = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="Service Charge", bd=16, anchor='w')
lblService.grid(row=2, column=2)
txtService = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4,
                           bg="powder blue", justify='right')
txtService.grid(row=2, column=3)

lblStateTax = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="State Tax", bd=16, anchor='w')
lblStateTax.grid(row=3, column=2)
txtStateTax = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=Tax, bd=10, insertwidth=4,
                            bg="powder blue", justify='right')
txtStateTax.grid(row=3, column=3)

lblSubTotal = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=4, column=2)
txtSubTotal = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4,
                            bg="powder blue", justify='right')
txtSubTotal.grid(row=4, column=3)

lblTotalCost = tkinter.Label(leftFrame, font=('arial', 10, 'bold'), text="Total Cost", bd=16, anchor='w')
lblTotalCost.grid(row=5, column=2)
txtTotalCost = tkinter.Entry(leftFrame, font=('arial', 7, 'bold'), textvariable=Total, bd=10, insertwidth=4,
                             bg="powder blue", justify='right')
txtTotalCost.grid(row=5, column=3)

# --------------------------Buttons-------------

btnTotal = tkinter.Button(leftFrame, padx=16, pady=8, bd=16, fg="black", font=('arial', 10, 'bold'), width=10,
                          text="Total", bg="powder blue", command=Ref).grid(row=7, column=1)

btnReset = tkinter.Button(leftFrame, padx=16, pady=8, bd=16, fg="black", font=('arial', 10, 'bold'), width=10,
                          text="Reset", bg="powder blue", command=Reset).grid(row=7, column=2)

btnExit = tkinter.Button(leftFrame, padx=16, pady=8, bd=16, fg="black", font=('arial', 10, 'bold'), width=10,
                         text="Exit", bg="powder blue", command=qExit).grid(row=7, column=3)

mainWindow.mainloop()
