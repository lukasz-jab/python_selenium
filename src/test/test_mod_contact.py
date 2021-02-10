from datetime import datetime

from src.model.contact import Contact


def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact("Precond name", "Precond last", "Precon address", "00000", " Precond notes notes notes"))

    old_contacts = app.contact.get_contacs_list()
    contact = Contact(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ", ""
                      + str(datetime.now()) + " ", "" + str(datetime.now())
                      + " ", " " + str(datetime.now()))
    contact.id = old_contacts[0].id
    app.contact.modify(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacs_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
