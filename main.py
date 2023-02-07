##########################################

#mystère
import webbrowser


#ICI, permet juste d'éxécuter d'autre fichier.py
import subprocess


#Création d'un menu permettant d'exécuter d'autre programme python

def main_menu():

    print("Bienvenue au Menu Principal\n")
    print("Pour accéder aux exercices du TP1, taper 1\n")
    print("Pour accéder aux exercices du TP2, taper 2\n")
    print("?????????????????????????????????, taper 3\n")
    print("Sinon taper 0 pour quitter le progarmme\n")


    choix = input("Entrer votre choix ici : ")

    if choix == "1" :
        subprocess.run(["python", "src/TP1.py"])
    
    elif choix == "2":
        subprocess.run(["python", "src/TP2.py"])
    elif choix == "3":
        webbrowser.open('https://www.youtube.com/watch?v=_ccoZhuNlls')  # Go to example.com
    
    elif choix == "0":
        exit()
        
        
    
    else :
        print("Choix non valide. Veuillez réessayer")
        main_menu()

main_menu()