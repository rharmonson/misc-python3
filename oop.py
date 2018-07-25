# oop test
import tkinter as tk


class PathFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self['height'] = 100
        self['width'] = 800
        self['bg'] = 'lightblue'


class FilesFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self['height'] = 400
        self['width'] = 800
        self['bg'] = 'grey'


class RegexFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self['height'] = 100
        self['width'] = 800
        self['bg'] = 'lightblue'


root = tk.Tk()
root.geometry('800x600')
root.resizable(width=True, height=True)

frame_top = PathFrame(root)
frame_middle = FilesFrame(root)
frame_bottom = RegexFrame(root)

frame_top.grid(row=0)
frame_middle.grid(row=1)
frame_bottom.grid(row=2)

root.mainloop()
