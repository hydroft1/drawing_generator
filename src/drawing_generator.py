"""
Ce module contient trois classes pour créer des images avec des traits aléatoires et des couleurs aléatoires.

Classes:
    - CouleursAleatoires: Génère une liste de couleurs aléatoires.
    - TraitsAleatoires: Dessine des traits aléatoires sur une image.
    - ImageAleatoire: Récupère une image aléatoire à partir de l'API Unsplash.

Utilisation:
    Pour créer une image aléatoire avec des traits aléatoires, utilisez la classe ImageAleatoire pour obtenir une image aléatoire depuis l'API Unsplash, puis créez une instance de TraitsAleatoires avec cette image et le nombre de traits souhaité. Ensuite, appelez la méthode dessiner() pour dessiner les traits aléatoires sur l'image. Enfin, sauvegardez l'image résultante avec la méthode save() et affichez-la avec la méthode show().

Exemple d'utilisation:
    access_key = 'SlBMO4Rjm4OYptsHk4R1yowTSHd7kKhfIFscPsl5jig'
    image_generator = ImageAleatoire(access_key)
    image = image_generator.get_random_image()

    img = Image.open("projet2_img.png")
    ctx = ImageDraw.Draw(img)

    nb_traits = random.randrange(250, 350)
    couleurs = CouleursAleatoires(nb_traits)

    traits = TraitsAleatoires(img, nb_traits, couleurs)
    traits.dessiner()

    img.save('dessin.png')
    img.show('dessin.png')

Note:
    Assurez-vous d'obtenir une clé d'accès valide à l'API Unsplash pour que le code puisse fonctionner correctement. Le nombre de traits peut être ajusté en modifiant la plage passée à random.randrange().
"""

import random
from PIL import Image, ImageDraw
from io import BytesIO
import requests

class CouleursAleatoires:
    """
    Génère une liste de couleurs aléatoires.

    Attributes:
        nombre_couleurs (int): Le nombre de couleurs aléatoires à générer.
    """

    def __init__(self, nombre_couleurs):
        self.nombre_couleurs = nombre_couleurs
        self.couleurs_random = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(self.nombre_couleurs)]

    def obtenir_couleur_aleatoire(self):
        """
        Retourne une couleur aléatoire parmi celles générées.

        Returns:
            Tuple[int, int, int]: Un tuple représentant une couleur au format (R, G, B).
        """
        return random.choice(self.couleurs_random)


class TraitsAleatoires:
    """
    Dessine des traits aléatoires sur une image.

    Attributes:
        image (PIL.Image.Image): L'image sur laquelle les traits seront dessinés.
        nb_traits (int): Le nombre de traits à dessiner.
        gestion_couleur (CouleursAleatoires): L'instance de CouleursAleatoires pour la gestion des couleurs.

    Methods:
        dessiner: Dessine les traits aléatoires sur l'image.
    """

    def __init__(self, image, nb_traits, gestion_couleur):
        self.image = image
        self.dessin = ImageDraw.Draw(self.image)
        self.taille = image.size
        self.nombre_traits = nb_traits
        self.gestion_couleur = gestion_couleur

    def dessiner(self):
        """
        Dessine les traits aléatoires sur l'image.
        """
        centre_x, centre_y = self.taille[0] // 2, self.taille[1] // 2
        for _ in range(self.nombre_traits):
            x1 = centre_x + random.randint(-1200, 1200)
            y1 = centre_y + random.randint(-1200, 1200)
            x2 = centre_x + random.randint(-1200, 1200)
            y2 = centre_y + random.randint(-1200, 1200)
            couleur_aleatoire = self.gestion_couleur.obtenir_couleur_aleatoire()
            largeur = 1
            self.dessin.line([(x1, y1), (x2, y2)], fill=couleur_aleatoire, width=largeur)

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères de l'objet TraitsAleatoires.
        """
        return f"Traits aléatoires : Nombre de traits = {self.nombre_traits}"

class ImageAleatoire:
    """
    Récupère une image aléatoire à partir de l'API Unsplash.

    Attributes:
        access_key (str): La clé d'accès à l'API Unsplash.

    Methods:
        get_random_image: Récupère une image aléatoire depuis l'API Unsplash.

    Example:
        access_key = 'SlBMO4Rjm4OYptsHk4R1yowTSHd7kKhfIFscPsl5jig'
        image_generator = ImageAleatoire(access_key)
        image = image_generator.get_random_image()
    """

    def __init__(self, access_key):
        self.access_key = access_key

    def get_random_image(self):
        """
        Récupère une image aléatoire depuis l'API Unsplash.

        Returns:
            PIL.Image.Image: L'image récupérée depuis l'API Unsplash.
        """
        url = f"https://api.unsplash.com/photos/random/?client_id={self.access_key}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            image_url = data['urls']['regular']

            image_response = requests.get(image_url)
            image_data = image_response.content

            image = Image.open(BytesIO(image_data))
            image.save("projet2_img.png")

            return image
        else:
            print("Échec de la requête à l'API Unsplash.")
            return None
