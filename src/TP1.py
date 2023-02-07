import subprocess
import math
from decimal import Decimal
from tqdm import tqdm
import webbrowser

def factorielExo3(valeur):
    chiffre = 1
    valeurTabI= []
    for i in range(1, valeur+1) : 
        chiffre = chiffre*i
        valeurTabI.append(i)
    print("Le factoriel de  ", valeur, " est : ")
    print(" * ".join(map(str, valeurTabI)), " = ", chiffre)
    print(chiffre, "= "," * ".join(map(str, valeurTabI[::-1])))
    
def factoriel(valeur):
    chiffre = 1
    valeurTabI= []
    for i in range(1, valeur+1) : 
        chiffre = chiffre*i
    return(chiffre)
    
def F1(x,n):
    resultatF1 = x**n / Decimal(factoriel(n))
    return(resultatF1)

def somme(valeur):
    chiffre = 1
    valeurTabI= []
    for i in range(1, valeur+1) : 
        chiffre = chiffre+i
        valeurTabI.append(i)
    print("La somme de 0 à ", valeur, " est : ")
    print(" * ".join(map(str, valeurTabI)), " = ", chiffre)
    print(chiffre, "= "," * ".join(map(str, valeurTabI[::-1])))



def exercice1() :

    print("Choisissez un caractère de l'alphabet : ")
    charactere = input()
    print("Choisissez un chiffre compris entre 0 et 127 : ")
    numero = input()

    #On doit vérifier si la personne ne met qu'un seul caractère et non plusieurs charactères sinon ça plante totalement.
    #Pour faire chaque caractère d'une chaîne de caractère, il faudrait parser chaque élément de la chaîne et faire une boucle 
    #égal à la taille du tableau que l'on va créer.
    try:
        if len(charactere) == 1:
            print(charactere + " est égal à " + str(ord(charactere)) +"\n")
        else:
            print("Vous devez entrer un seul caractère.")
    except ValueError:
        print("Erreur, veuillez entrer un caractère valide.")

    
    try:
        numero = int(numero)
        if 0 <= numero <= 255:
            print("La correspondance ASCII pour "+ str(numero) + " est " + chr(numero))
        else:
            print("Le numéro doit être compris entre 0 et 255.")
    except ValueError:
        print("Vous devez entrer un nombre")

    
    
    print("Pour recommencer, taper 1. \n Pour revenir au menur précédent, taper 2 \n")
    choix = input("Entre votre choix ici : ")
    if choix == "1" : 
        exercice1()
    else :
        main_menu()

def exercice2():
    
    valeurA = int(input ("Choisissez la valeur de A (en m) : "))
    valeurB = int(input ("Choisissez la valeur de B (en m) : "))
    valeurC = int(input ("Choisissez la valeur de C (en m) : "))

    print("La surface du trapèze est de : ", (valeurA + valeurB)* valeurC * 0.5,"m²\n")
    print("Maintenant, je vais vous demander les valeurs souhaitées pour dessiner un trapèze.\n")
    
    #lancement du programme avec tkinter 
    subprocess.run(["python", "src/tkinter/trapeze.py"])
    print("Pour recommencer, taper 1. \n Pour revenir au menur précédent, taper 2 \n")
    choix = input("Entre votre choix ici : ")
    if choix == "1" : 
        exercice2()
    else :
        main_menu()

def exercice3():
    valeur = int(input("Veuillez saisir une valeur pour faire le factoriel et la somme de cette dernière :  \n"))
    factorielExo3(valeur)
    somme(valeur)
    print("Pour recommencer, taper 1. \n Pour revenir au menur précédent, taper 2 \n")
    choix = input("Entre votre choix ici : ")
    if choix == "1" : 
        exercice3()
    else :
        main_menu()
    
def exercice4():
    hauteur = int(input("Hauteur de l'arbre : "))
    for i in range(1, hauteur + 1):
        print("{}{}{}".format("=" * (hauteur - i), "*" * (2 * i - 1), "=" * (hauteur - i)))

    for i in range(1,3):
        print("{}{}{}".format("=" * (hauteur - 2), "*" * 3, "=" * (hauteur - 2)))
    print("Pour recommencer, taper 1. \n Pour revenir au menur précédent, taper 2 \n")
    choix = input("Entre votre choix ici : ")
    if choix == "1" : 
        exercice4()
    else :
        main_menu()

