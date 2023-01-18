from behave import *

@When('Secure page: I click on logout button')
def step_impl(context):
	context.secure_page_object.click_on_logout_button()

@When('Secure page: I successfully enter on /secure page and info message You logged into a secure area! is displayed in a green tab')
def step_impl(context):
	context.secure_page_object.check_login_to_secure_area()