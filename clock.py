import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

root = tk.Tk()
root.title("专注时钟")
root.attributes('-topmost', True)
root.geometry('200x100')

clock_label = tk.Label(root, font=('Helvetica', 48))
clock_label.pack(expand=True)

update_clock()

root.mainloop()
