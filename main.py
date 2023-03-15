import random

number = random.randint(0, 1000)
found = False

print("Vous devez trouver un nombre aléatoire entre 0 et 1000")

while not found:
    print("Entez un nombre : ")
    x = int(input())

    if x == number:
        found = True
    elif x < number:
        print("Le nombre doit être supérieur")
    else:
        print("Le nombre doit être inférieur")


print("Bravo! Vous avez trouvé le nombre.")