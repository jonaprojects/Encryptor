from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import font as tkFont
from PIL import ImageTk, Image


def apply_theme(master, theme='light'):
    master.tk.call("source", "azureTheme\\azure.tcl")
    master.tk.call("set_theme", theme)


def execute_gui(gui_class, theme='light'):
    root = Tk()
    apply_theme(master=root, theme=theme)
    my_gui = gui_class(root)
    root.mainloop()


RANSOMWARE_INFO = """ We have decrypted all of your files. Any attempt to decrypt the files will lead to
a corruption of data, and therefore the files will be rendered useless. But you can still save your precious files...
"""


class RansomwareUI:
    """A ui for the ransomware program"""
    H1 = 24
    H2 = 22
    H3 = 20
    H4 = 18
    H5 = 16
    H6 = 14
    TEXT = 12

    def __init__(self, master, width=800, height=500):
        # Basic page characteristics
        self.master = master
        self.width = width
        self.height = height
        self.master.geometry(f"{self.width}x{self.height}")
        master.title("You've been hacked!")

        # overriding window behaviour for malicious purposes - might only work on windows
        try:
            self.master.protocol("WM_DELETE_WINDOW", self._close_x_command)  # the user can't close the program
            self.master.resizable(False, False)  # the user can't resize the screen
        except:
            pass

        # menu
        self.menu = Menu(master)
        self.master.config(menu=self.menu)
        self.help_sub_menu = Menu(self.menu)
        self.help_sub_menu.add_command(label="Repair", command=self._repair_command)
        self.help_sub_menu.add_command(label="Contact", command=self._contact_command)
        self.help_sub_menu.add_command(label="Close", command=self._close_command)
        self.menu.add_cascade(label="Help", menu=self.help_sub_menu)

        # Adding components
        self.main_frame = Frame(master)
        self.header = Label(master, text="Oops! It seemed you've been hacked...", font=("Arial", self.H3))
        self.info = Label(self.main_frame, text=RANSOMWARE_INFO, font=("Arial", self.TEXT))
        self.decrypt_button = ttk.Button(self.main_frame, text='Decrypt the files', style='Accent.TButton')
        self.delete_button = ttk.Button(self.main_frame, text='Delete the files')
        pil_scary_image = Image.open(f"assets\\scaryimage.jpg")
        pil_scary_image = pil_scary_image.resize((pil_scary_image.width // 5, pil_scary_image.height // 5))
        self.scary_image = ImageTk.PhotoImage(pil_scary_image)
        self.scary_image_panel = Label(self.main_frame, image=self.scary_image)
        # positioning them with the grid
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.main_frame.grid(row=1, column=1, pady=20)
        self.header.grid(row=0, column=1)
        self.info.grid(row=0, column=0, columnspan=10, ipady=10)
        self.decrypt_button.grid(row=1, column=3)
        self.delete_button.grid(row=1, column=5)
        self.scary_image_panel.grid(row=2, column=0, columnspan=10, pady=15)

    def _close_command(self):
        tkinter.messagebox.showerror(title="Nope", message="Did you really think it'll work? ")

    def _close_x_command(self):
        tkinter.messagebox.showerror(title="Your computer is being hacked.", message="There is no way out.")

    def _repair_command(self):
        tkinter.messagebox.showwarning(title="Nah", message="You're pushing your luck")

    def _contact_command(self):
        tkinter.messagebox.showerror(title="I don't think so", message="We're not available at the moment!")





def main():
    try:
        execute_gui(RansomwareUI, theme="dark")
    except KeyboardInterrupt:
        print("program halted")


if __name__ == '__main__':
    main()
