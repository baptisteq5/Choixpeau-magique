# coding : utf-8

"""

Ce programme renvoi la maison de Poudlard qui correspond le mieux à une 
personnalitée type en calculant les plus proches voisins du nouveau personnage.

Authors: QUANTIN Baptiste, BIGOT Simon, FRANCOIS Valentine
Version : v.8
URL Github : https://github.com/baptisteq5/Choixpeau-magique

"""

import csv

les_profiles_de_la_consigne = [{'Courage' : 9, 'Ambition' : 2,
                                'Intelligence' : 8, 'Good' : 9},
                               {'Courage' : 6, 'Ambition' : 7, 
                                'Intelligence' : 9, 'Good' : 7},
                               {'Courage' : 3, 'Ambition' : 8, 
                                'Intelligence' : 6, 'Good' : 3},
                               {'Courage' : 2, 'Ambition' : 3,
                                'Intelligence' : 7, 'Good' : 8},
                               {'Courage' : 3, 'Ambition' : 4,
                                'Intelligence' : 8, 'Good' : 8}]

def fusion_import_perso():
    """
    Import des tables "Characters.csv" et "Caracteristiques_des_persos.csv" et 
    fusion de celles-ci
    
    Entrée : Rien
    Sortie : une table de dictionnaires, résultat de la jointure des deux fichiers

    """
    # ouverture du permier fichier
    with open("Characters.csv", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        characters_tab = [{key : value.replace('\xa0', ' ')
                           for key, value in element.items()} for element in 
                          reader]
    # ouverture du second fichier
    with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        characteristics_tab = [{key : value for key, value in element.items()} 
                               for element in reader]

    poudlard_characters = []
    
    # fusion des deux table dans une nouvelle table : poudlard_characters
    for poudlard_character in characteristics_tab:
        for kaggle_character in characters_tab:
            if poudlard_character['Name'] == kaggle_character['Name']:
                poudlard_character.update(kaggle_character)
                poudlard_characters.append(poudlard_character)
    
    return poudlard_characters


def distancekppv(poudlard_characters, courage, ambition, intelligence, good):
    """
    Calcule la distance entre le personnage cible et tous les autres 
    personnages de Poudlard
    
    Entrée : une table de dictionnaire, 4 entiers correspondant aux 
    caracteristiques du personnage cible
    
    Sortie : une table de dictionnaire contenant la distance entre le 
    personnage cible et chaque personnage de poudlard

    """

    for prenom in poudlard_characters:
        
        
        # changer les caractéristiques des personnages en entiers
        courage_perso = int(prenom["Courage"])
        ambition_perso = int(prenom["Ambition"])
        intelligence_perso = int(prenom["Intelligence"])
        good_perso = int(prenom["Good"])
        # calcul de la distance avec le voisin
        distance = ((courage - courage_perso)**2 + 
                    (ambition - ambition_perso)**2 +
                    (intelligence - intelligence_perso)**2 +
                    (good - good_perso)**2)**0.5
        
        
        prenom["Distance"] = distance

    poudlard_characters.sort(key=lambda x: x["Distance"])

    return poudlard_characters 
    
    



def resultat_kppv_maisons(poudlard_characters):
    """
    Comptage du nombre de voisins dans chaque maison pour savoir laquelle est 
    majoritaire. 
    
    Entrée : un table de dictionnaire avec les 5 plus proches voisins du nouveau
    personnage
    
    Sortie : une table de dictionnaire contenant le nombre de personnage(s) de 
    chaque maison
    
    """
    table_compteur_maison = [{"House" : "Gryffindor", "Character"  : 0}, 
                          {"House" : "Slytherin", "Character" : 0},
                          {"House" : "Hufflepuff", "Character" : 0},
                          {"House" : "Ravenclaw", "Character" : 0 }]
    valeur_voisins = 5
    
    while table_compteur_maison[0]["Character"] == table_compteur_maison[1]["Character"]: 
        table_compteur_maison = [{"House" : "Gryffindor", "Character"  : 0}, 
                              {"House" : "Slytherin", "Character" : 0},
                              {"House" : "Hufflepuff", "Character" : 0},
                              {"House" : "Ravenclaw", "Character" : 0 }]
        
        for name in poudlard_characters[:valeur_voisins]:
            if name["House"] == "Gryffindor":
                table_compteur_maison[0]["Character"] += 1
            elif name["House"] == "Slytherin":
                table_compteur_maison[1]["Character"] += 1
            elif name["House"] == "Hufflepuff":
                table_compteur_maison[2]["Character"] += 1
            elif name["House"] == "Ravenclaw":
                table_compteur_maison[3]["Character"] += 1
                
        table_compteur_maison.sort(key=lambda x : x["Character"], reverse=True) 
        valeur_voisins += 1
    del poudlard_characters[valeur_voisins - 1:]      

    return table_compteur_maison, poudlard_characters
        

def affichage_maison(compteur_par_maisons, poudlard_characters_reduit,
                     caracteristiques_inconnu):
    """
    Affiche dans la console le nom des 5 plus proches voisins du nouveau
    personnage, leur maison et la maison dans le nouveau personnage est le plus
    proche.
    
    Entrée : une table de dictionnaires : le compteur par maison des plus proches
    voisins, un table de dictionnaires contenant les caractéristiques de ses 
    voisins, un dictionnaire contenant les caracteriqutiques du nouveau personnage
    
    Sortie : un affichage dans la console des voisins et de la maison dont laquelle
    le nouveau personnage est le plus proche.
    """

    print("Le personnage inconnu ayant les caractéristiques "
          f"{caracteristiques_inconnu} est le plus proches de ces autres " 
          "personnages :\n")
    
    for character in poudlard_characters_reduit:
        print(f'{character["Name"]} de la maison {character["House"]}, '
              f'distance : {character["Distance"]}')
            
            
    print("\nLa maison qui lui correspond le mieux est donc : " 
          f"{compteur_par_maisons[0]['House']} !\n\n")


def ihm_kppv(profils_consigne):
    """
    Execute les fonctions pour permettre le bon déroulement de l'affichage dans 
    la console
    
    Entrée : une table de dictionnaires qui contient tous les profils type à 
    tester
    
    Sortie: l'execution des fonctions
    """
    
    for perso in profils_consigne:
        poudlard_characters = fusion_import_perso()   
        poudlard_characters = distancekppv(poudlard_characters,
                                           perso['Courage'], perso['Ambition'],
                                           perso['Intelligence'], perso['Good']) 
        compteur_par_maisons, poudlard_characters_reduit = resultat_kppv_maisons(poudlard_characters)
        affichage_maison(compteur_par_maisons, poudlard_characters_reduit, perso)
                


def ihm_kppv2(new_profil):
    '''
    Execute les fonctions pour permettre le bon déroulement de l'affichage dans 
    la console
    
    Entrée : une table de dictionnaires qui contient le profil crée à 
    tester
    
    Sortie: l'execution des fonctions
    '''
    poudlard_characters = fusion_import_perso()   
    poudlard_characters = distancekppv(poudlard_characters,
                                        new_profil['Courage'], new_profil['Ambition'],
                                        new_profil['Intelligence'], new_profil['Good']) 
    compteur_par_maisons, poudlard_characters_reduit = resultat_kppv_maisons(poudlard_characters)
    affichage_maison(compteur_par_maisons, poudlard_characters_reduit, new_profil)



def ihm():
    """
    Demande à l'utilisateur de tester les profils de la consigne ou de crée un nouveau profil à tester

    Entrée : aucune
    
    Sortie : IHM fonctionnelle 
    """
    start = input("Vous pouvez tester les kppv : \n 1- des profiles de la consigne\n 2- un autre profil (création) \n Toute autre action vous fera quitter le programme")   
    
    if start == '1':
        ihm_kppv(les_profiles_de_la_consigne)
        print('Au revoir')
    
    elif start == '2':
        list_new_profil = {'Courage' : 0, 'Ambition' : 0, 'Intelligence' : 0, 'Good' : 0}

        list_new_profil['Courage'] += (int(input('Saisissez une valeur de courage :')))
        list_new_profil['Ambition'] += (int(input("Saisissez une valeur d'ambition :")))
        list_new_profil['Intelligence'] += (int(input("Saisissez une valeur d'intelligence :")))
        list_new_profil['Good'] += (int(input('Saisissez une valeur de bonté :')))

        ihm_kppv2(list_new_profil)
        print('Au revoir')
        
    else:
        print("Le programme s'est arrêté")



ihm()