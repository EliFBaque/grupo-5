string = "Cambiando to upper case o LOWER CASE"

def changeFont(string):
    """Intercambia el las minisculas a mayusculas y viceversa"""
    swap = string.swapcase()
    return swap

def replaceSpaceByGuion(string):
    """ Funcion que reemplaza los espacios por guiones """
    return string.replace(" ","-")

print(changeFont(string))
