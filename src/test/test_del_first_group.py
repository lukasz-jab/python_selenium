from src.model.group import Group


def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Precondiction Group name", "Precondition Group header", "Precongition Group footer"))
    app.group.delete_first_group()

