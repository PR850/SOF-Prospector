import core
import tkinter as tk
import stackoverflow_api


root = tk.Tk()
root.title("StackOverFlow Tag Prospector")
root.resizable(False, False)

app = core.Main_window(master=root)

app.mainloop()


root.destroy()
