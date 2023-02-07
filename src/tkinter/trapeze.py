from tkinter import *


def trapezoid(base1, base2, hauteur):
    base1 = int(base1)
    base2 = int(base2)
    hauteur = int(hauteur)
    point1 = (150 - base1/2,150 - hauteur/2)
    point2 = (150 + base1/2, 150 - hauteur/2)
    point3 = (150 + base2/2, 150 + hauteur/2)
    point4 = (150 - base2/2, 150 + hauteur/2)
    canvas.create_polygon(point1, point2, point3, point4, fill="white", outline="black")




root = Tk()


base1 = input("Entrez la longueur de la base 1: ")
base2 = input("Entrez la longueur de la base 2: ")
hauteur = input("Entrez la hauteur du trapèze: ")

canvas = Canvas(root, width=800, hauteur=600)
canvas.pack()

trapezoid(base1, base2, hauteur)

root.mainloop()
