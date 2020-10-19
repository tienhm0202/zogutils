import string
from datetime import time


def unique_id(length: int = 5, prefix: str = '2EC') -> str:
    """
    Generate anonymous id follow convention: ANON_[0-9]{9}

    :param prefix: prefix of ID
    :param length: length of random number
    >>> import re
    >>> pattern = r"ANON_[0-9]{5}[A-Z]{1}"
    >>> m = re.compile(pattern).match(unique_id(prefix="ANON_"))
    >>> assert m
    >>> pattern = r"2EC[0-9]{100}[A-Z]{1}"
    >>> m = re.compile(pattern).match(unique_id(100))
    >>> assert m
    """
    ts = str(time()).replace(".", "")
    rand_int = int(ts[-1])
    if length > len(ts):
        rand_str = ts.zfill(length)
    else:
        rand_str = ts[:length]
    return prefix + rand_str + string.ascii_uppercase[rand_int]
