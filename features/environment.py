import behave_webdriver
# from selenium.webdriver.chrome.options import Options

# def before_all(context):
#     # Set up the Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Running in headless mode
    
#     # You can add a timeout setting directly if needed
#     context.behave_driver = behave_webdriver.Chrome(options=chrome_options)
#     context.behave_driver.implicitly_wait(35)
#     context.behave_driver.set_page_load_timeout(10)

def before_all(context):
    context.behave_driver = behave_webdriver.Chrome.headless()
    #context.behave_driver = behave_webdriver.Chrome()

def after_all(context):
    context.behave_driver.quit()
