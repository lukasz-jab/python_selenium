import random
import string
from src.model.group import Group

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*7
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
             for i in range(3)]

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="*name2+", header="?header2/", footer="=footer2>")
    ]
