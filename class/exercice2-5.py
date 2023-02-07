import requests

class Livre:
    def __init__(self, nom, auteur, maison_edition, code_barre):
        self.nom = nom
        self.auteur = auteur
        self.maison_edition = maison_edition
        self.code_barre = code_barre
        
    def modification(self, nom, auteur, maison_edition, code_barre):
        self.nom = nom
        self.auteur = auteur
        self.maison_edition = maison_edition
        self.code_barre = code_barre
        
    def affichage(self):
        print("Nom :", self.nom)
        print("Auteur :", self.auteur)
        print("Maison d'edition :", self.maison_edition)
        print("Code barre :", self.code_barre)

class Roman(Livre):
    def __init__(self, nom, auteur, maison_edition, code_barre, type_roman, description):
        Livre.__init__(self, nom, auteur, maison_edition, code_barre)
        self.type_roman = type_roman
        self.description = description
        
    def modification(self, nom, auteur, maison_edition, code_barre, type_roman, description):
        Livre.modification(self, nom, auteur, maison_edition, code_barre)
        self.type_roman = type_roman
        self.description = description
        
    def affichage(self):
        Livre.affichage(self)
        print("Type de roman :", self.type_roman)
        print("Description :", self.description)

# Creation d'un livre
mon_livre = Livre("Les Fourmis", "Bernard Werber", "Robert Laffont", "123456789")
print("Information du livre :")
mon_livre.affichage()
print()

# Modification du livre
mon_livre.modification("Les Fourmis", "Bernard Werber", "Robert Laffont", "987654321")
print("Information modifiée du livre :")
mon_livre.affichage()
print()

# Creation d'un roman
mon_roman = Roman("Les Fourmis", "Bernard Werber", "Robert Laffont", "123456789", "Science-fiction", "Une histoire sur les fourmis et leur societe")
print("Information du roman :")
mon_roman.affichage()
print()

# Modification du roman
mon_roman.modification("Les Fourmis", "Bernard Werber", "Robert Laffont", "987654321", "Science-fiction", "Une histoire sur les fourmis et leur societe avancee")
print("Information modifiée du roman :")
mon_roman.affichage()


data = mon_roman
url = "https://api.qrserver.com/v1/create-qr-code/?data={}&size=100x100".format(data)
mon_livre.affichage()
response = requests.get(url)

with open("second_livre.png", "wb") as f:
    f.write(response.content)
