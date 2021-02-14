from src.model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacs_list()
    contact = Contact(firstname="lukasz", lastname="jab", homephone="1+1+1 1", mobilephone="2-2-2 2",
                      workphone="(3(3)3) 3", address="polska", notes="notes notes notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacs_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
