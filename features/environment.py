import behave_webdriver

def before_all(context):
    context.behave_driver = behave_webdriver.Chrome.headless()
    context.behave_driver.set_window_size(1920,1080) #only use if in headless mode 
    #context.behave_driver = behave_webdriver.Chrome()

def after_all(context):
    context.behave_driver.quit()
