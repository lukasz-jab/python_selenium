import pymysql.cursors

from src.model.contact import Contact
from src.model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=self.host, database=self.name, user=self.user, password=self.password)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                groups.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups

    def get_contact_list(self):
        contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT id, firstname, lastname, address, home, mobile, work, email, notes, deprecated FROM addressbook")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, notes, deprecated) = row
                if deprecated == "0000-00-00 00:00:00":
                    contacts.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                            homephone=home, mobilephone=mobile, workphone=work, email_1=email,
                                            notes=notes))
        finally:
            cursor.close()

        return contacts
