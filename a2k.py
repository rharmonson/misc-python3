# anime to kodi (a2k) using the tkinter GUI
import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # code here

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side='top', fill='both', expand=True)
    root.mainloop()
