from src.model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("Precond name", "Precond last", "Precon address", "00000", " Precond notes notes notes"))
    app.contact.delete()

