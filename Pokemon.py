import time
from random import*
pokemonlist = ["", "Carapuce", "Salamèche", "Bulbizzard", "Pikachu", "Ratata", "Roucoul"]
PV_Pok = {"Carapuce": 60, "Salamèche": 60, "Bulbizzard": 70, "Pikachu": 60, "Ratata": 50, "Roucoul": 60}
attaque_Pok = {"Charge": 15, "Pistoler à O": 25, "Plonger": 25, "Vive-attaque": 10, "Eclair": 25, "Feu folet": 15, "Flamèche": 25, "Griffe": 20, "Fouet liane": 25, "Vol de vie": 10, "Crocs-fatal": 30, "Abri": 5, "Cru-aile": 25, "Atterissage": 0}
liste_att_carapuce = ["", "Charge", "Pistoler à O", "Plonger"]
liste_att_salameche = ["", "Griffe", "Flamèche", "Feu folet"]
liste_att_bulbizzard = ["", "Charge", "Fouet liane", "Vol de vie"]
liste_att_pikachu = ["", "Charge", "Vive-attaque", "Eclair"]
liste_att_ratata = ["", "Vive-attaque", "Crocs-fatal", "Abri"]
liste_att_roucoul = ["", "Griffe", "Cru-aile", "Atterissage"]
Liste_of_liste = ["", liste_att_carapuce, liste_att_salameche, liste_att_bulbizzard, liste_att_pikachu, liste_att_ratata, liste_att_roucoul]


def MontrerAttaqueJ1(): 
    print( "1)" + str(Liste_of_liste[PokJ1][1]))
    print( "2)" + str(Liste_of_liste[PokJ1][2]))
    print( "3)" + str(Liste_of_liste[PokJ1][3]))
    return

def MontrerAttaqueJ2(): 
    print( "1)" + str(Liste_of_liste[PokJ2][1]))
    print( "2)" + str(Liste_of_liste[PokJ2][2]))
    print( "3)" + str(Liste_of_liste[PokJ2][3]))
    return


