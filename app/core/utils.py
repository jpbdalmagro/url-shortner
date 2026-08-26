import string

from secrets import choice


alphabet = string.ascii_letters + string.digits


def gen_code():
    return "".join(choice(alphabet) for _ in range(6))
