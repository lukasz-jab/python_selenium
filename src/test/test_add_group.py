# -*- coding: utf-8 -*-
from src.model.group import Group


def test_add_group(app):
    app.group.create(Group("group name 1", "group header 1", "group footer 1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
