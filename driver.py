from selenium.webdriver import Chrome, ChromeOptions
import chromedriver_binary


def create_test_driver(options=ChromeOptions()):
    return Chrome(options=options)


def create_driver():
    options = ChromeOptions()
    options.add_argument('--headless')
    return create_test_driver(options)
