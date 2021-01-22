from src.model.group import Group
from datetime import datetime

def test_mod_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ",""
                           + str(datetime.now())))
    app.session.logout()