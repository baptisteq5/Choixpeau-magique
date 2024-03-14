from browser import document, html
import csv


table_questions = []
with open("questions du questionnaire choipeau-magique Pt2.csv", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    key_line = lines[0].strip()
    keys = key_line.split(";")
    for line in lines[1:]:
        line = line.strip()
        values = line.split(';')
        dico = {}
        for i in range(len(keys)):
            dico[keys[i]] = values[i]
        table_questions.append(dico)
  
print(table_questions)


def change_texte(ev):
    global i, profil, table_questions
    
    if ev.target.id == "bouton1":
        print("vous avez clique bouton 1.")
        liste_valeur = []
        a = 0
        for str in table_questions[i]["Profil 1"].split(","):
            chiffre = int(str)
            liste_valeur.append(chiffre)
        for element in profil:
            profil[element] += liste_valeur[a]
            a += 1 
        print(profil)
        i += 1
    elif ev.target.id == "bouton2":
        print("vous avez clique bouton 2.")
        liste_valeur = []
        a = 0
        for str in table_questions[i]["Profil 2"].split(","):
            chiffre = int(str)
            liste_valeur.append(chiffre)
        for element in profil:
            profil[element] += liste_valeur[a]
            a += 1 
        print(profil)
        i += 1
    elif ev.target.id == "bouton3":
        print("vous avez clique bouton 3.")
        liste_valeur = []
        a = 0
        for str in table_questions[i]["Profil 3"].split(","):
            chiffre = int(str)
            liste_valeur.append(chiffre)
        for element in profil:
            profil[element] += liste_valeur[a]
            a += 1 
        print(profil)
        i += 1
    print(i)
    document["bouton1"].textContent = table_questions[i]["Reponse 1"]
    document["bouton2"].textContent = table_questions[i]["Reponse 2"]
    document["bouton3"].textContent = table_questions[i]["Reponse 3"]
    document["zone_question"].textContent = table_questions[i]["Question"]
    if i == 7:
        page_resultat(profil)


def page_resultat(profil): 
    document["bouton1"].style.display = "None"
    document["bouton2"].style.display = "None"
    document["bouton3"].style.display = "None"
    document["bouton0"].style.display = "None"
    document["texte démarrage"].style.display = "None"
    ihm_kppv(profil)



# algorithme kppv
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
        

def affichage_maison(compteur_par_maisons, poudlard_characters_reduit):
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

    document <= html.H1("La maison qui vous correspond le mieux est : ") 
    (f"{compteur_par_maisons[0]['House']} !\n\n")

    document <= html.H2("Vos plus proches voisins sont :\n")
    for character in poudlard_characters_reduit:
        document <= html.P(f'{character["Name"]} de la maison {character["House"]}, ')
        (f'distance : {character["Distance"]}')
            
            
    

def ihm_kppv(profil):
    """
    Execute les fonctions pour permettre le bon déroulement de l'affichage dans 
    la console
    
    Entrée : une table de dictionnaires qui contient tous les profils type à 
    tester
    
    Sortie: l'execution des fonctions
    """
    poudlard_characters = fusion_import_perso()   
    poudlard_characters = distancekppv(poudlard_characters,
                                        profil['Courage'], profil['Ambition'],
                                        profil['Intelligence'], profil['Good']) 
    compteur_par_maisons, poudlard_characters_reduit = resultat_kppv_maisons(poudlard_characters)
    affichage_maison(compteur_par_maisons, poudlard_characters_reduit)


profil = {'Courage' : 5, 'Ambition' : 5, 'Intelligence' : 5, 'Good' : 5}
print(profil)
i = 0

document["bouton0"].bind("click", change_texte)
document["bouton1"].bind("click", change_texte)
document["bouton2"].bind("click", change_texte)
document["bouton3"].bind("click", change_texte)


        


