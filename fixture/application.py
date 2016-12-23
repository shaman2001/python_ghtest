from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = WebDriver(executable_path='/home/shaman/mywebdrivers/chromedriver')
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def different_actions(self):
        #select repo
        wd = self.wd
        wd.find_element_by_css_selector("span.repo").click()
        #press button "Clone or download"
        wd.find_element_by_xpath(
            "//div[@class='repository-content']//button[normalize-space(.)='Clone or download']").click()
        wd.find_element_by_xpath("//div[@class='repository-content']//button[.='Use HTTPS']").click()
        wd.find_element_by_xpath("//div[@class='repository-content']//button[.='Use SSH']").click()
        wd.find_element_by_css_selector("div.modal-backdrop.js-touch-events").click()
        wd.back()
        wd.find_element_by_xpath("//ul[@id='user-links']/li[3]/a").click()
        # Open "Your profile" page
        wd.find_element_by_link_text("Your profile").click()
        # Open "PyGithubTest" project page
        wd.find_element_by_link_text("python_ghtest").click()
        wd.back()

    def destroy(self):
        self.wd.quit()
