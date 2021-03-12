import random

from src.fixture.orm import ORMFixture
from src.model.contact import Contact
from src.model.group import Group


def test_add_contact_to_group(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(
            Contact("Precond name", "Precond last", "Precon address", "00000", " Precond notes notes notes"))
    if len(db.get_groups_list()) == 0:
        app.group.create(Group("Precondiction Group name", "Precondition Group header", "Precongition Group footer"))

    db_orm = ORMFixture(host="127.0.0.1", name="addressbook", user="admin", password="password")

    groups = db_orm.get_group_list()
    for g in groups:
        if len(db_orm.get_contact_not_in_group(g)) > 0:
            contact = random.choice(db_orm.get_contact_not_in_group(g))
            app.contact.add_contact_to_group(contact, g)
            assert contact in db_orm.get_contact_in_group(g)
            app.contact.delete_contact_from_group(contact, g)
            assert contact not in db_orm.get_contact_in_group(g)
            print("IN IF")
            return
        else:
            app.contact.create(Contact(firstname="Contact"))
            app.navigation.open_contacts()
            contact = db.get_last_added_contact()
            group = random.choice(db.get_groups_list())
            app.contact.add_contact_to_group(contact, group)
            assert str(contact) in str(db_orm.get_contact_in_group(group))
            app.contact.delete_contact_from_group(contact, group)
            assert str(contact) not in str(db_orm.get_contact_in_group(group))
            print("IN ELSE")