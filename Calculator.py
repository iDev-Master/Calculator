
# ========================= Calculator

from tkinter import *

# Notes: Method 2) when pressing equal button, show the number and delete it from memory... Next time the app will read from the screen and will make correct calculation.

# # ---------------------------------------------------- All functions
tk = Tk()
tk.title("A Simple calculator")

# # -------- Buttons
def b1(): entry_screen.insert(END, 1)
def b2(): entry_screen.insert(END, 2)
def b3(): entry_screen.insert(END, 3)
def b4(): entry_screen.insert(END, 4)
def b5(): entry_screen.insert(END, 5)
def b6(): entry_screen.insert(END, 6)
def b7(): entry_screen.insert(END, 7)
def b8(): entry_screen.insert(END, 8)
def b9(): entry_screen.insert(END, 9)
def b0(): entry_screen.insert(END, 0)
def bdot(): 
   floating_point = entry_screen.get()
   dots = floating_point.count(".")
   if dots == 0:
      entry_screen.insert(END, ".")
      # buttondot["state"] = DISABLED


# # -------- Operations: addition, subtraction, multiplication and division

final_result = 0
operator = 0 # operation saves the last arithmetical operation such as addition, subtraction, division and multiplication (so when you press on the Equal button, it will calculate the last number as well).

def backspace():
   length = len(entry_screen.get())
   entry_screen.delete(length-1, END)

def operation(O):
   global first_number
   first_number = float(entry_screen.get())
   entry_screen.delete(0, END)
   global final_result
   global operator

   if operator == 0:
      final_result += first_number
      operator = O
      print(f"first number added, the result is: {final_result}, {operator}")
   elif O == "addition":
      final_result += first_number
      operator = "addition"
      print(f"added, the result is {final_result}, {operator}")
   elif O == "subtraction":
      final_result -= first_number
      operator = "subtraction"
      print(f"subtracted, the result is {final_result}, {operator}")
   elif O == "division":
      if int(first_number) == 0:
         final_result = "Error. A number can't be devided by Zero!"
      else:
         final_result /= first_number
         operator = "division"
         print(f"divided, the result is {final_result}, {operator}")
   elif O == "multiplication":
      final_result *= first_number
      operator = "multiplication"
      print(f"multiplied, the result is {final_result}, {operator}")


def bequal():
   global operator
   global final_result
   operation(operator)
   entry_screen.delete(0, END)
   if final_result == int(final_result): # if the answer is a whole number, delete ".0" from the answer.
      final_result = int(final_result)
   entry_screen.insert(0, final_result)

   # So when you press equal to see the result and then you press an arithmetical operator in order to contiue calculation, 
   # the answer will be correct (not doubled). because othervise the answer is showen in the display will be added 
   # to the result second time.
   if final_result > 0:
      final_result -= final_result  
   elif final_result < 0:
      final_result += final_result
   operator = 0 # to make correct calculation (operation) from the beggining


def clear(): 
   entry_screen.delete(0, END)
   global final_result
   final_result = 0
   global operator
   operator = 0
   print(f"cleared, the result is: {final_result}, {operator}")



# # ---------------------------------------------------- GUI interface of the app
entry_screen = Entry(tk, width=58, borderwidth=5)
entry_screen.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

button_clear = Button(tk, text='Clear', padx=126, pady=20, command=clear).grid(row = 1, column = 0, columnspan=3)
button1 = Button(tk, text='<-', padx=36, pady=20, command=backspace).grid(row = 1, column = 4)

button1 = Button(tk, text='1', padx=40, pady=20, command=b1).grid(row = 2, column = 0)
button2 = Button(tk, text='2', padx=40, pady=20, command=b2).grid(row = 2, column = 1)
button3 = Button(tk, text='3', padx=40, pady=20, command=b3).grid(row = 2, column = 2)
button4 = Button(tk, text='4', padx=40, pady=20, command=b4).grid(row = 3, column = 0)
button5 = Button(tk, text='5', padx=40, pady=20, command=b5).grid(row = 3, column = 1)
button6 = Button(tk, text='6', padx=40, pady=20, command=b6).grid(row = 3, column = 2)
button7 = Button(tk, text='7', padx=40, pady=20, command=b7).grid(row = 4, column = 0)
button8 = Button(tk, text='8', padx=40, pady=20, command=b8).grid(row = 4, column = 1)
button9 = Button(tk, text='9', padx=40, pady=20, command=b9).grid(row = 4, column = 2)

buttondot = Button(tk, text='.', padx=41, pady=20, command=bdot).grid(row = 5, column = 0)
button0 = Button(tk, text='0', padx=40, pady=20, command=b0).grid(row = 5, column = 1)
buttonequal = Button(tk, text='=', padx=39, pady=20, command=bequal).grid(row = 5, column = 2)

buttonDiv = Button(tk, text='/', padx=40, pady=20, command=lambda:operation('division')).grid(row = 2, column = 4)
buttonMult = Button(tk, text='*', padx=40, pady=20, command=lambda:operation('multiplication')).grid(row = 3, column = 4)
buttonMinus = Button(tk, text='-', padx=40, pady=20, command=lambda:operation('subtraction')).grid(row = 4, column = 4)
buttonPlus = Button(tk, text='+', padx=39, pady=20, command=lambda:operation('addition')).grid(row = 5, column = 4)

tk.mainloop()










# ================ Calculator. first vertion 
# from tkinter import *

