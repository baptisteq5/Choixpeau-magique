from browser import document, html

document <= html.B("Hello World ! ")

def change_texte(ev):
    document["button"].textContent = "Nouvelle réponse"

document["button"].bind("click", change_texte)