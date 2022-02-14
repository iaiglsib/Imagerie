from string import ascii_uppercase
from string import digits
import random


# Generer un numero pour le patient enregistré
def idGenerator(size = 10, chars=ascii_uppercase + digits):
    chaine = ''.join(random.choice(chars) for _ in range(size))
    chaine = random.sample(chaine, len(chaine))
    chaine = ''.join([str(item) for item in chaine])

    return chaine