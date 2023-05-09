# Certains mots se retrouvent très fréquemment dans la langue française. En anglais, on les 
# appelle les « stop words ». Ces mots, bien souvent, n’apportent pas d’information dans les 
# tâches suivantes. Lorsque l’on effectue par exemple une classification par la méthode Tf-IdF, on 
# souhaite limiter la quantité de mots dans les données d’entraînement.

# Les « stop words » sont établis comme des listes de mots. Ces listes sont 
# généralement disponibles dans une librairie appelée NLTK (Natural Language
# Tool Kit), et dans beaucoup de langues différentes.
# Voir l'adresse suivante pour plus d'informations : https://www.stat4decision.com/fr/traitement-langage-naturel-francais-tal-nlp/


# Le stemming consiste à réduire un mot dans sa forme “racine”. 
# Le but du stemming est de regrouper de nombreuses variantes d’un mot
# comme un seul et même mot. Par exemple, une fois que l’on applique un
# stemming sur “Chiens” ou “Chien”, le mot résultant est le même. Cela 
# permet notamment de réduire la taille du vocabulaire


import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer

import numpy 
# import tflearn
# import tensorflow

import random
import json

with open("intents.json") as file :
    data = json.load(file)
    
print(data)