print("-------------------------------------------------------------------------------------------------------------------------------")
print("")
print("Hello J1! bienvenu dans l'Arene Pokemon !")
print("")
print("-------------------------------------------------------------------------------------------------------------------------------")
time .sleep(5)
print("")
print("========MENU========")
print(" 1) - ORDI - ") 
print(" 2) - 1V1 - ")  
#print(" 3) - 2V2 - ")
mdj = int(input("Choissisez votre mode de jeu : "))
print("")
print("-------------------------------------------------------------------------------------------------------------------------------")
if mdj == 1:
    print("Bienvenur dans dans l'entrainement contre l'ordinateur")
    print("J1 voici les pokemons pour le 1er round:")
    print("")
    print("   1) - Carapuce ")
    print("   2) - Salamèche ")
    print("   3) - Bulbizzard ")
    print("   4) - Pikachu ")
    print("   5) - Ratata ")
    print("   6) - Roucoul ")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    PokJ1 = int(input("Veuillez choisir votre pokemon en sélectionnant son numéro : "))
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("")
    while PokJ1 < 1 or PokJ1 > 6:
        PokJ1 = int(input("Veuillez rentrer un chiffre valide ! : "))
        print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print("vous avez choisi le n° " + str(PokJ1) + ", " + str(pokemonlist[PokJ1]) + ".")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    PokOrdi1 = randint(1,6)
    time.sleep(2)
    print("")
    print("l'Ordinateur a choisi le n° " + str(PokOrdi1) + ", " + str(pokemonlist[PokOrdi1]) + ".")
    print("")
    PokJ1N = pokemonlist[PokJ1]
    PokOrdi1N = pokemonlist[PokOrdi1]
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print(PokJ1N + " a " + str(PV_Pok[PokJ1N]) + "PV")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print(PokOrdi1N + " a " + str(PV_Pok[PokOrdi1N]) + "PV")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print("Que le Combat commence !")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print("C'est à votre tour")
    print("")

    MontrerAttaqueJ1()

    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    attaqueJ1T1 = int(input("J1 à vous de jouer, séléctionner une attaque parmi les trois que votre Pokemon connait en rentrant son 'numéro': "))
    print("")
    while attaqueJ1T1 < 1 or attaqueJ1T1 > 3:
        attaqueJ1T1 = int(input("Veuillez rentrer un chiffre valide : "))
        print("")
    attaqueJ1T1 = str(Liste_of_liste[PokJ1][attaqueJ1T1])


    def VolDeVieJ1():
        if attaqueJ1T1 == "Vol de vie":
            PV_Pok[PokJ1N] = PV_Pok[PokJ1N] + 10
            if PV_Pok[PokJ1N] > 100:
                PV_Pok[PokJ1N] = 100
            print(PokJ1N + " vol " + str(attaque_Pok[attaqueJ1T1]) + " hp a " + PokOrdi1N)
        return
    
    def AtterissageJ1():
        if attaqueJ1T1 == "Atterissage":
            PV_Pok[PokJ1N] = PV_Pok[PokJ1N] + 20
            if PV_Pok[PokJ1N] > 80:
                PV_Pok[PokJ1N] = 80
            print(PokJ1N + " se soigne de " + str(20) + " hp")
        return


    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print(PokJ1N + " de J1 attaque " + str(attaqueJ1T1))
    print(str(attaqueJ1T1) + " inflige " + str(attaque_Pok[attaqueJ1T1]) + " point de dégats à " + PokOrdi1N)
    time.sleep(2)
    print("")
    (PV_Pok[PokOrdi1N]) = (PV_Pok[PokOrdi1N]) - (attaque_Pok[attaqueJ1T1])

    VolDeVieJ1()

    AtterissageJ1()

    print(PokOrdi1N + " de l'ordinateur perd " + str(attaque_Pok[attaqueJ1T1]) + " hp et passe maintenant à " + str(PV_Pok[PokOrdi1N]) + " hp")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("C'est au tour de l'ordinateur")
    print("")
    attaqueOrdi1T1 = randint(1,3)
    attaqueOrdi1T1 = str(Liste_of_liste[PokOrdi1][attaqueOrdi1T1])


    def VolDeVieO():
        if attaqueOrdi1T1 == "Vol de vie":
            PV_Pok[PokOrdi1N] = PV_Pok[PokOrdi1N] + 10
            if PV_Pok[PokOrdi1N] > 100:
                PV_Pok[PokOrdi1N] = 100
            print(PokOrdi1N + " vol " + str(attaque_Pok[attaqueOrdi1T1]) + " hp a " + PokJ1N)
        return

    def AtterissageO():
        if attaqueOrdi1T1 == "Atterissage":
            PV_Pok[PokOrdi1N] = PV_Pok[PokOrdi1N] + 20
            if PV_Pok[PokOrdi1N] > 80:
                PV_Pok[PokOrdi1N] = 80
            print(PokOrdi1N + " se soigne de " + str(20) + " hp")
        return

    
    time.sleep(2)
    print("")
    print(PokOrdi1N + " de l'ordinateur attaque " + str(attaqueOrdi1T1))
    print(str(attaqueOrdi1T1) + " inflige " + str(attaque_Pok[attaqueOrdi1T1]) + " point de dégats à " + PokJ1N)
    time.sleep(2)
    print("")
    (PV_Pok[PokJ1N]) = (PV_Pok[PokJ1N]) - (attaque_Pok[attaqueOrdi1T1])

    VolDeVieO()

    AtterissageO()

    print(PokJ1N + " de J1 perd " + str(attaque_Pok[attaqueOrdi1T1]) + " hp et passe maintenant à " + str((PV_Pok[PokJ1N])) + " hp")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    while PV_Pok[PokJ1N] or PV_Pok[PokOrdi1N] > 0:
        print("")
        print("C'est à votre tour")
        print("")

        MontrerAttaqueJ1()

        print("")
        print("-------------------------------------------------------------------------------------------------------------------------------")
        time.sleep(2)
        print("")
        attaqueJ1T1 = int(input("J1 à vous de jouer, séléctionner une attaque parmi les trois que votre Pokemon connait en rentrant son 'numéro': "))
        print("")
        while attaqueJ1T1 < 1 or attaqueJ1T1 > 3:
            attaqueJ1T1 = int(input("Veuillez rentrer un chiffre valide : "))
            print("")
        attaqueJ1T1 = str(Liste_of_liste[PokJ1][attaqueJ1T1])
        print("-------------------------------------------------------------------------------------------------------------------------------")
        time.sleep(2)
        print("")
        print(PokJ1N + " de J1 attaque " + str(attaqueJ1T1))
        print(str(attaqueJ1T1) + " inflige " + str(attaque_Pok[attaqueJ1T1]) + " point de dégats à " + PokOrdi1N)
        time.sleep(2)
        print("")
        (PV_Pok[PokOrdi1N]) = (PV_Pok[PokOrdi1N]) - (attaque_Pok[attaqueJ1T1])
        
        VolDeVieJ1()

        AtterissageJ1()

        if PV_Pok[PokOrdi1N] < 0:
            PV_Pok[PokOrdi1N] = 0
        print(PokOrdi1N + " de l'ordinateur perd " + str(attaque_Pok[attaqueJ1T1]) + " hp et passe maintenant à " + str(PV_Pok[PokOrdi1N]) + " hp")
        print("")
        if PV_Pok[PokOrdi1N] == 0:
            print("Vous avez gagné !")
            break
        print("-------------------------------------------------------------------------------------------------------------------------------")
        attaqueOrdi1T1 = randint(1,3)
        attaqueOrdi1T1 = str(Liste_of_liste[PokOrdi1][attaqueOrdi1T1])
        time.sleep(2)
        print("")
        print(PokOrdi1N + " de l'ordinateur attaque " + str(attaqueOrdi1T1))
        print(str(attaqueOrdi1T1) + " inflige " + str(attaque_Pok[attaqueOrdi1T1]) + " point de dégats à " + PokJ1N)
        time.sleep(2)
        print("")
        (PV_Pok[PokJ1N]) = (PV_Pok[PokJ1N]) - (attaque_Pok[attaqueOrdi1T1])

        VolDeVieO()

        AtterissageO()

        if PV_Pok[PokJ1N] < 0:
            PV_Pok[PokJ1N] = 0
        print(PokJ1N + " de J1 perd " + str(attaque_Pok[attaqueOrdi1T1]) + " hp et passe maintenant à " + str((PV_Pok[PokJ1N])) + " hp")
        print("")
        if PV_Pok[PokJ1N] == 0:
            print("Vous avez perdu ...")
            break
        print("-------------------------------------------------------------------------------------------------------------------------------")       



