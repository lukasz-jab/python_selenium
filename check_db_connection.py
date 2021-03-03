from src.fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="admin", password="password")

try:
    groups = db.get_group_list()
    for g in groups:
        print(g)
finally:
    pass

try:
    contacts = db.get_contact_list()
    for c in contacts:
        print(c)
finally:
    pass