# # NOTES: Method 1) variable viklichatel. if = was pressed, Vikl, if operator was pressed, then Vikl is off
# # Method 2) when pressing equal button, show the number and delete it from memory... 

# # # ---------------------------------------------------- All functions
# tk = Tk()
# tk.title("Simple calculator")



# def b1(): e.insert(END, 1)
# def b2(): e.insert(END, 2)
# def b3(): e.insert(END, 3)
# def b4(): e.insert(END, 4)
# def b5(): e.insert(END, 5)
# def b6(): e.insert(END, 6)
# def b7(): e.insert(END, 7)
# def b8(): e.insert(END, 8)
# def b9(): e.insert(END, 9)
# def b0(): e.insert(END, 0)
# def bdot(): e.insert(END, ".")


# final_result = 0
# operation = -1 # operation saves the last operation. 1 is addition, 2 is subtraction, 3 is division and 4  is multiplication.


# def addition():
#    global first_number
#    first_number = float(e.get())
#    e.delete(0, END)
#    global final_result
#    final_result += first_number
#    global operation
#    if operation != "addition":
#       operation = "addition"


# def subtraction():
#    global first_number
#    first_number = float(e.get())
#    e.delete(0, END)
#    global final_result
#    final_result -= first_number
#    global operation
#    if operation != "subtraction":
#       operation = "subtraction"


# def division():
#    global first_number
#    first_number = float(e.get())
#    e.delete(0, END)
#    global final_result
#    if final_result != 0:
#       final_result /= first_number
#    else:
#       final_result = first_number
#    global operation
#    if operation != "division":
#       operation = "division"


# def multiplication():
#    global first_number
#    first_number = float(e.get())
#    e.delete(0, END)
#    global final_result
#    if final_result != 0:
#       final_result *= first_number
#    else:
#       final_result = first_number
#    global operation
#    if operation != "multiplication":
#       operation = "multiplication"

# def bequal():
#    last_number = float(e.get())
   
#    if operation == "addition":
#       global final_result
#       final_result += last_number
#       e.delete(0, END)
#       e.insert(0, final_result)
   
#    if operation == "subtraction":
#       final_result -= last_number
#       e.delete(0, END)
#       e.insert(0, final_result)

#    elif operation == "division":
#       final_result /= last_number
#       e.delete(0, END)
#       e.insert(0, final_result)

#    elif operation == "multiplication":
#       final_result *= last_number
#       e.delete(0, END)
#       e.insert(0, final_result)


# def clear(): 
#    e.delete(0, END)
#    global final_result
#    final_result = 0





# # def addition():
# #    global first_number
# #    first_number = float(e.get())
# #    e.delete(0,END)


# # def bequal():
# #    global second_number
# #    second_number = float(e.get())
# #    e.delete(0, END)
# #    e.insert(0, first_number + second_number)






# # def addition():
# #    screenclearing()
# #    global final_result
# #    final_result += N
# #    global operation
# #    if operation != "add":
# #       operation = "add"

# # def last_addition():
# #    pass

# # def bequal():
# #    if operation == "add":
# #       addition()
# #    e.delete(0, END)
# #    e.insert(0, final_result)



# # # ---------------------------------------------------- GUI interface of the app
# e = Entry(tk, width=58, borderwidth=5)
# e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# button_clear = Button(tk, text='Clear', padx=171, pady=20, command=clear)
# button_clear.grid(row = 1, column = 0, columnspan=5)
# button1 = Button(tk, text='1', padx=40, pady=20, command=b1)
# button1.grid(row = 2, column = 0)
# button2 = Button(tk, text='2', padx=40, pady=20, command=b2)
# button2.grid(row = 2, column = 1)
# button3 = Button(tk, text='3', padx=40, pady=20, command=b3)
# button3.grid(row = 2, column = 2)
# button4 = Button(tk, text='4', padx=40, pady=20, command=b4)
# button4.grid(row = 3, column = 0)
# button5 = Button(tk, text='5', padx=40, pady=20, command=b5)
# button5.grid(row = 3, column = 1)
# button6 = Button(tk, text='6', padx=40, pady=20, command=b6)
# button6.grid(row = 3, column = 2)
# button7 = Button(tk, text='7', padx=40, pady=20, command=b7)
# button7.grid(row = 4, column = 0)
# button8 = Button(tk, text='8', padx=40, pady=20, command=b8)
# button8.grid(row = 4, column = 1)
# button9 = Button(tk, text='9', padx=40, pady=20, command=b9)
# button9.grid(row = 4, column = 2)
# buttondot = Button(tk, text='.', padx=41, pady=20, command=bdot).grid(ro
# buttondotw = 5, column = 0)
# button0 = Button(tk, text='0', padx=40, pady=20, command=b0)
# button0.grid(row = 5, column = 1)

# buttonequal = Button(tk, text='=', padx=39, pady=20, command=bequal)
# buttonequal.grid(row = 5, column = 2)
# buttonPlus = Button(tk, text='/', padx=40, pady=20, command=division)
# buttonPlus.grid(row = 2, column = 4)
# buttonPlus = Button(tk, text='*', padx=40, pady=20, command=multiplication)
# buttonPlus.grid(row = 3, column = 4)
# buttonPlus = Button(tk, text='-', padx=40, pady=20, command=subtraction)
# buttonPlus.grid(row = 4, column = 4)
# buttonPlus = Button(tk, text='+', padx=39, pady=20, command=addition)
# buttonPlus.grid(row = 5, column = 4)


# tk.mainloop()
