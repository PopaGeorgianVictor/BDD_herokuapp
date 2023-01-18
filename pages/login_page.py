from browser import Browser
from selenium.webdriver.common.by import By


class Login_page(Browser):
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button')
    LOGIN_PAGE = 'https://the-internet.herokuapp.com/secure'
    MESSAGE_PLACE = (By.ID, 'flash')
    MESSAGE_TEXT = 'You logged out of the secure area!'

    def enter_username(self, user):
        self.driver.find_element(*self.USERNAME).send_keys(user)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def check_login_success(self):
        current_url = self.driver.current_url  # we get the url at the page we ended up after the click
        assert current_url == self.LOGIN_PAGE, f"Error, we expected the url: {self.LOGIN_PAGE}, but we got: {current_url}"

    def check_logout_success(self):
        message_received = self.driver.find_element(*self.MESSAGE_PLACE).text
        assert self.MESSAGE_TEXT in message_received.strip(), f"Error, expected the message(logout): {self.MESSAGE_TEXT}, but we got: {message_received}"
