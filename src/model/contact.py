from sys import maxsize


class Contact:
    def __init__(self, id=None, firstname=None, lastname=None, address=None, homephone=None, mobilephone=None,
                 workphone=None, fax=None, notes=None, all_phones_from_home_page=None, email_1=None, email_2=None,
                 email_3=None, all_emails=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.emial_1 = email_1
        self.emial_2 = email_2
        self.emial_3 = email_3
        self.all_emails = all_emails

    def __repr__(self):
        return "%s, %s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def set_id(self, id):
        self.id = id
