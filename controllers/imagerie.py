from json import dump
from json import load
from os import path
from datetime import date
from controllers.image import Image
from utils.generator import idGenerator
from controllers.patient import Patient


class Imagerie:

    def __init__(self, typeImagerie = "", description = "", partieDuCorps = "", etatUrgence = 0):
        #attribut
        self.numero = idGenerator()
        self.date = date.today().strftime("%d/%m/%Y")
        self.description = description
        self.etatUrgence = etatUrgence
        self.typeImagerie = typeImagerie
        self.partieDuCorps = partieDuCorps


    # Enregistrer un nouveau ...
    def nouvelImagerie(self, patient, image):
        # Definition de patient et image
        image = Image(image.format, image.contraste, image.luminiosite, image.image)
        patient = Patient(patient.nom, patient.prenom, patient.age, patient.sexe)

        # Ajout de patient et image
        image = image.enregistrerImage()
        patient = patient.ajouterPatient()

        # Eneregstrer l'imagerie
        if path.exists('data/imagerie.json'):
            # Get if already exist data from imagerie.json to append
            with open('data/imagerie.json', 'r+') as fImageries:
                try: 
                    imageries = load(fImageries)
                except:
                    imageries = {'Imageries': []}
            fImageries.close()
        else:
            imageries = {'Imageries': []}

        # Define
        imagerie = {
            "numero": self.numero,
            "date": self.date,
            "typeImagerie": self.typeImagerie,
            "description": self.description,
            "partieDuCorps": self.partieDuCorps,
            "etatUrgence": self.etatUrgence,
            "image": image,
            "patient": patient
        }
        # Append the new Imagerie
        imageries['Imageries'].append(imagerie)

        # Store imagerie
        with open('data/imagerie.json', 'w') as fimageries:
            dump(imageries, fimageries)
        fimageries.close()

        return imageries

    
    #Liste des imageries
    def listeImageries(self):
        with open('data/imagerie.json') as fimageries:
            imageries = load(fimageries)
        fimageries.close()
        return imageries


    #Trouver une imagerie
    def trouverUneImagerie(self): 
        # Will be available on next update
        return 

