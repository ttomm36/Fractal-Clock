# Degrees
# Ratio
# Number of splits

import datetime
import numpy as np
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
        while True:
            self.clear_all_inside_frame()
            canv = Canvas(self.master)
            canv.pack()
            time = datetime.datetime.now().time()
            y_center = np.floor(canv.winfo_reqheight()/2)
            x_center = np.floor(canv.winfo_reqwidth()/2)

            start_x = x_center
            start_y = y_center - np.floor(y_center/2)

            # Hour hand
            angle = np.radians((360 / 12)*time.hour + (360 / 12/600)*time.minute)
            newx = ((start_x-x_center)*np.cos(angle)-(start_y-y_center)*np.sin(angle)) + x_center
            newy = ((start_x-x_center)*np.sin(angle)+(start_y-y_center)*np.cos(angle)) + y_center
            canv.create_line(x_center,y_center,newx,newy, fill= 'black')

            # Minute hand
            start_y = y_center - np.floor(y_center/3)
            angle = np.radians((360 / 60)*time.minute)
            newx = ((start_x-x_center)*np.cos(angle)-(start_y-y_center)*np.sin(angle)) + x_center
            newy = ((start_x-x_center)*np.sin(angle)+(start_y-y_center)*np.cos(angle)) + y_center
            canv.create_line(x_center,y_center,newx,newy, fill= 'blue')

            # Minute hand
            start_y = y_center - np.floor(y_center)
            angle = np.radians((360 / 60)*time.second)
            newx = ((start_x-x_center)*np.cos(angle)-(start_y-y_center)*np.sin(angle)) + x_center
            newy = ((start_x-x_center)*np.sin(angle)+(start_y-y_center)*np.cos(angle)) + y_center
            canv.create_line(x_center,y_center,newx,newy, fill= 'blue')


            self.master.update()

    def clear_all_inside_frame(self):

        for widget in self.master.winfo_children():
            widget.destroy()


if __name__== "__main__":
    clock = Clock()
    clock.mainloop()