def exercice5():
    valeur = int(input("Veuillez saisir une valeur : "))
    #Il est pas possible de faire le log d'une valeur négative donc except-block
    try:
        if valeur >0:
            print("Le Logarithme népérien de ", valeur, " est : Ln(",valeur,") = ", math.log(valeur))
    except ValueError:
        print("Il est pas possible de calculer le logarithme népérien pour une valeur négative")
    #calcul cosinus et sinus de la valeur
    print("Le cosinus de ", valeur, " est : cos(",valeur,") = ", math.cos(valeur))
    print("Le sinus de ", valeur, " est : sin(",valeur,") = ", math.sin(valeur))
    
    print("Pour recommencer, taper 1. \n Pour revenir au menur précédent, taper 2 \n")
    choix = input("Entre votre choix ici : ")
    if choix == "1" : 
        exercice5()
    else :
        main_menu()

def exercice6():
    valeur = int(input("Veuillez rentrer une valeur pour n : "))
    
    resultat1 = factoriel(valeur-1)
    resultat2 = factoriel(valeur)
    resultat = resultat1*resultat2
    
    print("factoriel(",valeur,") est : ",resultat)
    
    x  = int(input("Veuillez saisir la valeur de x : "))
    n  = int(input("Veuillez saisir une valeur pour n : "))
    print(F1(x,n))
    
    
    print("Passons à la fonction Res(X,i)")
    x = Decimal(input("Saisir une valeur pour X"))
    n = int(input("Saisir une valeur de n"))

    #commenter à partir d'ici
    somme = 0
    
    for i in tqdm (range (1, n)):
        somme += F1(x,i)
    #Fin de ce qu'il faut commenter
    
    #Façon optimisée : 
    # somme = 0
    # facto = 1
    
    # for i in tqdm (range (1, n)):
    #     facto = facto*i
    #     somme += x**i /facto
        
    
    print(somme)
    
    print("Pour recommencer, taper 1. \n Pour revenir au menur précédent, taper 2 \n")
    choix = input("Entre votre choix ici : ")
    if choix == "1" : 
        exercice6()
    else :
        main_menu()
       
def exercice7():
    valeur= (int(input("Veuillez saisir une valeur pour n : ")))
    U0 = 1
    Un = U0
    
    for i in range(1, valeur+1) :
        Vn = Un + 1/(valeur * factoriel(i))
        Un = Un + (1 / factoriel(i))
        
    
    print("Valeur de la suite Un où n = ",valeur,"= ",Un)
    print("Valeur de la suite Vn où n = ",valeur,"= ",Vn)
    
    print("Pour recommencer, taper 1. \n Pour revenir au menur précédent, taper 2 \n")
    choix = input("Entre votre choix ici : ")
    if choix == "1" : 
        exercice7()
    else :
        main_menu()

def exercice8():
    n = int(input("Saisir la valeur de n :  "))
    p = int(input("Saisir la valeur de p :  "))
    FactoN = factoriel(n)
    FactoNP = factoriel(n-p)
    X = FactoN/ FactoNP
    Y = FactoN / (factoriel(p) * FactoNP)
    print(X)
    print(Y)
    print("Pour recommencer, taper 1. \n Pour revenir au menur précédent, taper 2 \n")
    choix = input("Entre votre choix ici : ")
    if choix == "1" : 
        exercice8()
    else :
        main_menu()
 
   
def main_menu():

    print("Bienvenue au Menu Principal du TP1\n")
    print("Pour accéder au premier exercice, taper 1\n")
    print("Pour accéder au second exercice, taper 2\n")
    print("Pour accéder au troisième exercice, taper 3\n")
    print("Pour accéder au quatrième exercice, taper 4\n")
    print("Pour accéder au cinquième exercice, taper 5\n")
    print("Pour accéder au sixième exercice, taper 6\n")
    print("Pour accéder au septième exercice, taper 7\n")
    print("Pour accéder au huitième exercice, taper 8\n")
    #print("Pour accéder au neuvième exercice, taper 9\n")
    print("Sinon retourner au menu principal, taper 0\n")


    choix = input("Entrer votre choix ici : ")

    if choix == "1" :
        exercice1()
    
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    if choix == "8" :
        exercice8()

    elif choix == "0":
         subprocess.run(["python", "../main.py"])
    
    else :
        main_menu()

main_menu()