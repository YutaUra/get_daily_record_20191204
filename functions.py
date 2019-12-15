from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def try_wait_by(driver: WebDriver, by: By, target: str):
    while True:
        try:
            driver.find_element(by, target)
        except NoSuchElementException:
            sleep(0.2)
        else:
            break


def try_wait_by_loading(driver: WebDriver, by, target):
    while True:
        try:
            if not driver.find_element(by, target).is_displayed():
                break
        except NoSuchElementException:
            sleep(0.2)


def wait_all(driver: WebDriver):
    WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located)


def js_click(driver: WebDriver, by, target):
    el = driver.find_element(by, target)
    driver.execute_script("arguments[0].click();", el)
