def mystery_2(a):
    """Provides the count of number of characters in a string

    Parameters:
        a: string

    Returns -> int being the count of characters in a string

    Raises:
        AssertionError: if the arguments are not a string

    >>> mystery_2("Test")
    4

    >>> mystery_2("Muqaddas")
    8

    >>> mystery_2("Muqaddas Rehman")
    15
    """
    assert isinstance(a, str), "a is string"
    
    if len(a) == 0:
        return None

    return len(a)
