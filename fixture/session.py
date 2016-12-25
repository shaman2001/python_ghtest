

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//ul[@id='user-links']/li[3]/a").click()
        wd.find_element_by_css_selector("button.dropdown-item.dropdown-signout").click()

    def login(self, username, password):
        wd = self.app.wd
        wd.get("https://github.com/")
        wd.find_element_by_link_text("Sign in").click()
        wd.find_element_by_id("login_field").clear()
        wd.find_element_by_id("login_field").send_keys(username)
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_name("commit").click()