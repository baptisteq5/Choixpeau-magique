# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
valeur_list = ('Courage', 'Ambition', 'Intelligence', 'Good')
def ihm_kppv():
    start = input("Vous pouvez tester les kppv\
des profiles de la consigne(1)\
un autre(2)\
ou partir(autre chose)")
    while start in {'1', '2'}:
        if start == '1':
            for persos in les_profiles_de_la_consignes:
                plus_proches_voisins = fonction_kppv(persos)
                print(f"Les 5 plus proches voisons de {persos} sont {plus_proches_voisins} sa maison sera donc {fonction_kppv_qui_la_calcule}.")
                start = input("Vous pouvez tester les kppv\
des profiles de la consigne(1)\
un autre(2)\
ou partir(autre chose)")
        else:
            list_new_profile = []
            for valeurs in valeur_list:
                list_new_profile.append(int(input("Veullez entrez la valeur de {valeurs} que vous désirez pour votre profile : ")))
            print(f"Les 5 plus proches voisins de ce profile sont {plus_proches_voisins} sa maison sera donc {fonction_kppv_qui_la_calcule}.")
            start = input("Vous pouvez tester les kppv\
des profiles de la consigne(1)\
un autre(2)\
ou partir(autre chose)")
    print("Fin du programme")
ihm_kppv()

