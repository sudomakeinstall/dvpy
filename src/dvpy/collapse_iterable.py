from collections import Iterable


def collapse_iterable_imp(container):
    """
    https://stackoverflow.com/a/40857703/1544627
    """
    for i in container:
        if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
            yield from collapse_iterable_imp(i)
        else:
            yield i


def collapse_iterable(container):
    """
    Collapse (i.e., flatten) a nested collection of iterables into a single list.
    """
    return list(collapse_iterable_imp(container))
