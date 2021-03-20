from pytest_bdd import given, when, then
import pytest
from src.model.group import Group

@pytest.fixture
@given("a group list")
def group_list(db):
    return db.get_groups_list()

@pytest.fixture()
@given("a group with <name>, <header> and <footer>")
def new_group(name, header, footer):
    return (Group(name=name, header=header, footer=footer))


@when("I add a group to the list")
def add_group(app, new_group):
    app.group.create(new_group)


@then("a new group list is equal to the old list with added a new group")
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_groups_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

