from browser import Browser
from selenium.webdriver.common.by import By


class Home_page(Browser):

    def navigate_to_homepage(self):
        self.driver.get("https://the-internet.herokuapp.com/")  # main webpage for the project

    def click_on_element(self, element):
        self.driver.find_element(By.LINK_TEXT, element).click()  # used to click on element

    def check_current_page(self, element_page):
        current_url = self.driver.current_url  # we get the url at the page we ended up after the click
        assert element_page == current_url, f"Error, the page expected is: {element_page}, but we got: {current_url}"
