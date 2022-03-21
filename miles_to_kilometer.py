from tkinter import *

window = Tk()
window.title("miles to kilometer converter")


def miles_to_kilometer():
    miles = float(miles_value_entry.get())
    kilometer = 1.6 * miles
    kilometer_value_label.config(text=f"{kilometer}")


miles_label = Label(text="miles : ")
miles_label.grid(column=0, row=0)

miles_unit_label = Label(text="miles")
miles_unit_label.grid(column=2, row=0)

kilometer_label = Label(text="kilometers : ")
kilometer_label.grid(column=0, row=1)

kilometer_unit_label = Label(text="kilometers")
kilometer_unit_label.grid(column=2, row=1)

miles_value_entry = Entry(width=10)
miles_value_entry.grid(column=1, row=0)

kilometer_value_label = Label(text="0")
kilometer_value_label.grid(column=1, row=1)

calculate_button = Button(text="calculate", command=miles_to_kilometer)
calculate_button.grid(column=1, row=2)

window.mainloop()
