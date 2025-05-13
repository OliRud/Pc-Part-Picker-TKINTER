import tkinter as tk
from tkinter import ttk
import csv

#loading the data
def load_data():
    with open("Parts list.csv", "r") as f:
        file = csv.reader(f)
        for row in file:
            file_data.append(row)
    
    #select the parts for each catagory
    for row in file_data:
        match row[0]:
            case "CPU":
                data["cpu_parts"].append(row)
            case "GPU":
                data["gpu_parts"].append(row)
            case "RAM":
                data["ram_parts"].append(row)
            case "POWER":
                data["power_parts"].append(row)
            case "HDD":
                data["hdd_parts"].append(row)
            case "SSD":
                data["ssd_parts"].append(row)
    
    print(data["gpu_parts"])

def update_list():
    pass



file_data = []

data = {
    "cpu_parts":[],
    "gpu_parts":[],
    "ram_parts":[],
    "power_parts":[],
    "hdd_parts":[],
    "ssd_parts":[]
}



#MAIN

load_data()

#set up the main window
root = tk.Tk()
root.geometry("700x550")
root.config(background="#a2faa3")
root.title("Pc Store Program")

#Title
message_label = tk.Label(root,text="Oli Rud's PC Part Picker",font=("Arial",22),bg="#a2faa3")
message_label.place(x=10, y=10)


#configuring ttk style
s = ttk.Style()
s.theme_use('winnative')
s.configure("TNotebook",background = "#70a094")
s.configure('TNotebook.Tab', background="#92c9b1")
s.map("TNotebook", background= [("selected", "green3")])


#make the tabbed notebook
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control, height=320,) #add a tab to the notebook
tab2 = ttk.Frame(tab_control, width=440, height=320)
tab3 = ttk.Frame(tab_control, width=440, height=320)
tab4 = ttk.Frame(tab_control, width=440, height=320)
tab5 = ttk.Frame(tab_control, width=440, height=320)
tab5 = ttk.Frame(tab_control, width=440, height=320)
tab6 = ttk.Frame(tab_control, width=440, height=320)
tab_control.add(tab1, text="CPU") 
tab_control.add(tab2, text="GPU")
tab_control.add(tab3, text="RAM")
tab_control.add(tab4, text="POWER")
tab_control.add(tab5, text="HDD")
tab_control.add(tab6, text="SSD")
tab_control.place(x=10, y=60)

#cart list
list = tk.Listbox(root, height = 18, 
                  width = 20, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")

list.place(x = 480,y = 60)

#price
message_label = tk.Label(root,text="Your total cost is:",font=("Arial",22),bg="#a2faa3")
message_label.place(x=10, y=410)

#checkout
checkout_button = tk.Button(root, text= "Checkout",font=("Arial",22),bg="#92c9b1")
checkout_button.place(x = 10, y = 460)




#tab contents
for index in data:
    if index == "cpu_parts":
        for part in data[index]:
            CPUListBox = tk.Checkbutton(tab1,text = part[1] + "        $"+part[2], variable = part,)
            CPUListBox.pack(anchor=tk.W)


root.mainloop()
