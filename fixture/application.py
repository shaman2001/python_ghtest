from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        self.wd = WebDriver(executable_path='/home/shaman/mywebdrivers/chromedriver')
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)



    def destroy(self):
        self.wd.quit()
