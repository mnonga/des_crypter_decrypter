# -*- coding: utf-8 -*-
"""
***************************************************************
                  TP DE SECURITE INFORMATIQUE
                     L2 GENIE INFORMATIQUE
                    by NONGA MAHUKOLA Michée

        PROGRAMME QUI APPLIQUE L'ALGORITHME DES EN MODE CBC
***************************************************************

"""

# pip3 install pycryptodomex
from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import unpad, pad
from Cryptodome.Random import get_random_bytes
# pour les arguments passés en ligne de commande
import sys

# Verifier si on a fourni le texte à chiffrer
if len(sys.argv)==1:
    print("Usage : \n\t", sys.argv[0], "<TEXTE A CHIFFRER>")
    exit(1)

user_text = " ".join(sys.argv[1:])
text_clair = user_text 

cle = get_random_bytes(DES.key_size) # 8 bytes pour la clé du DES
iv = get_random_bytes(8) # 8 bytes pour le mode CBC

cipher1 = DES.new(cle, DES.MODE_CBC, iv)
text_chiffre = cipher1.encrypt(pad(text_clair.encode('utf-8'), DES.block_size))

cipher2 = DES.new(cle, DES.MODE_CBC, iv)
text_dechiffre = unpad(cipher2.decrypt(text_chiffre), DES.block_size)

print(__doc__)
print("Texte clair       :", text_clair)
print("Texte chiffré     :", text_chiffre.hex())
print("Texte dechiffré   :", text_dechiffre.decode('utf-8'))
print("Decryptage reussi ?", 'Oui' if text_dechiffre==text_clair.encode('utf-8') else 'Non')
