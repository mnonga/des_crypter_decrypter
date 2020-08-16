# des_crypter_decrypter

Projet d'examen de **Sécurité informatique** pour les étudiants en L2 Genie informatique à l'**Université de Kinshasa** pour la promotion 2018-2019  
Ce projet est realisé par l'étudiant **NONGA MAHUKOLA Michéé**  

## Outils
- Environnement : Python 3.6 et au dessus  
- Installer la bibliotheque python **pycryptodomex**  
  ````$ pip3 install pycryptodomex````

## Lancer l'application

````$ python3 des_crypter_decrypter.py text à crypter````

# A propos du DES (Data Encryption Standard)[https://fr.wikipedia.org/wiki/Data_Encryption_Standard]
**Le Data Encryption Standard (DES)** est un algorithme de chiffrement symétrique (chiffrement par bloc) utilisant des clés de 56 bits.
### Caractéristiques
- Taille(s) du bloc :	64 bits
- Longueur(s) de la clé :	56 bits
- Structure	: schéma de Feistel  
![Schéma de Feistel](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Sch%C3%A9ma_de_Feistel.svg/299px-Sch%C3%A9ma_de_Feistel.svg.png)
- Nombre de tours :	16 tours du DES
- Attaques :	Cryptanalyse, Attaque par force brute, Linéaire / Différentielle
Dans le mode **Cipher Block Chaining (CBC)**, on applique sur chaque bloc un **OU exclusif** avec le chiffrement du bloc précédent avant qu’il soit lui-même chiffré. De plus, afin de rendre chaque message unique, un vecteur d'initialisation (IV) est utilisé.

# Details de l'implementation

````python
# la classe DES permet d'utiliser l'algorithme DES (Data Encryption Standard)
from Cryptodome.Cipher import DES

# les outils de padding rendent possible de chiffrer un text clair dont la longueure n'est pas multiple de 8
from Cryptodome.Util.Padding import unpad, pad

# pour generer un tableau de bytes de manière aleatoire
from Cryptodome.Random import get_random_bytes

# pour les arguments passés en ligne de commande
import sys

# recuperer le texte passé en paramètre
user_text = " ".join(sys.argv[1:])

# generer une clé et un vecteur d'initialisation
cle = get_random_bytes(DES.key_size) # 8 bytes pour la clé du DES
iv = get_random_bytes(8) # 8 bytes pour le mode CBC

# voir les codes pour la suite ...
````
