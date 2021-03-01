import random
from datetime import datetime

from src.model.group import Group


def test_mod_group(app, db):
    if len(db.get_groups_list()) == 0:
        app.group.create(Group("Precondiction Group name", "Precondition Group header", "Precongition Group footer"))
    old_groups = db.get_groups_list()
    group = Group(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ", ""
                  + str(datetime.now()))
    modyfied_group = random.choice(old_groups)
    app.group.modify_some_group_by_id(modyfied_group.id, group)
    # in application, in 9.0 version, is bug after updating a group:
    # Invalid ID.
    # return to the group page
    new_groups = db.get_groups_list()
    old_groups.remove(modyfied_group)
    group.set_id(modyfied_group.id)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
