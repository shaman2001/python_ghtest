# -*- coding: utf-8 -*-

from application import Application
import pytest
#from selenium.webdriver.common.keys import Keys


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_GitHubScript(app):
    success = True
    app.open_login_page()
    app.login(username="v.s.kotovich@gmail.com", password="qwerty123")
    app.different_actions()
    app.logout()
#    assertTrue(success)
