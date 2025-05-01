import tkinter as tk
from tkinter import ttk

#set up the main window
root = tk.Tk()
root.geometry("700x500")
root.config(background="#ffeecc")
root.title("Pc Store Program")


#configuring ttk style
s = ttk.Style()
s.theme_use('winnative')
s.configure("TNotebook",background = "#15788c")
s.configure('TNotebook.Tab', background="#00b9be")
s.map("TNotebook", background= [("selected", "green3")])


#make the tabbed notebook
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control, height=320,) #add a tab to the notebook
tab2 = ttk.Frame(tab_control, width=440, height=320)
tab_control.add(tab1, text="CPU",) 
tab_control.add(tab2, text="GPU") 
tab_control.place(x=10, y=10)

#cart list
list = tk.Listbox(root, height = 17, 
                  width = 20, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")

list.place(x = 480,y = 30)

#price
message_label = tk.Label(root,text="Your total cost is:",font=("Arial",22),bg="#ffeecc")
message_label.place(x=10, y=370)

#checkout
checkout_button = tk.Button(root, text= "Checkout",font=("Arial",22),bg="#53b415")
checkout_button.place(x = 10, y = 420)


root.mainloop()