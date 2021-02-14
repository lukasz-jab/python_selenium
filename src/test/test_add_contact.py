import pytest
import random
import string
from src.model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data= [
    Contact(firstname=random_string("name", 10), lastname=random_string("name", 10), homephone="1+1+1 1", mobilephone="2-2-2 2",
                      workphone="(3(3)3) 3", address=random_string("adress", 30), notes=random_string("notes", 50))
    for i in range(3)]


@pytest.mark.parametrize("contact", test_data, ids=[str(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacs_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacs_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
