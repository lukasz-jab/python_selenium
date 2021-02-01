from src.model.contact import Contact
from datetime import datetime

def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact("Precond name", "Precond last", "Precon address", "00000", " Precond notes notes notes"))

    app.contact.modify(Contact(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ",""
                                   + str(datetime.now()) + " ","" + str(datetime.now())
                                   + " ", " " + str(datetime.now())))
