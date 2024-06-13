from tkinter import *
from tkinter import messagebox
from winsound import PlaySound


j1gagnant = False
j2gagnant = False
symbol = 1
tour = 1
cercles = []


class Partie:
    joueurs = list()

    def __init__(self, joueur1,  joueur2):
        self.joueurs.append(joueur1)
        self.joueurs.append(joueur2)
        self.jeu = Jeu()


class Jeu:
    VIDE = 0

    def __init__(self):
        self.initJeu(7)

    def initJeu(self, taille):
        self.taille = taille
        self.grille = [[0] * (taille) for _ in range(taille)]
        col = 0
        while (col < taille):
            row = 0
            while (row < taille):
                self.grille[col][row] = Jeu.VIDE
                row += 1
            col += 1

    def gagner(self, l, c):  # retourne si le joueur courant a gagné ou non
        if Jeu.nb_pions_alignées(self, l, c, 1, 1) >= 4 or Jeu.nb_pions_alignées(self, l, c, 1,
                                                                                 -1) >= 4 or Jeu.nb_pions_alignées(
                self, l, c, 0, 1) >= 4 or Jeu.nb_pions_alignées(self, l, c, 1, 0) >= 4:
            return True
        else:
            return False

    def joue(self, indColonne):
        global tour, symbol, message, affiche_message, j1gagnant, j2gagnant

        if tour < 21 and j1gagnant is False and j2gagnant is False:
            print("tour N°" + str(tour) + "\n")
            if len(indColonne) == 0: # si aucun chiffre nest entré
                message = "L'indice ne doit pas être-vide .\n Veuillez choisir un indice entre 0 et 6"
            elif not str(indColonne).isdigit():
                message = "L'indice doit-être un entier .\n Veuillez choisir un indice entre 0 et 6"
            else:
                colonne = int(indColonne)
                if not (colonne in range(7)):
                    message = " L'indice de la colonne est faux .\n Veuillez choisir un indice entre 0 et 6"
                else:
                    l = self.l_ajout(colonne)
                    if l == -1:  # si la case choisie n'est pas vide refaire la saisie des indices
                        message = "\n La colonne choisie n'est pas libre ,\n Veuillez choisir une autre colonne  "
                    else:
                        # mettre le numero de joueur dans la case choisie
                        self.ajout(symbol, colonne)
                        if symbol == 1:
                            cercles[l][colonne] = creation_cercle(
                                50 + colonne * 70, 50 + l * 70, 28, monCanvas, "#4169E1")

                            if self.gagner(l, colonne):

                                print(
                                    str(Partie.joueurs[0]) + " a gagnée !!")
                                messagebox.showinfo(
                                    "showinfo", Partie.joueurs[0] + " a gagnée !!")

                                j1gagnant = True

                            else:
                                symbol = 2
                                message = "C'est le tour de " + \
                                    str(Partie.joueurs[1])
                        else:
                            cercles[l][colonne] = creation_cercle(50 + colonne * 70, 50 + l * 70, 28, monCanvas,
                                                                  "#20B2AA")
                            if self.gagner(l, colonne):
                                print(
                                    str(self.joueurs[1]) + " a gagnée !!")

                                messagebox.showinfo(
                                    "showinfo", Partie.joueurs[1] + " a gagnée !!")

                                j2gagnant = True

                            else:
                                symbol = 1
                                message = "C'est le tour de " + \
                                    str(Partie.joueurs[0])
                                tour += 1

        else:
            if j1gagnant is True:
                message = str(Partie.joueurs[0]) + " a gagnée !!"
            elif j2gagnant is True:
                message = str(Partie.joueurs[1]) + " a gagnée !!"
            else:
                message = " c'était une amusante partie ! bravo les deux!! "

        affiche_message.pack_forget()
        affiche_message = Label(frame, text=message, bg='#eeeeee', font=(
            "Courrier", 18, "bold"), fg="#9932CC")
        affiche_message.pack()

    def l_ajout(self, c): #verfie si les colonnes est totalement rempli par 6 cercles
        l = 5 # tabda m 0 wanna 6 cercles
        while self.grille[l][c] != 0 and l >= 0:
            l -= 1 
        return l #traja3 fkol ligne gadeh aana mn wahda fergha

    def verif(self, c):  # retourne si la case est vide
        if c < 0 or c > 6:
            return False
        return self.grille[self.l_ajout(c)][c] == 0

    def ajout(self, symbol, c):  # ajouter le symbol (1 ou 2) a la case disponible
        if not self.verif(c):
            print("veuillez choisir une autre colonne")
            return False, -1
        l = self.l_ajout(c)
        self.grille[l][c] = symbol
        print(self)
        return True, l

    # compter les symboles alignées horizontalement, verticalement et en diagonale
    def nb_pions_alignées(self, l, colonne, x, y):
        symbol = self.grille[l][colonne]
        res = 1
        # comptabiliser les pions dans la direction (x,y)
        lig, col = l + y, colonne + x
        if lig in range(6) and col in range(7):
            while self.grille[lig][col] == symbol:
                res += 1
                lig, col = lig + y, col + x
                if lig not in range(6) or col not in range(7):
                    break

        # Comptabiliser les pions dans la direction opposée(-x,-y)
        lig, col = l - y, colonne - x
        if lig in range(6) and col in range(7):
            while self.grille[lig][col] == symbol:
                res += 1
                lig, col = lig - y, col - x
                if lig not in range(6) or col not in range(7):
                    break
        return res


