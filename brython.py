from browser import document, html

table_questions = []
with open("questionnaire version 1.csv", mode='r', encoding='utf-8') as f:
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
    global i
    document["bouton1"].textContent = table_questions[i]["Reponse 1"]
    document["bouton2"].textContent = table_questions[i]["Reponse 2"]
    document["bouton3"].textContent = table_questions[i]["Reponse 3"]
    document["zone_question"].textContent = table_questions[i]["Question"]
    i += 1
    

profil = {'Courage' : 0, 'Ambition' : 0, 'Intelligence' : 0, 'Good' : 0}

def profil_bouton_1(profil_perso, table_questions):
    for valeur in table_questions["Profil"]:
        int(valeur)
        valeur.split(",")
        print(valeur)
        """
        for cate in profil.values:
            cate += valeur
    print(profil)
    """
    




document["bouton1"].bind("click", change_texte)
document["bouton2"].bind("click", change_texte)
document["bouton3"].bind("click", change_texte)
