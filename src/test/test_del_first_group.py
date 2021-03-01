import random

from src.model.group import Group


def test_del_some_group(app, db):
    if len(db.get_groups_list()) == 0:
        app.group.create(Group("Precondiction Group name", "Precondition Group header", "Precongition Group footer"))
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = db.get_groups_list()
    old_groups.remove(group)
    assert old_groups == new_groups
