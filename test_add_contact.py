import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixtures = Application()
    request.addfinalizer(fixtures.destroy)
    return fixtures


def test_add_contact(app):
    app.login("admin", "secret")
    app.fill_contact_form(Contact("lukasz", "jab", "polska", "555555", "notes notes notes"))
    app.logout()
