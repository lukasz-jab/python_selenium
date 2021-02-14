# -*- coding: utf-8 -*-
import pytest
import random
import string
from src.model.group import Group

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*7
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



test_data = [Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10) ]
    for header in ["", random_string("header", 10)]
    for footer in ["", random_string("footer", 10)]
    ]

@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_groups_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)