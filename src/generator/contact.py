import os
import random
import string
from src.model.contact import Contact
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a
    else:
        assert False, "unhandled option"

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data= [
    Contact(firstname=random_string("name", 10), lastname=random_string("name", 10), homephone="1+1+1 1", mobilephone="2-2-2 2",
                      workphone="(3(3)3) 3", address=random_string("adress", 30), notes=random_string("notes", 50))
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f)

with open(file, "w") as out:
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))