from src.model.contact import Contact

def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.fill_form(Contact("lukasz", "jab", "polska", "555555", "notes notes notes"), modify=False)
    app.session.logout()
