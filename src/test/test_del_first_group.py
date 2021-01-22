def test_del_first_group(app):
    app.session.login("admin", "secret")
    app.navigation.open_groups()
    app.group.delete()
    app.navigation.return_to_groups()
    app.session.logout()
