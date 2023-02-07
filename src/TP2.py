import subprocess
import random


#Fonction pour exercice
def f(x):
  return x * x

def calcul(f, a, b, p):
  n = int((b-a)/p)
  sum = 0
  for i in range(n):
    x = a + i * p
    sum += f(x) * p
  return sum


def tour_ordinateur(n):
  return 4 - n % 4 if n % 4 != 0 else random.choice([1, 2, 3])

def jouer_partie(n):
  print("Il y a {} allumettes sur la table.".format(n))
  tour_actuel = random.choice([0, 1])
  nom_joueur = input("Entrer votre nom : ")
  
  while n > 1:
    print("Il reste {} allumettes".format(n))
    if tour_actuel == 0:
      print("Tour de {}.".format(nom_joueur))
      coup_joueur = int(input("Entrer 1, 2 ou 3 : "))
      while coup_joueur > 3 or coup_joueur < 1 or coup_joueur > n:
        coup_joueur = int(input("Entrer 1, 2 ou 3 : "))
      n -= coup_joueur
    else:
      print("Tour de l'ordinateur.")
      coup_ordinateur = tour_ordinateur(n)
      print("L'ordinateur enlève {} allumettes.".format(coup_ordinateur))
      n -= coup_ordinateur
    tour_actuel = (tour_actuel + 1) % 2

  print("{} a perdu.".format(nom_joueur) if tour_actuel == 0 else "L'ordinateur a perdu.")


###########################

#Fonction exercice
def exercice3():

# Pour créer un fichier binaire
    num1, num2 = int(input("Saisir un entier: ")), int(input("Saisir un autre entier: "))
    with open("BDD.bin", "wb") as f:
        f.write(num1.to_bytes(4, 'big'))
        f.write(num2.to_bytes(4, 'big'))

    # Pour créer un fichier texte
    num1, num2 = int(input("Saisir un entier: ")), int(input("Saisir un autre entier: "))
    with open("BDD.txt", "w") as f:
        f.write(str(num1) + "\n")
        f.write(str(num2))

    # Pour lire les données du fichier binaire
    with open("BDD.bin", "rb") as f:
        num1 = int.from_bytes(f.read(4), 'big')
        num2 = int.from_bytes(f.read(4), 'big')
        print("Données lues depuis BDD.bin :", num1, num2)

    # Pour lire les données du fichier texte
    with open("BDD.txt", "r") as f:
        num1 = int(f.readline().strip())
        num2 = int(f.readline().strip())
        print("Données lues depuis BDD.txt :", num1, num2)
    
    print("Pour recommencer, taper 1. \nPour revenir au menur précédent, taper 2 \n")
    choix = input("Entre votre choix ici : ")
    if choix == "1" : 
        exercice3()
    else :
        main_menu()

def exercice2():
    n = int(input("Entrer le nombre d'allumettes : "))
    jouer_partie(n)
    print("Pour recommencer, taper 1. \nPour revenir au menur précédent, taper 2 \n")
    choix = input("Entre votre choix ici : ")
    if choix == "1" : 
        exercice2()
    else :
        main_menu()

def exercice1():
    a = float(input("La valeur de A: "))
    b = float(input("La valeur de B: "))
    p = float(input("La valeur de P: "))

    result = calcul(f, a, b, p)
    print("Le résultat est : ", result," . On est sur une approximation via la méthode des rectlanges.")


    print("Pour recommencer, taper 1. \nPour revenir au menur précédent, taper 2 \n")
    choix = input("Entre votre choix ici : ")
    if choix == "1" : 
        exercice1()
    else :
        main_menu()

def main_menu():

    print("Bienvenue au Menu Principal du TP2\n")
    print("Pour accéder au premier exercice, taper 1\n")
    print("Pour accéder au second exercice, taper 2\n")
    print("Pour accéder au troisième exercice, taper 3\n")
    print("Pour accéder au quatrième exercice, taper 4\n")
    print("Pour accéder au cinquième exercice, taper 5\n")
    print("Pour accéder au sixième exercice, taper 6\n")

    print("Sinon retourner au menu principal, taper 0\n")


    choix = input("Entrer votre choix ici : ")

    if choix == "1" :
        exercice1()
    
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        subprocess.run(["python", "class/exercice2-4.py"])
    elif choix == "5":
        subprocess.run(["python", "class/exercice2-5.py"])
    elif choix == "6":
        subprocess.run(["python", "class/exercice2-6.py"])

    elif choix == "0":
         subprocess.run(["python", "../main.py"])
    
    else :
        main_menu()

main_menu()
