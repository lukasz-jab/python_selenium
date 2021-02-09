from sys import maxsize


class Contact:
    def __init__(self, id=None, firstname=None, lastname=None, address=None, mobile=None, notes=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.mobile = mobile
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s, %s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
