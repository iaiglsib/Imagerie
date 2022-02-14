from os import path
from json import load
from json import dump
from datetime import date
from utils.generator import idGenerator

class Image:

    def __init__(self, formatImage = "", contraste = 0, luminiosite = 0, image = ""):

        self.numero = idGenerator()
        self.format = formatImage
        self.contraste = contraste
        self.luminiosite = luminiosite
        self.image = image
        self.date = date.today().strftime("%d/%m/%Y")
    

    # Enregistrer une image
    def enregistrerImage(self):
        if path.exists('data/image.json'):
            # Try get data if already exist for update
            with open('data/image.json', 'r+') as fimages:
                try: 
                    images = load(fimages)
                except:
                    images = {'Images': []}
            fimages.close()
        else:
            images = {'Images': []}

        # Define patient
        image = {
            "numero": self.numero,
            "format": self.format,
            "contraste": self.contraste,
            "luminiosite": self.luminiosite,
            "image": self.image,
            "date": self.date 
        }
        images['Images'].append(image)

        # Try to dump data to patient.json
        with open('data/image.json', 'w') as fimages:
            dump(images, fimages)
        fimages.close()

        return image