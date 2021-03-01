import random

from src.model.contact import Contact


def test_del_some_contact(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(
            Contact("Precond name", "Precond last", "Precon address", "00000", " Precond notes notes notes"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    old_contacts.remove(contact)
    # after added refresh value ddepracated in database is changed
    app.navigation.open_home()
    new_contacts = db.get_contacts_list()
    assert old_contacts == new_contacts
