class Joueur:
    nom = None
    couleur = 0

    def __init__(self, nom,  couleur):
        self.nom = nom
        self.couleur = couleur

    def getNom(self):
        return self.nom


class Humain(Joueur):
    def __init__(self, nom,  couleur):
        super().__init__(nom, couleur)

    def joue(self, jeu):
        jeu.afficher()
        valide = False
        while True:
            print("Joueur " + self.getNom() + ", entrez un num?ro de colonne" +
                  "  (entre 1 et " + str(jeu.getTaille()) + ") : ")
            col = int(input())
            # on pourrait faire ici la validation de la lecture
            col -= 1
            # remet entre 0 et taille-1 (indice ? la Java)
            valide = jeu.joueCoup(col, self.getCouleur())
            if (valide == False):
                print("-> Coup NON valide.")
            if ((valide == False) == False):
                break


class Ordinateur(Joueur):
    def __init__(self, couleur):
        super().__init__("Le programme", couleur)

    def joue(self, jeu):
        col = 0
        while (col < jeu.getTaille()):
            if (jeu.joueCoup(col, self.getCouleur())):
                print(self.getNom() + " a jou? en " + str((col + 1)))
                return
            col += 1
