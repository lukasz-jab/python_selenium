from src.model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact("lukasz", "jab", "polska", "555555", "notes notes notes"))

