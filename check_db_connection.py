from src.fixture.orm import ORMFixture
from src.model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="admin", password="password")

try:
    l = db.get_contact_not_in_group(Group(id=476))
    for item in l:
        print(item)
finally:
    pass



# try:
#     groups = db.get_group_list()
#     for g in groups:
#         print(g)
# finally:
#     pass
#
# try:
#     contacts = db.get_contact_list()
#     for c in contacts:
#         print(c)
# finally:
#     pass