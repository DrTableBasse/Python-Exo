def factoriel():
    chiffre=1
    valeurI= []
    print("test")
    valeur = int(input("votre valeur : "))
    print(valeur)
    for i in range(1, valeur+1) : 
        chiffre = chiffre+i

        valeurI.append(i)
    print("resultat", chiffre)
    print(" * ".join(map(str, valeurI)), " = ", chiffre)
    print(chiffre, "= "," * ".join(map(str, valeurI[::-1])))
    
factoriel()