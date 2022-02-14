from asyncio import constants
from os import path
from json import load
from json import dump
from utils.generator import idGenerator

class Patient:

    def __init__(self = "", nom = "", prenom = "", age = 0, sexe = ""):

        self.numero = idGenerator()
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe

    # Ajouter un patient
    def ajouterPatient(self):
        if path.exists('data/patient.json'):
            # Try get data if already exist for update
            with open('data/patient.json', 'r+') as fpatients:
                try: 
                    patients = load(fpatients) 
                except:
                    patients = {'Patients': []}
            fpatients.close()
        else:
            patients = {'Patients': []}

        # Define patient
        patient = {
            "numero": self.numero,
            "nom": self.nom,
            "prenom": self.prenom,
            "age": self.age,
            "sexe": self.sexe
        }
        patients['Patients'].append(patient)

        # Try to dump data to patient.json
        with open('data/patient.json', 'w') as fpatients:
            dump(patients, fpatients)
        fpatients.close()

        return patient




    # Afficher la liste des patients
    def listePatients(self):

        with open('data/patient.json') as fpatients:
            patients = load(fpatients)
        fpatients.close()
        return patients


    # Trouver un patient grace a son numero
    def trouverPatients(self, numero):

        with open('data/patient.json') as fpatients:
            patients = load(fpatients)['Patients']
        fpatients.close()

        for i in range(len(patients)):
            patient = patients[i]
            numeroPatient = patient.get('numero')
            if numeroPatient == numero:
                return patient
            else:
                if((i == (len(patients) -1)) and (numeroPatient == patient.get('numero'))):
                    return {"erreur": "Ce patient n'existe pas"}

        # for patient in patients:
        #     numeroPatient = patient.get('numero')
        #     if numeroPatient == numero:
        #         return patient
        #     else:
        #         return {"erreur": "Ce patient n'existe pas"}

    def patientGenerate(self):
        for i in range(100):
            if path.exists('data/patient.json'):
            # Try get data if already exist for update
                with open('data/patient.json', 'r+') as fpatients:
                    try: 
                        patients = load(fpatients) 
                    except:
                        patients = {'Patients': []}
                fpatients.close()
            else:
                patients = {'Patients': []}
            # Define patient
            patient = {
                "numero": self.numero,
                "nom": self.nom,
                "prenom": self.prenom,
                "age": self.age,
                "sexe": self.sexe
            }
            patients['Patients'].append(patient)

            # Try to dump data to patient.json
            with open('data/patient.json', 'w') as fpatients:
                dump(patients, fpatients)
            fpatients.close()

patient = Patient()

# print(patient.sexe)

# patient.ajouterPatient()

# print(patient.listePatients())

# print(patient.trouverPatients("RVVXI4ZQ95"))