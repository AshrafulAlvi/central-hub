from tkinter import *
import inventory
import sales
import timesheet


def open_menu():

    def open_inventory_window():
        menu_window.destroy()
        inventory.open_inventory()

    def sales():
        menu_window.destroy()
        sales.open_sales()

    def timesheet():
        menu_window.destroy()
        timesheet.open_time()


    menu_window = Tk()
    menu_window.title("Main Menu")
    menu_window.config(width=800, height=600, bg="#c5fada",)

    inv_button = Button(menu_window, text="Inventory", font=("Alice",20), bg="#c5fada", activebackground="#c5fada", command=open_inventory_window)
    inv_button.place(x=140, y=200, height=80, width=160)

    sales_button = Button(menu_window, text="Sales", font=("Alice",20), bg="#c5fada", activebackground="#c5fada", command=sales )
    sales_button.place(x=320, y=200, height=80, width=160)

    time_button = Button(menu_window, text="TimeSheet", font=("Alice",20), bg="#c5fada", activebackground="#c5fada", command=timesheet )
    time_button.place(x=500, y=200, height=80, width=160)



    menu_window.mainloop()