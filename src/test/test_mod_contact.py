from src.model.contact import Contact
from datetime import datetime

def test_mod_contact(app):
    app.contact.modify(Contact(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ",""
                                   + str(datetime.now()) + " ","" + str(datetime.now())
                                   + " ", " " + str(datetime.now())))
