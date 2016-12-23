# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application


#from selenium.webdriver.common.keys import Keys


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_GitHubScript(app):
    success = True
    app.session.login(username="v.s.kotovich@gmail.com", password="qwerty123")
    app.different_actions()
    app.session.logout()
#    assertTrue(success)
