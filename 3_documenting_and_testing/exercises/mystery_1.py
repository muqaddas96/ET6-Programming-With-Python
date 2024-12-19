def mystery_1(a,b):
    """Provides the sum of the two integers

    Parameters:
        a: int
        b: int

    Returns -> int being the sum of the two int provided

    Raises:
        AssertionError: if the arguments are not an integer

    >>> mystery_1(1,2)
    3

    >>> mystery_1(-5,4)
    -1

    >>> mystery_1(0,0)
    0
    """
    assert isinstance(a, int), "a is not an integer"
    assert isinstance(b, int), "b is not an integer"
    return a + b
