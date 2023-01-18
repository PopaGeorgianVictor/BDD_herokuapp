from behave import *


@given("Home page: I am user on the-internet.herokuapp.com")
def step_impl(context):
	context.home_page_object.navigate_to_homepage()


@when('Home page: I click on "<page to be open>"')
def step_impl(context, element):
	context.home_page_object.click_on_element(element)


@then('Home page: I am able to enter on the "<accessed_site>" page')
def step_impl(context, element_page):
	context.home_page_object.check_current_page(element_page)