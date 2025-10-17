# Classe Voiture
from typing import Union, List


class Voiture:
    def __init__(
        self, marque: str, modele: str, prix: Union[float, int], kilometrage: int = 0
    ):
        self.marque = marque
        self.modele = modele
        self.prix = prix
        self.kilometrage = kilometrage

    def afficher_info(self) -> None:
        print("Marque: ", self.marque)
        print("Modèle: ", self.modele)
        print("Prix: ", self.prix)
        print("Kilométrage: ", self.kilometrage)
        print("")


# Classe VoitureElectrique (héritage)


class VoitureElectrique(Voiture):
    def __init__(
        self,
        marque: str,
        modele: str,
        prix: Union[float, int],
        autonomie: float,
        kilometrage=0,
    ):
        super().__init__(marque, modele, prix, kilometrage)
        self.autonomie = autonomie

    def afficher_info(self) -> None:
        print("Marque: ", self.marque)
        print("Modèle: ", self.modele)
        print("Prix: ", self.prix)
        print("Kilométrage: ", self.kilometrage)
        print("Autonomie: ", self.autonomie)
        print("")


# Classe Concession


class Concession:
    def __init__(self, nom: str):
        self.nom = nom
        self.inventaire = []

    def ajouter_voiture(self, voiture: Voiture) -> None:
        self.inventaire.append(voiture)

    def afficher_inventaire(self) -> None:
        for voiture in self.inventaire:
            voiture.afficher_info()

    def vendre_voiture(self, marque: str, modele: str) -> None:
        voiture_supprimer = [
            voiture
            for voiture in self.inventaire
            if voiture.marque == marque and voiture.modele == modele
        ]
        if len(voiture_supprimer) != 0:
            self.inventaire.remove(voiture_supprimer[0])
            print(f"La voiture {marque} {modele} a été vendue.")
        else:
            print("La voiture n'a pas été trouver.")

    def prix_moyen_tot(self) -> None:
        prix_list = [voiture.prix for voiture in self.inventaire]
        print(
            "La somme totale de prix de l'inventaire: ",
            sum(prix_list),
        )
        print(
            "La moyenne de prix de l'inventaire: ",
            sum(prix_list) / len(prix_list),
        )

    def __str__(self) -> str:
        return f"La concession {self.nom} à {len(self.inventaire)} voitures."


# Tests

concession = Concession("Concession du Centre")
voiture1 = Voiture("Peugeot", "205", 15000, 12000)
voiture2 = Voiture("Audi", "100", 10000, 10000)
voiture3 = Voiture("Fiat", "500", 13000, 20000)
voitureelec1 = VoitureElectrique("Tesla", "300", 15000, 12000, 300)
voitureelec2 = VoitureElectrique("Audi", "100", 10000, 10000, 200)
voitureelec3 = VoitureElectrique("Fiat", "200", 13000, 20000, 250)

concession.ajouter_voiture(voiture1)
concession.ajouter_voiture(voiture2)
concession.ajouter_voiture(voiture3)
concession.ajouter_voiture(voitureelec1)
concession.ajouter_voiture(voitureelec2)
concession.ajouter_voiture(voitureelec3)

concession.afficher_inventaire()

concession.vendre_voiture(marque="Peugeot", modele="205")
concession.vendre_voiture(marque="Fiat", modele="205")
print(concession)
concession.prix_moyen_tot()

# Question conceptuelle: Expliquez en quelques lignes l’intérêt de l’héritage en POO. Pourquoi créer une classe VoitureElectrique héritant de Voiture plutôt que de tout réécrire dans une classe indépendante ?
"""L'iintérét est tous d'abords de factoriseer les attributs 
et méthodes pour éviter de tous réécrire. Cela permet aussi 
une meilleur organisation du code."""
