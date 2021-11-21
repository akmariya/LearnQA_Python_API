import string
import random


def random_str(length=None):
    if length is not None:
        return ''.join(random.choices(string.ascii_letters, k=length))
    else:
        return ''.join(random.choices(string.ascii_letters, k=5))
