import pytest

from src.fixture.application import Application
from src.model.contact import Contact


@pytest.fixture
def app(request):
    fixtures = Application()
    request.addfinalizer(fixtures.destroy)
    return fixtures


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.fill_form(Contact("lukasz", "jab", "polska", "555555", "notes notes notes"))
    app.session.logout()
