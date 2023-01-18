from behave import *


@Given("Home page: I am on the-internet.herokuapp.com")
def step_impl(context):
	context.home_page_object.navigate_to_homepage()


@When('Home page: I look for "{element}" and I click on it')
def step_impl(context, element):
	context.home_page_object.click_on_element(element)


@Then('I am on the "{element_page}" page')
def step_impl(context, element_page):
	context.home_page_object.check_current_page(element_page)