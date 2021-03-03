import random

from src.fixture.orm import ORMFixture
from src.model.contact import Contact
from src.model.group import Group


def test_add_and_delete_contact_to_group(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(
            Contact("Precond name", "Precond last", "Precon address", "00000", " Precond notes notes notes"))
    if len(db.get_groups_list()) == 0:
        app.group.create(Group("Precondiction Group name", "Precondition Group header", "Precongition Group footer"))

    contact = random.choice(db.get_contacts_list())
    group = random.choice(db.get_groups_list())
    app.contact.add_contact_to_group(contact, group)

    db_orm = ORMFixture(host="127.0.0.1", name="addressbook", user="admin", password="password")

    assert str(contact) in str(db_orm.get_contact_in_group(group))

    #Removing added group from contact:
    app.contact.delete_contact_from_group(contact, group)

    assert str(contact) not in str((db_orm.get_contact_in_group(group)))

