import tkinter as tk

root = tk.Tk()
root.title("Kalkulator")
root.resizable(False, False)
root.config(background = "gray11")
root.geometry("453x400")

def guzik(text, row, column):
    button = tk.Button(root, text = text, width = 5, height = 2, font=("Courier", 16), background = "gray42", bd = 5, command = lambda: klik(text))
    button.grid(row = row, column = column, padx = 5, pady = 5)

def guzik_jasny(text, row, column):
    button = tk.Button(root, text = text, width = 5, height = 2, font=("Courier", 16), background = "gray75", bd = 5, command = lambda: klik(text))
    button.grid(row = row, column = column, padx = 5, pady = 5)

def guzik_rownasie(text, row, column):
    button = tk.Button(root, text = text, width = 19, height = 2, font=("Courier", 16), background = "pale green", bd = 5, command = lambda: klik(text))
    button.grid(row = row, column = column, columnspan = 3, padx = 5, pady = 5)
        
def guzik_del(text, row, column):
    button = tk.Button(root, text = text, width = 5, height = 2, font=("Courier", 16), background = "brown2", bd = 5, command = lambda: klik(text))
    button.grid(row = row, column = column, padx = 5, pady = 5)

def guzik_reset(text, row, column):
    button = tk.Button(root, text = text, width = 5, height = 2, font=("Courier", 16), background = "tomato", bd = 5, command = lambda: klik(text))
    button.grid(row = row, column = column, padx = 5, pady = 5)
        
def klik(text):
    if text == "=":
        try:
            result = str(eval(output.get()))
            output.delete(0, tk.END)
            output.insert(0, result)
        except:
            output.delete(0, tk.END)
            output.insert(0, "Błąd")
    elif text == "⌫":
        output.delete(len(output.get())-1, tk.END)
    elif text == "CE":
        output.delete(0, tk.END)
    else:
        output.insert(tk.END, text)
       
        

output = tk.Entry(width = 25, justify = "right", font = ("Courier", 22), background = "DarkOliveGreen4", foreground = "black")
output.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 15)
guzik("1", 1, 0)
guzik("2", 1, 1)
guzik("3", 1, 2)
guzik("4", 2, 0)
guzik("5", 2, 1)
guzik("6", 2, 2)
guzik("7", 3, 0)
guzik("8", 3, 1)
guzik("9", 3, 2)
guzik("0", 4, 1)
guzik_rownasie("=", 4, 2)
guzik_del("⌫", 1, 4)
guzik_reset("CE", 4, 0)
guzik_jasny("+", 1, 3)
guzik_jasny("-", 2, 3)
guzik_jasny("*", 3, 3)
guzik_jasny("/", 2, 4)
guzik_jasny(".", 3, 4)



    


root.mainloop()
