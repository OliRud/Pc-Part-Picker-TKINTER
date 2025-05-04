
import tkinter as tk
import csv

#load in the csv and store in data
data = []
with open("testing\Parts.csv", "r") as f:
    file = csv.reader(f)
    for row in file:
        data.append(row)

#loop over the data and add all the 'CPU' parts to the cpu list
cpu_list = []
for row in data:
    if row[0] == "CPU":
        cpu_list.append(row)



#set up the main window
root = tk.Tk()
root.geometry("700x500")



cpu_list_name = [] 
for row in cpu_list:
    cpu_list_name.append(row[1])
cpu_value = tk.StringVar(root) #track the choice
cpu_value.set("Please choose a cpu")
cpu_menu = tk.OptionMenu(root,cpu_value,*cpu_list)
cpu_menu.place(x = 100, y=50)

#must be at the end of your code
root.mainloop()