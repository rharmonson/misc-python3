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
        self['height'] = 200
        self['width'] = 400
        self['bg'] = 'grey'


class TestFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self['height'] = 200
        self['width'] = 400
        self['bg'] = 'white'


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
frame_middle_left = FilesFrame(root)
frame_middle_right = TestFrame(root)
frame_bottom = RegexFrame(root)

frame_top.grid(row=0, column=0)
frame_middle_left.grid(row=1, column=0)
frame_middle_right.grid(row=1, column=1)
frame_bottom.grid(row=2, column=0)

root.mainloop()
