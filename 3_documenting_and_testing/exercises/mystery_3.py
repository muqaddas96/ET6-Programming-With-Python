def mystery_3(a, b):
    """Takes in 2 numbers and return the smaller number if numbers are different and return sum if numbers are same.

    Parameters:
        a: int
        b: int

    Returns -> returns int being the smaller numer if input numbers are different and sum if number are same. 

    Raises:
        AssertionError: if the arguments are not integer.

    >>> mystery_3(2,3)
    2

    >>> mystery_3(-2, 0)
    -2

    >>> mystery_3(1,1)
    2
    """

    assert isinstance(a, int), "a is int"
    assert isinstance(b, int), "a is int"
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
