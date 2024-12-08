from behave_webdriver.steps import *
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#behave --tags=-@skip
#@skip

#And I click on the button "//*[@id="post-948257"]/div[1]/p[5]/input"

@when('I click on the element with the xpath "{xpath}"')
def step_click_on_element_with_xpath(context, xpath):
    element = context.behave_driver.find_element_by_xpath(xpath)
    element.click()

@when('I scroll down the page to element with the xpath "{xpath}"')
def step_scroll_down_to_element_with_xpath(context, xpath):
    context.behave_driver.scroll_to_element(xpath)

@when('I type "{text}" into the element with the xpath "{xpath}"')
def step_type_text_into_element_with_xpath(context, text, xpath):
    element = context.behave_driver.find_element_by_xpath(xpath)
    element.send_keys(text)

@then('I should see "{text}" text in the element with the xpath "{theXPath}"')
def step_verify_text_inside_element_with_xpath(context, text, theXPath):
    #element = context.behave_driver.get_element(theXPath, 'xpath')
    elements_text = context.behave_driver.get_element_text(theXPath) # or this works too element.text
    assert elements_text == text, f"Expected {text}, but found {elements_text}."


