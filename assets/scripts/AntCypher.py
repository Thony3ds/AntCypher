def decode_methode(methode): # TODO build function
    decoded_methode = []
    return decoded_methode

def creer_dictionnaire():
    dictionnaire = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for i, char in enumerate(alphabet):
        dictionnaire[char] = i
    return dictionnaire

def crypt(message, cle):
    dictionnaire = creer_dictionnaire()
    message_crypte = ''
    for index, lettre in enumerate(message):
        if lettre in dictionnaire:
            # Calculer la clé pour cette itération
            cle_iteration = cle + index
            # Récupérer le code du caractère dans le dictionnaire
            code_caractere = dictionnaire[lettre]
            # Appliquer l'équation à une inconnue avec la clé modifiée
            code_caractere = (code_caractere + cle_iteration) % len(dictionnaire)
            # Récupérer le caractère correspondant au nouveau code
            caractere_crypte = list(dictionnaire.keys())[list(dictionnaire.values()).index(code_caractere)]
            message_crypte += caractere_crypte
        else:
            message_crypte += lettre
    return message_crypte

def decrypt(message_crypte, cle):
    dictionnaire = creer_dictionnaire()
    message_clair = ''
    for index, lettre in enumerate(message_crypte):
        if lettre in dictionnaire:
            # Calculer la clé pour cette itération
            cle_iteration = cle + index
            # Récupérer le code du caractère dans le dictionnaire
            code_caractere = dictionnaire[lettre]
            # Appliquer l'équation inverse à une inconnue avec la clé modifiée
            code_caractere = (code_caractere - cle_iteration) % len(dictionnaire)
            # Récupérer le caractère correspondant au nouveau code
            caractere_clair = list(dictionnaire.keys())[list(dictionnaire.values()).index(code_caractere)]
            message_clair += caractere_clair
        else:
            message_clair += lettre
    return message_clair