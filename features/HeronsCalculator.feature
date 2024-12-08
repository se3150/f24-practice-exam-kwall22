Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro

@skip
Scenario: I can calculate the area of a triangle
    Given I open the url "https://byjus.com/herons-calculator/"
    When I set "6" to the inputfield "//*[@id='a']"
    And I set "8" to the inputfield "//*[@id="b"]"
    And I set "10" to the inputfield "//*[@id="c"]"
    And I click on the element with the xpath "//*[@id="post-948257"]/div[1]/p[5]/input"
    Then I expect that element "//*[@id='_d']" contains the text "24"
@skip
Scenario: Testing a few things out
    Given I open the url "https://byjus.com/herons-calculator/"
    When I scroll down the page to element with the xpath "//*[@id="comment-for-desktop"]/div[2]"
    And I type "hello" into the element with the xpath "//*[@id="comment"]"
    And I click on the element with the xpath "//*[@id="submit"]"
    Then I should see "Mobile No. is required." text in the element with the xpath "//*[@id="data-comment-form"]/div/div[1]/div/div[2]"

Scenario: Trying other things out 
    Given I open the url "https://byjus.com/herons-calculator/"
    When I move to element "//*[@id="header-secondary-menu"]/div[5]"
    Then I wait on element "//*[@id='header-secondary-menu']/div[5]/ul/li[1]" for 2000ms to be visible
    When I click on the element "//*[@id="header-secondary-menu"]/div[5]/ul/li[1]"
    Then I expect that element "/html/body/div[1]/div[1]/div[1]/div/div[4]/h1" contains the text "Addition Calculator"