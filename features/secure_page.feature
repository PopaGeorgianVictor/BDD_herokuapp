Feature: Testing access to '/secure' page of herokuapp and if info message is displayed on this pages

  Background:
    Given Home page: I am user on the-internet.herokuapp.com

  @Secure
  Scenario Outline:
    When Home page: I look for "<page to be open>" and I click on it
    When Login page: I enter "<username>" in the username text field
    When Login page: I enter "<password>" in the password text field
    When Login page: I click on login button
    When Secure page: I read the "You logged into a secure area!" message
    When Secure page: I click on logout button
    Then Secure page: I successfully enter on /secure page and info message You logged into a secure area! is displayed in a green tab
    Examples:
      | page to be open     | username | password             |
      | Form Authentication | tomsmith | SuperSecretPassword! |