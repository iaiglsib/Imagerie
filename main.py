# from controllers.patient import Patient

# patient = Patient('LAWSON-HETCHELY', "Laté Seth", 18, "M")

# patient = patient.ajouterPatient()

# print(patient)

# from controllers.image import Image

# image = Image("png", 80, 50, 'source')

# im = image.enregistrerImage()
# print(im)
# from controllers.imagerie import Imagerie

# imagerie = Imagerie('png')

# from datetime import date

# today = date.today()

# # dd/mm/YY
# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)

# patient.ajouterPatient()

# print(patient.listePatients())

# print(patient.trouverPatients("UKSB3H2R85"))


from controllers.image import Image
from controllers.patient import Patient
from controllers.imagerie import Imagerie

patient = Patient("MODZINOU", "Leticia", 28, "F")
image = Image("png", 20, 40, "source") #Les sources des images seront traités apres

imagerie = Imagerie("scanner", "nothing", "seins", 0)

imagerie = imagerie.nouvelImagerie(patient, image)

print(imagerie)

# imagerie = Imagerie()

# imagerie = imagerie.listeImageries()

# print(imagerie)

