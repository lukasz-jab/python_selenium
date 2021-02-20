import pytest
from src.model.contact import Contact
from data.add_contact import test_data


@pytest.mark.parametrize("contact", test_data, ids=[str(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacs_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacs_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
