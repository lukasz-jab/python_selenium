# -*- coding: utf-8 -*-
from src.model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups_list()
    group = Group(name="group name 1", header="group header 1", footer="group footer 1")
    app.group.create(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_groups_list()
    group = Group(name="", header="group header 1", footer="group footer 1")
    app.group.create(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
