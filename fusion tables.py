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
                           for key, value in element.items()} for element in reader]
    
    with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        characteristics_tab = [{key : value for key, value in element.items()} for element in reader]

    poudlard_characters = []
    
    for poudlard_character in characteristics_tab:
        for kaggle_character in characters_tab:
            if poudlard_character['Name'] == kaggle_character['Name']:
                poudlard_character.update(kaggle_character)
                poudlard_characters.append(poudlard_character)
    
    return poudlard_characters


# print(fusion_import_perso())

def distancekppv(table, courage, ambition, intelligence, good):
    """
    Calcule la distance entre le personnage cible et tous les autres personnages
    de Poudlard
    
    Entrée : une table de dictionnaire, 4 entiers correspondant aux caracteristiques 
    du personnage cible
    
    Sortie : une table de dictionnaire regroupant la distance entre le personnage
    cible et chaque personnage de poudlard

    """
    table_distance = []
    for prenom in table:
        dico_distances = {}
        
        # changer les caractéristiques des personnages en entiers
        courage_perso = int(prenom["Courage"])
        ambition_perso = int(prenom["Ambition"])
        intelligence_perso = int(prenom["Intelligence"])
        good_perso = int(prenom["Good"])
        
        distance = ((courage - courage_perso)**2 + 
                    (ambition - ambition_perso)**2 +
                    (intelligence - intelligence_perso)**2 +
                    (good - good_perso)**2)**0.5
        
        dico_distances["Prenom"] = prenom["Name"]
        dico_distances["Distance"] = distance
        table_distance.append(dico_distances)
        table_distance.sort(key=lambda x: x["Distance"] )
    return table_distance
    
    
poudlard_characters = fusion_import_perso()   
print(distancekppv(poudlard_characters, 5, 3, 8, 9))













