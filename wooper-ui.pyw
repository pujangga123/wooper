import tkinter as tk
import pyautogui as py
import time
import win32gui

# refs:
# https://realpython.com/python-gui-tkinter/#getting-user-input-with-entry-widgets

def do_loop(n):
    hwnd = win32gui.FindWindow(None, "WhatsApp")
    win32gui.SetForegroundWindow(hwnd)

    # begin looping
    for i in range(0,n):
        py.hotkey('ctrl','v')
        time.sleep(1)
        py.hotkey('ctrl','shift',']')
        time.sleep(1)

def button_click():
    try:
        n = int(nloop.get())
    except:
        tk.messagebox.showerror("Invalid N value")
    finally:
        do_loop(n)


window = tk.Tk()
window.geometry("200x70")

label = tk.Label(text="n loop")
label.grid(row=0, column=0, padx=10, pady=5)

nloop = tk.Entry( width=10)
nloop.grid(row=0, column=1, padx=10, pady=5)
nloop.insert(0,"5")

button = tk.Button(text="Execute", command=button_click)
button.grid(row=1, column=1, padx=10, sticky="w")

window.mainloop()