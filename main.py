import tkinter as tk 
import yfinance as yf 

def center_window(root, width, height):

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("STOCK ALERT")
root.iconbitmap("stock.ico")

window_width = 400
window_height = 300

center_window(root, window_width, window_height)

root.mainloop()

