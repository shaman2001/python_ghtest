

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def different_actions(self):
        #select repo
        wd = self.app.wd
        wd.find_element_by_xpath(".//span[text()='python_ghtest']").click()
        #press button "Clone or download"
        wd.find_element_by_xpath(".//span[text()='Clone or download']").click()
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

    def get_repo_count_from_lbl(self):
        wd = self.app.wd
        return int(wd.find_element_by_xpath(".//div[@id='your_repos']/h3/span[@class='counter']").text)

    def get_repo_count_from_list(self):
        wd = self.app.wd
        repo_list = wd.find_elements_by_xpath(".//ul[@id='repo_listing']/li[@class='public source']")
        repo_count = len(repo_list)
        return repo_count
