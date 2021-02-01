from src.model.group import Group
from datetime import datetime

def test_mod_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Precondiction Group name", "Precondition Group header", "Precongition Group footer"))
    app.group.modify_first_group(Group(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ",""
                           + str(datetime.now())))
    #in application, in 9.0 version, is bug after updating a group:
    # Invalid ID.
    # return to the group page
