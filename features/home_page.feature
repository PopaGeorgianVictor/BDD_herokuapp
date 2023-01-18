Feature: Testing access to /login page of herokuapp

  Background:
    Given Home page: I am on the-internet.herokuapp.com

    @Home
  Scenario Outline: Check that the user can have  access on  different pages
    When Home page: I look for "<page to be open>" and I click on it
    Then I am on the "<accessed_site>" page
    Examples:
      | page to be open       | accessed_site                                               |
      | Form Authentication   | https://the-internet.herokuapp.com/login                         |
      | Forgot Password       | https://the-internet.herokuapp.com/forgot_password               |
      | Notification Messages | https://the-internet.herokuapp.com/notification_message_rendered |