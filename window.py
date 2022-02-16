from tkinter import *
from groups import Groups, dt
from time import sleep

HEIGHT = 800
WIDTH = 800
TIME_INTERVAL = dt

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
    sleep(TIME_INTERVAL)
