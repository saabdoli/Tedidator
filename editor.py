from Tkinter import *
import ScrolledText


class MainApp(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create scrollbar
        txt_area = ScrolledText.ScrolledText(root, width=100, height=80)
        txt_area.pack()



if __name__ == '__main__':
    root = Tk()
    MainApp(root).pack(side='top', fill='both', expand=True)
    root.mainloop()
