import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Label, Listbox
from stackoverflow_api import get_params, open_new_pages, save_current_to_file, save_web_pages


def help_window():
    root = tk.Tk()
    help = Help_window(master=root)
    help.mainloop()
    root.destroy()


def entry_to_params_to_(entry1, entry2, entry3, listbox: tk.Text):
    parameters = get_params(entry1.get(), entry2.get(), entry3.get())
    questions = save_web_pages(parameters)

    with open("temp_pages.txt", "w", encoding="UTF-8") as file:
        for question in questions["items"]:
            file.write(question["link"]+"\n")
    with open("temp_pages.txt", "r", encoding="UTF-8") as file:
        listbox.delete('1.0', tk.END)
        text = file.readlines()
        for t in text:
            listbox.insert(tk.END, t)


class Help_window(tk.Frame):
    def createWidgets(self, master):
        text_var = tk.StringVar(master)
        self.help_label = tk.Label(master,  textvariable=text_var)
        with open("readme.txt", "r", encoding="UTF-8") as file:
            text_var.set(file.read())

        self.help_label.grid(row=0, column=0)

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets(master)


class Main_window(tk.Frame):

    def createWidgets(self, master):

        ## background ##
        self.background_image = tk.Canvas(master,  borderwidth=0)
        self.image = ImageTk.PhotoImage(Image.open("stack-overflow3.png"))
        self.background_image.create_image(2, 2, image=self.image, anchor='nw')
        self.background_image.grid(row=0, column=0)

        ## Create Menu Bar ##
        self.menu_bar = tk.Menu()
        self.menu_bar.add_command(label="Help", command=help_window)
        self.menu_bar.add_command(label="Quit", command=master.quit)
        master.config(menu=self.menu_bar)

        ## label_name_pages ##

        self.page_label = tk.Label(
            self.background_image, text="Links to StackOverFlow pages", font="Times, 12", borderwidth=1, width=30, height=3, relief='groove').grid(row=0, column=2, columnspan=2, pady=10)

        self.intro_label = tk.Label(
            self.background_image, text="Welcome to StackOverFlow \ntag prospector", font="Times, 16", borderwidth=1, width=30, height=3, relief='groove').grid(row=0, column=0, columnspan=2, pady=10, padx=5)

        ## listbox for links ##
        self.listbox_links = tk.Text(
            self.background_image, width=36, height=20, relief='groove', borderwidth=1)
        self.listbox_links.grid(
            row=2, column=2, columnspan=2, rowspan=5, pady=5, padx=5)

        ## entry widget for tags/upvotes/responses ##
        self.entry_widget_tags = tk.Entry(
            self.background_image, width=30, font="Times, 14", justify='center')
        self.entry_widget_tags.insert(0, "Insert tag")
        self.entry_widget_tags.grid(row=2, column=0, padx=10, columnspan=2)

        self.entry_widget_upvotes = tk.Entry(
            self.background_image, font="Times, 13", justify='center')
        self.entry_widget_upvotes.insert(0, "How many upvotes")
        self.entry_widget_upvotes.grid(row=3, column=0, padx=5)

        self.entry_widget_days = tk.Entry(
            self.background_image, font="Times, 13", justify='center')
        self.entry_widget_days.insert(0, "From how long ago (days)")
        self.entry_widget_days.grid(row=3, column=1, padx=5)

        ## save / open / search buttons ##

        self.save_button = tk.Button(
            self.background_image, text="Save to txt file", width=19, command=lambda: save_current_to_file()).grid(row=1, column=2, pady=3)

        self.open_button = tk.Button(
            self.background_image, text="Open pages in web", width=19, command=lambda: open_new_pages()).grid(row=1, column=3, padx=1, pady=3)

        self.search_button = tk.Button(
            self.background_image, text="Search", font="Times, 18", command=lambda: entry_to_params_to_(self.entry_widget_days, self.entry_widget_upvotes, self.entry_widget_tags, self.listbox_links)).grid(row=4, column=0, columnspan=2)

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets(master)