elif mdj == 2:
    print("Bienvenur dans l'Arène 1V1")
    print("J1 voici les pokemons pour le 1er round:")
    print("")
    print("   1) - Carapuce ")
    print("   2) - Salamèche ")
    print("   3) - Bulbizzard ")
    print("   4) - Pikachu ")
    print("   5) - Ratata ")
    print("   6) - Roucoul ")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    PokJ1 = int(input("Veuillez choisir votre pokemon en sélectionnant son numéro : "))
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("")
    while PokJ1 < 1 or PokJ1 > 6:
        PokJ1 = int(input("Veuillez rentrer un chiffre valide ! : "))
        print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print("Le J1 a choisi le n° " + str(PokJ1) + ", " + str(pokemonlist[PokJ1]) + ".")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(3)
    print("")
    print("J2 voici les pokemons pour le 1er round:")
    print("")
    print("   1) - Carapuce ")
    print("   2) - Salamèche ")
    print("   3) - Bulbizzard ")
    print("   4) - Pikachu ")
    print("   5) - Ratata ")
    print("   6) - Roucoul ")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    PokJ2 = int(input("Veuillez choisir votre pokemon en sélectionnant son numéro : "))
    time.sleep(2)
    print("")
    print("Le J2 a choisi le n° " + str(PokJ2) + ", " + str(pokemonlist[PokJ2]) + ".")
    print("")
    PokJ1N = pokemonlist[PokJ1]
    PokJ2N = pokemonlist[PokJ2]
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print(PokJ1N + " a " + str(PV_Pok[PokJ1N]) + "PV")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print(PokJ2N + " a " + str(PV_Pok[PokJ2N]) + "PV")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print("Que le Combat commence !")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print("C'est au tour de J1")
    print("")

    MontrerAttaqueJ1()

    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    attaqueJ1T1 = int(input("J1 à vous de jouer, séléctionner une attaque parmi les trois que votre Pokemon connait en rentrant son 'numéro': "))
    print("")
    while attaqueJ1T1 < 1 or attaqueJ1T1 > 3:
        attaqueJ1T1 = int(input("Veuillez rentrer un chiffre valide : "))
        print("")
    attaqueJ1T1 = str(Liste_of_liste[PokJ1][attaqueJ1T1])


    def VolDeVieJ1():
        if attaqueJ1T1 == "Vol de vie":
            PV_Pok[(PokJ1N)] = PV_Pok[PokJ1N] + 10
            if PV_Pok[PokJ1N] > 100:
                PV_Pok[PokJ1N] = 100
            print(PokJ1N + " vol " + str(attaque_Pok[attaqueJ1T1]) + " hp a " + PokJ2N)
            return

    def AtterissageJ1():
        if attaqueJ1T1 == "Atterissage":
            PV_Pok[PokJ1N] = PV_Pok[PokJ1N] + 20
            if PV_Pok[PokJ1N] > 80:
                PV_Pok[PokJ1N] = 80
            print(PokJ1N + " se soigne de " + str(20) + " hp")
        return


    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print(PokJ1N + " de J1 attaque " + str(attaqueJ1T1))
    print(str(attaqueJ1T1) + " inflige " + str(attaque_Pok[attaqueJ1T1]) + " point de dégats à " + PokJ2N)
    time.sleep(2)
    print("")
    (PV_Pok[PokJ2N]) = (PV_Pok[PokJ2N]) - (attaque_Pok[attaqueJ1T1])
    
    VolDeVieJ1()

    AtterissageJ1()

    print(PokJ2N + " de J2 perd " + str(attaque_Pok[attaqueJ1T1]) + " hp et passe maintenant à " + str(PV_Pok[PokJ2N]) + " hp")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("C'est au tour de J2")
    print("")

    MontrerAttaqueJ2()

    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    attaqueJ2 = int(input("J1 à vous de jouer, séléctionner une attaque parmi les trois que votre Pokemon connait en rentrant son 'numéro': "))
    print("")
    while attaqueJ2 < 1 or attaqueJ2 > 3:
        attaqueJ2 = int(input("Veuillez rentrer un chiffre valide : "))
        print("")
    attaqueJ2 = str(Liste_of_liste[PokJ2][attaqueJ2])


    def VolDeVieJ2():
        if attaqueJ2 == "Vol de vie":
            PV_Pok[PokJ2N] = PV_Pok[PokJ2N] + 10
            if PV_Pok[PokJ2N] > 100:
                PV_Pok[PokJ2N] = 100
            print(PokJ2N + " vol " + str(attaque_Pok[attaqueJ2]) + " hp a " + PokJ1N)
        return

    def AtterissageJ2():
        if attaqueJ2 == "Atterissage":
            PV_Pok[PokJ2N] = PV_Pok[PokJ2N] + 20
            if PV_Pok[PokJ2N] > 80:
                PV_Pok[PokJ2N] = 80
            print(PokJ2N + " se soigne de " + str(20) + " hp")
        return


    print("-------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("")
    print(PokJ2N + " de J2 attaque " + str(attaqueJ2))
    print(str(attaqueJ2) + " inflige " + str(attaque_Pok[attaqueJ2]) + " point de dégats à " + PokJ1N)
    time.sleep(2)
    print("")
    (PV_Pok[PokJ1N]) = (PV_Pok[PokJ1N]) - (attaque_Pok[attaqueJ2])

    VolDeVieJ2()

    AtterissageJ2()

    print(PokJ1N + " de J1 perd " + str(attaque_Pok[attaqueJ2]) + " hp et passe maintenant à " + str((PV_Pok[PokJ1N])) + " hp")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    while PV_Pok[PokJ1N] or PV_Pok[PokJ2N] > 0:
        print("")
        print("C'est au tour de J1")
        print("")

        MontrerAttaqueJ1()

        print("")
        print("-------------------------------------------------------------------------------------------------------------------------------")
        time.sleep(2)
        print("")
        attaqueJ1T1 = int(input("J1 à vous de jouer, séléctionner une attaque parmi les trois que votre Pokemon connait en rentrant son 'numéro': "))
        print("")
        while attaqueJ1T1 < 1 or attaqueJ1T1 > 3:
            attaqueJ1T1 = int(input("Veuillez rentrer un chiffre valide : "))
            print("")
        attaqueJ1T1 = str(Liste_of_liste[PokJ1][attaqueJ1T1])
        print("-------------------------------------------------------------------------------------------------------------------------------")
        time.sleep(2)
        print("")
        print(PokJ1N + " de J1 attaque " + str(attaqueJ1T1))
        print(str(attaqueJ1T1) + " inflige " + str(attaque_Pok[attaqueJ1T1]) + " point de dégats à " + PokJ2N)
        time.sleep(2)
        print("")
        (PV_Pok[PokJ2N]) = (PV_Pok[PokJ2N]) - (attaque_Pok[attaqueJ1T1])

        VolDeVieJ1()

        AtterissageJ1()

        if PV_Pok[PokJ2N] < 0:
            PV_Pok[PokJ2N] = 0
        print(PokJ2N + " de J2 perd " + str(attaque_Pok[attaqueJ1T1]) + " hp et passe maintenant à " + str(PV_Pok[PokJ2N]) + " hp")
        print("")
        if PV_Pok[PokJ2N] == 0:
            print("J1 a GAGNER !")
            break
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("")
        print("C'est au tour de J2")
        print("")

        MontrerAttaqueJ2()

        print("")
        print("-------------------------------------------------------------------------------------------------------------------------------")
        attaqueJ2 = int(input("J1 à vous de jouer, séléctionner une attaque parmi les trois que votre Pokemon connait en rentrant son 'numéro': "))
        print("")
        while attaqueJ2 < 1 or attaqueJ2 > 3:
            attaqueJ2 = int(input("Veuillez rentrer un chiffre valide : "))
            print("")
        attaqueJ2 = str(Liste_of_liste[PokJ2][attaqueJ2])
        time.sleep(2)
        print("")
        print(PokJ2N + " de J2 attaque " + str(attaqueJ2))
        print(str(attaqueJ2) + " inflige " + str(attaque_Pok[attaqueJ2]) + " point de dégats à " + PokJ1N)
        time.sleep(2)
        print("")
        (PV_Pok[PokJ1N]) = (PV_Pok[PokJ1N]) - (attaque_Pok[attaqueJ2])

        VolDeVieJ2()

        AtterissageJ2()

        if PV_Pok[PokJ1N] < 0:
            PV_Pok[PokJ1N] = 0
        print(PokJ1N + " de J1 perd " + str(attaque_Pok[attaqueJ2]) + " hp et passe maintenant à " + str((PV_Pok[PokJ1N])) + " hp")
        print("")
        if PV_Pok[PokJ1N] == 0:
            print("J2 a GAGNER !s")
            break
        print("-------------------------------------------------------------------------------------------------------------------------------")





#Reg_att_ratata = {"Abri": attaqueOrdi1T1}
#    del pokemonlist[PokJ1]
#    pokemonlist.insert(PokJ1, "")
#print(pokemonlist)
        