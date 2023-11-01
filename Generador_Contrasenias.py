import random
import string


def gen_contrasenia(longitud):
    caracteres = string.ascii_letters + string.digits
    contrasenia = "".join(random.choice(caracteres) for i in range(longitud))
    return contrasenia
