from src.model.group import Group
from datetime import datetime

def test_mod_group(app):
    app.group.create(Group(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ",""
                           + str(datetime.now())))
    #in application, in 9.0 version, is bug after updating a group:
    # Invalid ID.
    # return to the group page
