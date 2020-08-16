# des_crypter_decrypter

Projet d'examen de **Sécurité informatique** pour les étudiants en L2 Genie informatique à l'**Université de Kinshasa** pour la promotion 2018-2019  
Ce projet est realisé par l'étudiant **NONGA MAHUKOLA Michéé**  

## Outils
- Python 3.6 et au dessus  
- Installer la bibliotheque python **pycryptodomex**  
  ````$ pip3 install pycryptodomex````

## Lancer l'application

````$ python3 des_crypter_decrypter.py text à crypter````

# A propos du DES (Data Encryption Standard)[https://fr.wikipedia.org/wiki/Data_Encryption_Standard]

Le Data Encryption Standard (DES, prononcer /dɛs/) est un algorithme de chiffrement symétrique (chiffrement par bloc) utilisant des clés de 56 bits. Son emploi n'est plus recommandé aujourd'hui, du fait de sa lenteur à l'exécution et de son espace de clés trop petit permettant une attaque systématique en un temps raisonnable. Quand il est encore utilisé c'est généralement en Triple DES, ce qui ne fait rien pour améliorer ses performances. DES a notamment été utilisé dans le système de mots de passe UNIX.  

### Caractéristiques
- Taille(s) du bloc :	64 bits
- Longueur(s) de la clé :	56 bits
- Structure	: schéma de Feistel
- Nombre de tours :	16 tours du DES

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
