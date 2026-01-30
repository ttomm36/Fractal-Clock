import datetime
import numpy as np
from tkinter import *

class Clock(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Multi-Split Fractal Clock")
        
        # UI Elements
        controls = Frame(master)
        controls.grid(row=0, column=0, padx=10, pady=10)

        Label(controls, text="Recursion Depth").grid(row=0, column=0)
        self.depth_input = Entry(controls)
        self.depth_input.insert(0, "4")
        self.depth_input.grid(row=0, column=1)

        Label(controls, text="Number of Splits").grid(row=1, column=0)
        self.splits_input = Entry(controls)
        self.splits_input.insert(0, "3") # Try 3 or 4!
        self.splits_input.grid(row=1, column=1)

        Label(controls, text="Branch Spread (Deg)").grid(row=2, column=0)
        self.degrees_input = Entry(controls)
        self.degrees_input.insert(0, "60")
        self.degrees_input.grid(row=2, column=1)

        Label(controls, text="Length Ratio").grid(row=3, column=0)
        self.ratio_input = Entry(controls)
        self.ratio_input.insert(0, "0.6")
        self.ratio_input.grid(row=3, column=1)

        self.button = Button(controls, text="Start/Update Clock", command=self.update_clock)
        self.button.grid(row=4, column=0, columnspan=2, pady=10)

        self.canvas = Canvas(master, width=800, height=800, bg='white')
        self.canvas.grid(row=0, column=1)

    def create_fractal_line(self, x, y, length, angle, iteration, depth, ratio, spread, splits, color):
        if iteration >= depth or length < 2:
            return

        rad = np.radians(angle - 90)
        end_x = x + length * np.cos(rad)
        end_y = y + length * np.sin(rad)

        self.canvas.create_line(x, y, end_x, end_y, fill=color, width=max(1, depth-iteration))

        if splits > 1:
            # Calculate the angle between each new branch
            start_angle = angle - (spread / 2)
            step = spread / (splits - 1)
            
            for i in range(splits):
                new_angle = start_angle + (i * step)
                self.create_fractal_line(end_x, end_y, length * ratio, new_angle, 
                                         iteration + 1, depth, ratio, spread, splits, color)
        else:
            # If only 1 split, just go straight
            self.create_fractal_line(end_x, end_y, length * ratio, angle, 
                                     iteration + 1, depth, ratio, spread, splits, color)

    def update_clock(self):
        self.canvas.delete("all")
        
        try:
            depth = int(self.depth_input.get())
            ratio = float(self.ratio_input.get())
            spread = float(self.degrees_input.get())
            splits = int(self.splits_input.get())
        except ValueError:
            return 

        cx, cy = 400, 400
        now = datetime.datetime.now()
        
        # Smooth angles (includes fractional movements)
        s_angle = (now.second * 6) + (now.microsecond / 1000000.0 * 6)
        m_angle = (now.minute * 6) + (now.second * 0.1)
        h_angle = (now.hour % 12 * 30) + (now.minute * 0.5)

        # Draw Hands
        # Note: Higher splits + high depth = very slow. Be careful!
        self.create_fractal_line(cx, cy, 100, h_angle, 0, depth, ratio, spread, splits, "black")
        self.create_fractal_line(cx, cy, 130, m_angle, 0, depth, ratio, spread, splits, "blue")
        self.create_fractal_line(cx, cy, 160, s_angle, 0, depth - 1, ratio, spread, splits, "red")

        # Refresh faster for smooth motion (50ms = 20fps)
        self.master.after(50, self.update_clock)

if __name__ == "__main__":
    root = Tk()
    clock = Clock(root)
    root.mainloop()