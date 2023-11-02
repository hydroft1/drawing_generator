.. py:module:: random_image_generator

.. warning::
   **Assurez-vous d'obtenir une clé d'accès valide à l'API Unsplash.**

   **Assurez-vous d'avoir Pillow, io, installé requests sur votre ordinateur.**

Classes
=======

.. py:class:: CouleursAleatoires

    Classe pour générer une liste de couleurs aléatoires.

    :param int nombre_couleurs: Le nombre de couleurs aléatoires à générer.

    .. py:method:: __init__(self, nombre_couleurs)

        Initialise un objet CouleursAleatoires avec le nombre de couleurs à générer.

    .. py:method:: obtenir_couleur_aleatoire(self)

        Retourne une couleur aléatoire parmi celles générées.

        :returns: Tuple[int, int, int]
        :rtype: Un tuple représentant une couleur au format (R, G, B).

.. py:class:: TraitsAleatoires

    Classe pour dessiner des traits aléatoires sur une image.

    :param image: L'image sur laquelle les traits seront dessinés.
    :type image: PIL.Image.Image
    :param int nb_traits: Le nombre de traits à dessiner.
    :param gestion_couleur: L'instance de CouleursAleatoires pour la gestion des couleurs.
    :type gestion_couleur: CouleursAleatoires

    .. py:method:: __init__(self, image, nb_traits, gestion_couleur)

        Initialise un objet TraitsAleatoires avec une image, le nombre de traits et une instance de CouleursAleatoires.

    .. py:method:: dessiner(self)

        Dessine les traits aléatoires sur l'image.

    .. py:method:: __str__(self)

        Retourne une représentation sous forme de chaîne de caractères de l'objet TraitsAleatoires.

        :returns: Chaîne de caractères représentant l'objet.
        :rtype: str

.. py:class:: ImageAleatoire

    Classe pour récupérer une image aléatoire depuis l'API Unsplash.

    :param str access_key: La clé d'accès à l'API Unsplash.

    .. py:method:: __init__(self, access_key)

        Initialise un objet ImageAleatoire avec la clé d'accès à l'API Unsplash.

    .. py:method:: get_random_image(self)

        Récupère une image aléatoire depuis l'API Unsplash.

        :returns: L'image récupérée depuis l'API Unsplash.
        :rtype: PIL.Image.Image

Utilisation
======================

Exemple d'utilisation :

.. code-block:: python

    access_key = 'votre clé d’accès valide à l’API Unsplash'
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

