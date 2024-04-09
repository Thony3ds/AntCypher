import json

def apply_custom_methode(x, methode):
    calcul = decode_methode(methode)
    to_return = int()
    # Remplacer 'x' dans l'expression par sa valeur
    expression = calcul.replace('x', str(x))

    # Évaluer l'expression
    try:
        resultat = eval(expression)
    except Exception as e:
        print(f"Error no correct methode: {e}")

def load_json_element(file_path, element_key):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return data.get(element_key)

def decode_methode(methode):
    return load_json_element(methode, "methode")

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
            print("Error: a unknown letter have been detected !")
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