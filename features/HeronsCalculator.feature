Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro

Scenario: I can calculate the area of a triangle
    Given I open the url "https://byjus.com/herons-calculator/"
    When I set "6" to the inputfield "//*[@id='a']"
    And I set "8" to the inputfield "//*[@id="b"]"
    And I set "10" to the inputfield "//*[@id="c"]"
    And I click on the button "//*[@id="post-948257"]/div[1]/p[5]/input"
    Then I expect that element "//*[@id='_d']" contains the text "24"
