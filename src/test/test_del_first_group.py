from random import randrange

from src.model.group import Group


def test_del_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Precondiction Group name", "Precondition Group header", "Precongition Group footer"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index:(index + 1)] = []
    assert old_groups == new_groups
