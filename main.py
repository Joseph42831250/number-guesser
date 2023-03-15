import random

# Génération d'un nombre entre 0 et 1000 inclus
number = random.randint(0, 1000)
found = False

print("Vous devez trouver un nombre aléatoire entre 0 et 1000")

# Tant que le nombre n'est pas trouvé
while not found:
    print("Entez un nombre : ")
    # On demande à l'utilisateur d'entrer un nomnbre
    x = int(input())

    if x == number:
        found = True
    elif x < number:
        print("Le nombre doit être supérieur")
    else:
        print("Le nombre doit être inférieur")


print("Bravo! Vous avez trouvé le nombre.")