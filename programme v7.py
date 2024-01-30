# coding : utf-8

"""
Ce programme renvoi la maison de Poudlard qui correspond le mieux à une 
personnalité type en calculant les plus proches voisins du nouveau personnage.

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
    
    



def resultat_kppv_maisons(poudlard_characters_reduit):
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
    
    while table_compteur_maison[0]["Character"] == table_compteur_maison[1]["Character"]: 
        
        valeur_voisins = 5
        for name in poudlard_characters_reduit[:valeur_voisins]:
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
        
        #print(table_compteur_maison)        

    return table_compteur_maison
        

def affichage_maison(compteur_par_maisons, poudlard_characters,
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
          f"{caracteristiques_inconnu} est le plus proches de ces 5 autres " 
          "personnages :\n")
    
    for character in poudlard_characters:
        #if character["House"] == compteur_par_maisons[0]['House']: 
            print(f'{character["Name"]} de la maison {character["House"]}, '
                  f'distance : {character["Distance"]}\n')
            
            
    print("La maison qui lui correspond le mieux est donc : " 
          f"{compteur_par_maisons[0]['House']} !\n")


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
        
        compteur_par_maisons = resultat_kppv_maisons(poudlard_characters)
        affichage_maison(compteur_par_maisons, poudlard_characters, perso)
                

ihm_kppv(les_profiles_de_la_consigne)


"""
start = input("Vous pouvez tester les kppv"
              "des profiles de la consigne(1)")               
 un autre(2)\
 ou partir(autre chose)")    
        else:
            list_new_profile = []
            for caractéristiques in valeur_list:
                list_new_profile.append(int(input("Veullez entrez la valeur de {caractéristiques} que vous désirez pour votre profile : ")))
            print(f"m")
            start = input("Vous pouvez tester les kppv\
 des profiles de la consigne(1)\
 un autre profile (création)(2)\
 ou partir(autre chose)")
   print("Fin du programme")
""" 



