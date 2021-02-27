from src.model.contact import Contact
from src.model.group import Group


def test_group_list(app, db):
    db_groups = app.group.get_groups_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    ui_groups = map(clean, db.get_group_list())

    assert sorted(db_groups, key=Group.id_or_max) == sorted(ui_groups, key=Group.id_or_max)


def test_contact_list(app, db):
    db_contacts = db.get_contact_list()

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip())

    ui_contacts = map(clean, app.contact.get_contacs_list())

    assert sorted(db_contacts, key=Contact.id_or_max) == sorted(ui_contacts, key=Contact.id_or_max)
