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
        print("Nom du livre :", self.nom)
        print("Auteur :", self.auteur)
        print("Maison d'édition :", self.maison_edition)
        print("Code barre :", self.code_barre)

# Test des méthodes de la classe Livre
mon_livre = Livre("L'étranger", "Albert Camus", "Gallimard", "123456")


print("\nAprès modification :")
mon_livre.modification("La peste", "Albert Camus", "Gallimard", "654321")
mon_livre.affichage()
data = mon_livre
url = "https://api.qrserver.com/v1/create-qr-code/?data={}&size=100x100".format(data)
mon_livre.affichage()
response = requests.get(url)

with open("premier_livre.png", "wb") as f:
    f.write(response.content)
