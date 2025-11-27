def validate_length(length):
    if length < 4:
        raise ValueError ("Password length must be atleast 4 characters long!")
    return True


def validate_choices(include_lower, include_upper, include_digits, include_symbols):
    if not any([include_lower, include_upper, include_digits, include_symbols]):
        raise ValueError("You must select atleast one character type.")
    return True
