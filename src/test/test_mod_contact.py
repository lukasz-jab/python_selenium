import random
from datetime import datetime

from src.model.contact import Contact


def test_mod_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(
            Contact("Precond name", "Precond last", "Precon address", " Precond notes notes notes"))

    old_contacts = db.get_contacts_list()
    contact = Contact(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ", ""
                      + str(datetime.now()) + " "
                      + " ", " " + str(datetime.now()))
    modyfied_contact = random.choice(old_contacts)
    app.contact.modify_by_id(modyfied_contact.id, contact)
    new_contacts = db.get_contacts_list()
    old_contacts.remove(modyfied_contact)
    contact.set_id(modyfied_contact.id)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacs_list(), key=Contact.id_or_max)