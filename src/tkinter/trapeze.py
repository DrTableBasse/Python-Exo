from tkinter import *


def draw_trapezoid(base1, base2, height):
    base1 = int(base1)
    base2 = int(base2)
    height = int(height)
    point1 = (150 - base1/2,150 - height/2)
    point2 = (150 + base1/2, 150 - height/2)
    point3 = (150 + base2/2, 150 + height/2)
    point4 = (150 - base2/2, 150 + height/2)
    canvas.create_polygon(point1, point2, point3, point4, fill="white", outline="black")




root = Tk()


base1 = input("Entrez la longueur de la base 1: ")
base2 = input("Entrez la longueur de la base 2: ")
height = input("Entrez la hauteur du trapèze: ")

canvas = Canvas(root, width=800, height=600)
canvas.pack()

draw_trapezoid(base1, base2, height)

root.mainloop()
