# Degrees
# Ratio
# Number of splits

import datetime
import time
from tkinter import *


class Clock(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()

        self.nr_of_splits = Entry(master)
        self.ratio = Entry(master)
        self.degrees = Entry(master)

        Label(master,text="Number of Splits",background='lightgray').grid(row=0,column=0)
        Label(master,text="Ratio",background='lightgray').grid(row=1,column=0)
        Label(master,text="degrees",background='lightgray').grid(row=2,column=0)

        self.button = Button(master,command=self.button_click,background="lightgray",text="Generate Clock")
        self.button.grid(row=3,column=0,columnspan=2)

        self.nr_of_splits.grid(row=0,column=1)
        self.ratio.grid(row=1,column=1)
        self.degrees.grid(row=2,column=1)


    def button_click(self):
        """ handle button click event and output text from entry area"""
        print("Event Triggerd")
        self.clear_all_inside_frame()
        self.create_clock()

    def create_clock(self):
        canv = Canvas(self.master)
        canv.pack()
        print(datetime.datetime.now().time())
        pass

    def clear_all_inside_frame(self):

        for widget in self.master.winfo_children():
            widget.destroy()


if __name__== "__main__":
    clock = Clock()
    clock.mainloop()