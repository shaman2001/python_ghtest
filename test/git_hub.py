# -*- coding: utf-8 -*-

#from selenium.webdriver.common.keys import Keys

def test_GitHubScript(app):
    success = True
    app.session.login(username="v.s.kotovich@gmail.com", password="qwerty123")
    app.group.different_actions()
    app.session.logout()
#    assertTrue(success)

def test_repo_qty(app):
    app.session.login(username="v.s.kotovich@gmail.com", password="qwerty123")
    #print(app.group.get_repo_count_from_lbl())
    #print(app.group.get_repo_count_from_list())
    assert app.group.get_repo_count_from_lbl() == app.group.get_repo_count_from_list()
    app.session.logout()
