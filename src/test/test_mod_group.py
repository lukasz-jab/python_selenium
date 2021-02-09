from datetime import datetime

from src.model.group import Group


def test_mod_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Precondiction Group name", "Precondition Group header", "Precongition Group footer"))
    old_groups = app.group.get_groups_list()
    group = Group(" " + str(datetime.now()) + " ", "" + str(datetime.now()) + " ", ""
                  + str(datetime.now()))
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_groups_list()
    # in application, in 9.0 version, is bug after updating a group:
    # Invalid ID.
    # return to the group page
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
