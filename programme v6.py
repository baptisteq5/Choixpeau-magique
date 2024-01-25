import csv

def fusion_import_perso():
    """
    Import des tables "Characters.csv" et "Caracteristiques_des_persos.csv" et 
    fusion de celles-ci
    
    Entrée : Rien
    Sortie : une table de dictionnaires, résultat de la jointure des deux fichiers

    """
    with open("Characters.csv", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        characters_tab = [{key : value.replace('\xa0', ' ')
                           for key, value in element.items()} for element in 
                          reader]
    
    with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        characteristics_tab = [{key : value for key, value in element.items()} 
                               for element in reader]

    poudlard_characters = []
    
    for poudlard_character in characteristics_tab:
        for kaggle_character in characters_tab:
            if poudlard_character['Name'] == kaggle_character['Name']:
                poudlard_character.update(kaggle_character)
                poudlard_characters.append(poudlard_character)
    
    return poudlard_characters


# print(fusion_import_perso())

def distancekppv(poudlard_characters, courage, ambition, intelligence, good):
    """
    Calcule la distance entre le personnage cible et tous les autres 
    personnages de Poudlard
    
    Entrée : une table de dictionnaire, 4 entiers correspondant aux 
    caracteristiques du personnage cible
    
    Sortie : une table de dictionnaire regroupant la distance entre le 
    personnage cible et chaque personnage de poudlard

    """

    for prenom in poudlard_characters:
        
        
        # changer les caractéristiques des personnages en entiers
        courage_perso = int(prenom["Courage"])
        ambition_perso = int(prenom["Ambition"])
        intelligence_perso = int(prenom["Intelligence"])
        good_perso = int(prenom["Good"])
        
        distance = ((courage - courage_perso)**2 + 
                    (ambition - ambition_perso)**2 +
                    (intelligence - intelligence_perso)**2 +
                    (good - good_perso)**2)**0.5
        
        
        prenom["Distance"] = distance

    poudlard_characters.sort(key=lambda x: x["Distance"] )
    del poudlard_characters[5:]
    return poudlard_characters
    
    



def resultat_kppv_maisons(poudlard_characters_reduit):
    table_dico_maisons = [{"House" : "Gryffindor", "Character"  : 0}, 
                          {"House" : "Slytherin", "Character" : 0},
                          {"House" : "Hufflepuff", "Character" : 0},
                          {"House" : "Ravenclaw", "Character" : 0 }]

    for name in poudlard_characters_reduit[:5]:
        if name["House"] == "Gryffindor":
            table_dico_maisons[0]["Character"] += 1
        elif name["House"] == "Slytherin":
            table_dico_maisons[1]["Character"] += 1
        elif name["House"] == "Hufflepuff":
            table_dico_maisons[2]["Character"] += 1
        elif name["House"] == "Ravenclaw":
            table_dico_maisons[3]["Character"] += 1
            
    table_dico_maisons.sort(key=lambda x : x["Character"], reverse=True)      
            
    return table_dico_maisons
        



def affichage_maison(compteur_par_maisons, poudlard_characters,
                     caracteristiques_inconnu):

    print("Le personnage inconnu ayant les caractéristiques "
          f"{caracteristiques_inconnu} est le plus proches de ces 5 autres " 
          "personnages :\n")
    
    for character in poudlard_characters:
        #if character["House"] == compteur_par_maisons[0]['House']: 
            print(f'{character["Name"]} de la maison {character["House"]}, '
                  f'distance : {character["Distance"]}\n')
            
            
    print(f"La maison qui vous correspond le mieux est donc : {compteur_par_maisons[0]['House']} !\n")

les_profiles_de_la_consigne = [{'Courage' : 9, 'Ambition' : 2, 'Intelligence' : 8, 'Good' : 9},
                               {'Courage' : 6, 'Ambition' : 7, 'Intelligence' : 9, 'Good' : 7},
                               {'Courage' : 3, 'Ambition' : 8, 'Intelligence' : 6, 'Good' : 3},
                               {'Courage' : 2, 'Ambition' : 3, 'Intelligence' : 7, 'Good' : 8},
                               {'Courage' : 3, 'Ambition' : 4, 'Intelligence' : 8, 'Good' : 8}]
valeur_list = ('Courage', 'Ambition', 'Intelligence', 'Good')
def ihm_kppv(list_de_dico):
    
    
    for persos in list_de_dico:
        poudlard_characters = fusion_import_perso()   
        poudlard_characters = distancekppv(poudlard_characters, persos['Courage'], persos['Ambition'], persos['Intelligence'], persos['Good'])    
        compteur_par_maisons = resultat_kppv_maisons(poudlard_characters)
        affichage_maison(compteur_par_maisons, poudlard_characters, persos)
                
               
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

ihm_kppv(les_profiles_de_la_consigne)


 



