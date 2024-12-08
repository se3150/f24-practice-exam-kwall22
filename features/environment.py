import behave_webdriver

def before_all(context):
    context.behave_driver = behave_webdriver.Chrome.headless()
    chrome_options = behave_webdriver.ChromeOptions()
    chrome_options.add_argument('window-size=1920x1080')
    #context.behave_driver = behave_webdriver.Chrome()

def after_all(context):
    context.behave_driver.quit()
