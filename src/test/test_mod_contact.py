from src.model.contact import Contact
from datetime import datetime

def test_mod_contact(app):
    app.session.login("admin", "secret")
    app.contact.fill_form(Contact(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ",""
                                   + str(datetime.now()) + " ","" + str(datetime.now())
                                  + " ", " " + str(datetime.now())), modify=True)
    app.contact.submit_form()
    app.session.logout()