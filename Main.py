import tkinter as tk
from tkinter import ttk, messagebox
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


def update_list(part,cst):
    overall_cost = 0
    
    ##listbox
    try:
        #if it already exists within the array, remove it
        cart.remove(part)
    except:
        cart.append(part)
    
    print(cart)

    lb_contents.set(cart)

    ##cost
    try:
        cost.remove(float(cst))
    except:
        cost.append(float(cst))
    
    for item in cost:
        overall_cost += item
    
    pricetag.set("$"+str(overall_cost))
    
    
def process_order():
    messagebox.showinfo("Success :D","Order processed, thankyou for choosing Oli Rud's Pc Part Picker.")

    
    

file_data = []

data = {
    "cpu_parts":[],
    "gpu_parts":[],
    "ram_parts":[],
    "power_parts":[],
    "hdd_parts":[],
    "ssd_parts":[]
}

cart = []


cost = []

#MAIN

load_data()

#set up the main window
root = tk.Tk()
root.geometry("450x430")
root.config(background="#a2faa3")
root.title("Pc Store Program")

lb_contents = tk.StringVar(value=[])
pricetag = tk.StringVar(value="$0.00")

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
tab1 = ttk.Frame(tab_control, height=320) #add a tab to the notebook
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
                  listvariable=lb_contents,
                  selectmode=tk.MULTIPLE,
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")

list.place(x = 260,y = 60)

#price
message_label = tk.Label(root,textvariable=pricetag,font=("Arial",22),bg="#a2faa3")
message_label.place(x=10, y=280)

#checkout
checkout_button = tk.Button(root, text= "Checkout",font=("Arial",22),bg="#92c9b1",command=process_order)
checkout_button.place(x = 10, y = 345)




#tab contents
for index in data:
    if index == "cpu_parts":
        for part in data[index]:
            partname = part[1]
            CPUListBox = tk.Checkbutton(tab1,text = part[1] + "        $"+part[2], variable=part[1], command=lambda partname = part[1], cost = part[2]: update_list(partname,cost))
            CPUListBox.pack(anchor=tk.W)
    if index == "gpu_parts":
        for part in data[index]:
            GPUListBox = tk.Checkbutton(tab2,text = part[1] + "        $"+part[2], variable = part, command=lambda partname = part[1], cost = part[2]: update_list(partname,cost))
            GPUListBox.pack(anchor=tk.W)
    if index == "ram_parts":
        for part in data[index]:
            RAMListBox = tk.Checkbutton(tab3,text = part[1] + "        $"+part[2], variable = part, command=lambda partname = part[1], cost = part[2]: update_list(partname,cost))
            RAMListBox.pack(anchor=tk.W)
    if index == "power_parts":
        for part in data[index]:
            PowerListBox = tk.Checkbutton(tab4,text = part[1] + "        $"+part[2], variable = part, command=lambda partname = part[1], cost = part[2]: update_list(partname,cost))
            PowerListBox.pack(anchor=tk.W)
    if index == "hdd_parts":
        for part in data[index]:
            HDDListBox = tk.Checkbutton(tab5,text = part[1] + "        $"+part[2], variable = part, command=lambda partname = part[1], cost = part[2]: update_list(partname,cost))
            HDDListBox.pack(anchor=tk.W)
    if index == "ssd_parts":
        for part in data[index]:
            SDDListBox = tk.Checkbutton(tab6,text = part[1] + "        $"+part[2], variable = part, command=lambda partname = part[1], cost = part[2]: update_list(partname,cost))
            SDDListBox.pack(anchor=tk.W)


root.mainloop()
