from tkinter import *
from groups import Groups
from time import sleep
import particals


HEIGHT = 800
WIDTH = 800

root = Tk()
main_frame = Canvas(root, height=HEIGHT, width=WIDTH, bg='white')
main_frame.pack()
main_frame.update()
root.update()

group = Groups(main_frame, 2)
print(group.group[0].position,group.group[1].position)

while True:
    group.update()
    root.update()
    sleep(particals.Particals.time_interval)


root.mainloop()