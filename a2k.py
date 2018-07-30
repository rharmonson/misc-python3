# oop test
import tkinter as tk
from tkinter import ttk


class PathFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()

        path_label = ttk.Label(self, text='Directory Path:')
        path_entry = ttk.Entry(self, font=('Arial', 12))
        path_select_button = ttk.Button(self, text='Select', width=8)

        path_label.pack(anchor='w', padx=5)
        path_entry.pack(side='left', anchor='n', expand=1, fill='x', padx=5)
        path_select_button.pack(side='right', anchor='n', padx=(0, 5))


class FilesFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        files_label = ttk.Label(self, text='Current Files')
        files_list = tk.Listbox(self, font=('Arial', 12))
        rename_label = ttk.Label(self, text='Renamed Files')
        rename_list = tk.Listbox(self, font=('Arial', 12))

        files_label.grid(row=0, column=0, sticky='n')
        rename_label.grid(row=0, column=1, sticky='n')
        files_list.grid(row=1, column=0, sticky='nesw')
        rename_list.grid(row=1, column=1, sticky='nesw')


class RegexFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()

        regex_label = ttk.Label(self, text='Regex:', width=8)
        regex_entry = ttk.Entry(self, font=('Arial', 12))
        regex_select_button = ttk.Button(self, text='Test', width=8)

        regex_label.pack(side='left', anchor='nw', padx=(5, 0))
        regex_entry.pack(side='left', anchor='n', expand=1, fill='x', padx=(0, 5))
        regex_select_button.pack(padx=(0, 5))


class RenameFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()

        rename_label = ttk.Label(self, text='Rename:', width=8)
        rename_entry = ttk.Entry(self, font=('Arial', 12))
        rename_select_button = ttk.Button(self, text='Execute', width=8)

        rename_label.pack(side='left', anchor='sw', padx=(5, 0))
        rename_entry.pack(side='left', anchor='n', expand=1, fill='x', padx=(0, 5))
        rename_select_button.pack(padx=(0, 5))


class RegexCalcFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()

        calc_space = ttk.Label(self, width=8)
        calc_button01 = ttk.Button(self, text='b01', width=3)
        calc_button02 = ttk.Button(self, text='b02', width=3)
        calc_button03 = ttk.Button(self, text='b03', width=3)
        calc_button04 = ttk.Button(self, text='b04', width=3)
        calc_button05 = ttk.Button(self, text='b05', width=3)
        calc_button06 = ttk.Button(self, text='b06', width=3)
        calc_button07 = ttk.Button(self, text='b07', width=3)
        calc_button08 = ttk.Button(self, text='b08', width=3)
        calc_button09 = ttk.Button(self, text='b09', width=3)
        calc_button10 = ttk.Button(self, text='b10', width=3)
        calc_button11 = ttk.Button(self, text='b11', width=3)
        calc_button12 = ttk.Button(self, text='b12', width=3)
        calc_button13 = ttk.Button(self, text='b13', width=3)
        calc_button14 = ttk.Button(self, text='b14', width=3)
        calc_button15 = ttk.Button(self, text='b15', width=3)
        calc_button16 = ttk.Button(self, text='b16', width=3)
        calc_button17 = ttk.Button(self, text='b17', width=3)
        calc_button18 = ttk.Button(self, text='b18', width=3)
        calc_button19 = ttk.Button(self, text='b19', width=3)
        calc_button20 = ttk.Button(self, text='b20', width=3)

        calc_space.grid(row=0, column=0,)
        calc_button01.grid(row=0, column=1, padx=2)
        calc_button02.grid(row=0, column=2, padx=2)
        calc_button03.grid(row=0, column=3, padx=2)
        calc_button04.grid(row=0, column=4, padx=2)
        calc_button05.grid(row=0, column=5, padx=2)
        calc_space.grid(row=1, column=0,)
        calc_button06.grid(row=1, column=1, padx=2)
        calc_button07.grid(row=1, column=2, padx=2)
        calc_button08.grid(row=1, column=3, padx=2)
        calc_button09.grid(row=1, column=4, padx=2)
        calc_button10.grid(row=1, column=5, padx=2)
        calc_space.grid(row=2, column=0,)
        calc_button11.grid(row=2, column=1, padx=2)
        calc_button12.grid(row=2, column=2, padx=2)
        calc_button13.grid(row=2, column=3, padx=2)
        calc_button14.grid(row=2, column=4, padx=2)
        calc_button15.grid(row=2, column=5, padx=2)
        calc_space.grid(row=3, column=0,)
        calc_button16.grid(row=3, column=1, padx=2)
        calc_button17.grid(row=3, column=2, padx=2)
        calc_button18.grid(row=3, column=3, padx=2)
        calc_button19.grid(row=3, column=4, padx=2)
        calc_button20.grid(row=3, column=5, padx=2)



root = tk.Tk()
root.title('a2k')
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_section01 = PathFrame(root)
frame_section02 = FilesFrame(root)
frame_section03 = RegexFrame(root)
frame_section04 = RenameFrame(root)
frame_section05 = RegexCalcFrame(root)

frame_section01.grid(row=0, column=0, sticky='new')
frame_section02.grid(row=1, column=0, sticky='nesw')
frame_section03.grid(row=2, column=0, sticky='new')
frame_section04.grid(row=3, column=0, sticky='new')
frame_section05.grid(row=4, column=0, sticky='new')

root.mainloop()
