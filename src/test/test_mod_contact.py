from src.model.contact import Contact
from datetime import datetime

def test_mod_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify(Contact(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ",""
                                   + str(datetime.now()) + " ","" + str(datetime.now())
                                  + " ", " " + str(datetime.now())))
    app.session.logout()