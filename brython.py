from browser import document, html

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
i = 0
def change_texte(ev):
    global i, profil, table_questions
    document["bouton1"].textContent = table_questions[i]["Reponse 1"]
    document["bouton2"].textContent = table_questions[i]["Reponse 2"]
    document["bouton3"].textContent = table_questions[i]["Reponse 3"]
    document["zone_question"].textContent = table_questions[i]["Question"]
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
    elif ev.target.id == "bouton0":
        i = -1
    i += 1
    
    
    
        

profil = {'Courage' : 5, 'Ambition' : 5, 'Intelligence' : 5, 'Good' : 5}
print(profil)

document["bouton0"].bind("click", change_texte)
document["bouton1"].bind("click", change_texte)
document["bouton2"].bind("click", change_texte)
document["bouton3"].bind("click", change_texte)