def creer_fenetreNOM():
    # creer la fenetre de chargement des noms
    fenetre1 = Tk()
    fenetre1.title("Entrez vos noms")

    # creer les titre
    label_joueur1 = Label(fenetre1, text="Joueur 1 ", font=("Helvetica", 10))
    label_joueur2 = Label(fenetre1, text="Joueur 2 ", font=("Helvetica", 10))
    label_joueur1.grid(row=0, column=0, sticky=E, padx=10, pady=10)
    label_joueur2.grid(row=1, column=0, sticky=E, padx=10, pady=10)

    # creer les champs
    entrer_joueur1 = Entry(fenetre1)
    entrer_joueur2 = Entry(fenetre1)
    entrer_joueur1.grid(row=0, column=1, padx=15, pady=10)
    entrer_joueur2.grid(row=1, column=1, padx=15, pady=10)

    # creer un bouton pour lancer le jeu
    bouton_valider = Button(fenetre1, text="OK", width=10,
                            command=lambda: get_names(entrer_joueur1.get(), entrer_joueur2.get()))
    bouton_valider.grid(row=2, columnspan=2, padx=5, pady=(5, 15))

    # lancer la fenetre 1
    fenetre1.mainloop()


def get_names(nomJ1, nomJ2):

    global nom_j1, nom_j2
    if nomJ1 != "":
        nom_j1 += nomJ1
        Partie.joueurs.append(nom_j1)
    else:
        nom_j1 += "Joueur 1"
        Partie.joueurs.append(nom_j1)

    if nomJ2 != "":
        nom_j2 += nomJ2
        Partie.joueurs.append(nom_j2)
    else:
        nom_j2 += "Joueur 2"
        Partie.joueurs.append(nom_j2)

    creer_fenetreGRILLE()


def creer_fenetreGRILLE():
    a = 0

    global nom_j1, nom_j2, monCanvas, affiche_message, frame, partie, message, fenetre1
    partie = Jeu()  # initialiser le jeu
    # creer la fenetre principale de jeu
    fenetre2 = Tk()
    fenetre2.geometry("700x700")
    fenetre2.title("Puissance 4")

    monCanvas = Canvas(fenetre2, width=520, height=450, bg="#BA55D3")
    monCanvas.pack(side=TOP, padx=5, pady=5)
    for i in range(6):
        x = []
        for j in range(7):
            x.append(creation_cercle(50 + j * 70, 50 +
                     70 * i, 30, monCanvas, "#FAF0E6"))

        cercles.append(x)

    frame = Frame(fenetre2)
    entrer_colonne = Entry(frame, bd=5)
    frame.pack()

    entrer_colonne.pack()

    bouton_jouer = Button(frame, text="Jouer", command=lambda: partie.joue(
        entrer_colonne.get())).pack()
    message = "C'est le tour de " + (Partie.joueurs[0])
    affiche_message = Label(frame, text=message, bg='#eeeeee', font=(
        "Courrier", 18, "bold"), fg="#9932CC")
    indice_message = Label(frame, text="veuillez choisir un indice entre 0 et 6", bg='#eeeeee', font=(
        "Courrier", 10, "bold"), fg="#FF69B4")
    affiche_message.pack()
    indice_message.pack()
  

    monCanvas.bind("<Key>", key)
    monCanvas.bind("<Button-1>", callback)
    fenetre2.mainloop()


def key(event):
    print("pressed", repr(event.char))


def callback(event):
    print("clicked at", event.x, event.y)


def creation_cercle(x, y, r, nomCanvas, couleur):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return nomCanvas.create_oval(x0, y0, x1, y1, outline=couleur, fill=couleur)


if __name__ == "__main__":
    nom_j1, nom_j2 = '', ''
    print("aaaaaaa")
    #p = Partie(Humain(nomJ2, Jeu.BLEU), Humain(nom, Jeu.ROUGE))
    # p.joue()
    creer_fenetreNOM()


def play():
    pass
