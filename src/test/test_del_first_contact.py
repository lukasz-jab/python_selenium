def test_del_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.delete()
    app.session.logout()
