from datetime import datetime
from random import randrange

from src.model.group import Group


def test_mod_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Precondiction Group name", "Precondition Group header", "Precongition Group footer"))
    old_groups = app.group.get_groups_list()
    group = Group(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ", ""
                  + str(datetime.now()))
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_some_group(index, group)
    # in application, in 9.0 version, is bug after updating a group:
    # Invalid ID.
    # return to the group page
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
