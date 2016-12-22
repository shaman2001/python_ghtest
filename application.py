from selenium.webdriver.chrome.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver(executable_path='/home/shaman/mywebdrivers/chromedriver')
        self.wd.implicitly_wait(60)

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
        wd.find_element_by_link_text("PyGithubTest").click()
        wd.back()

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath("//ul[@id='user-links']/li[3]/a").click()
        wd.find_element_by_css_selector("button.dropdown-item.dropdown-signout").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_link_text("Sign in").click()
        wd.find_element_by_id("login_field").clear()
        wd.find_element_by_id("login_field").send_keys(username)
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_name("commit").click()

    def open_login_page(self):
        wd = self.wd
        wd.get("https://github.com/")

    def destroy(self):
        self.wd.quit()
