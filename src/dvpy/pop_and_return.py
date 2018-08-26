# System

# Third Party

# Internal


def pop_and_return(l, n):
    """
    Delete the `n`th element from the supplied list `l` and return the resulting list.
  
    :param l: The input list.
    :type l: list
  
    :param n: The index of the element to be removed.
    :type n: int
  
    :returns: A copy of the input list `l` with element `n` removed.
    :rtype: list
  
    :raises: `ValueError` if the index `n` is out of range.
             `ValueError` if the list `l` is empty.
    """
    o = l.copy()
    if (n >= len(l)) or (n < 0):
        raise ValueError("Index n = %d out of range" % (n))
    if len(l) == 0:
        raise ValueError("The supplied list must contain at least one element.")
    del o[n]
    return o
