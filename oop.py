# oop test
import tkinter as tk


class PathFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self['bg'] = 'lightblue'


class FilesFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self['bg'] = 'grey'


class TestFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self['bg'] = 'white'


class RegexFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self['bg'] = 'lightblue'
        self.button01 = tk.Button(self.tk.frame, text='Button 01')
        self.button01.grid()


root = tk.Tk()
root.geometry('800x600')
root.resizable(width=True, height=True)

frame_top = PathFrame(root)
frame_middle_left = FilesFrame(root)
frame_middle_right = TestFrame(root)
frame_bottom = RegexFrame(root)

frame_top.grid(row=0, column=0, rowspan=1, columnspan=6, sticky='ew')
frame_middle_left.grid(row=1, column=0, rowspan=1, columnspan=3, sticky='ewns')
frame_middle_right.grid(row=1, column=3, rowspan=1, columnspan=3, sticky='ewns')
frame_bottom.grid(row=2, column=0, rowspan=1, columnspan=6, sticky='ew')

root.mainloop()
