from src.model.contact import Contact
from src.model.group import Group


def test_group_list(app, db):
    ui_groups = app.group.get_groups_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    db_groups = db.get_groups_list()

    assert sorted(db_groups, key=Group.id_or_max) == sorted(ui_groups, key=Group.id_or_max)


def test_contact_list(app, db):
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip())

    db_contacts = map(clean, db.get_contacts_list())
    ui_contacts = map(clean, app.contact.get_contacs_list())

    assert sorted(db_contacts, key=Contact.id_or_max) == sorted(ui_contacts, key=Contact.id_or_max)

# print(timeit(lambda: app.group.get_groups_list(), number = 1))
# print(timeit(lambda: (map(clean, db.get_group_list())),number = 1))
