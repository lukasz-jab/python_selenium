import pytest
from src.fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_del_first_group(app):
    app.session.login("admin", "secret")
    app.navigation.open_groups()
    app.group.delete()
    app.navigation.open_groups()
    app.session.logout()
