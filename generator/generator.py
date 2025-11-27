import random
from .config import LOWERCASE, UPPERCASE, DIGITS, SYMBOLS

def create_password(length, include_lower = True, include_upper = True,
                    include_digits = True, include_symbols = True):
    

    char_pool = ""


    if include_lower:
        char_pool += LOWERCASE
    if include_upper:
        char_pool += UPPERCASE
    if include_digits:
        char_pool += DIGITS
    if include_symbols:
        char_pool += SYMBOLS


    password = "".join(random.choice(char_pool) for _ in range(length))
    return password
