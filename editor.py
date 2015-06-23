from Tkinter import *
import ScrolledText

# Initialize root window
root = Tk()

# Create scrollbar
txt_area = ScrolledText.ScrolledText(root, width=100, height=80)

txt_area.pack()

root.mainloop()
