import random
import string

print("Générateur de mot de passe aléatoire")

def generer_mot_de_passe(longueur=10, inclure_chiffres=True, inclure_caracteres_speciaux=True):
    # Définir les caractères possibles pour le mot de passe
    caracteres = string.ascii_letters  

    if inclure_chiffres:
        caracteres += string.digits  

    if inclure_caracteres_speciaux:
        caracteres += string.punctuation  

    # Générer le mot de passe aléatoire 
    mot_de_passe = ''.join(random.choice(caracteres) for i in range(longueur))
    
    return mot_de_passe


mot_de_passe = generer_mot_de_passe(longueur=16)
print("Mot de passe généré :", mot_de_passe)
