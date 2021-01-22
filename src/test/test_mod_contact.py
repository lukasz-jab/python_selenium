from src.model.contact import Contact
from datetime import datetime

def test_mod_contact(app):
    app.session.login("admin", "secret")
    app.navigation.open_contacts()
    app.contact.fill_form(Contact(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ",""
                                   + str(datetime.now()) + " ","" + str(datetime.now()) + " ", " " + str(datetime.now())))
    app.contact.submit_form()
    app.session.logout()