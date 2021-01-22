import pytest
from src.fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_del_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.delete()
    app.session.logout()
