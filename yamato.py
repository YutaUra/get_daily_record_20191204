import csv
import time
import os
from datetime import date

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

import functions as f
from credential import YAMATO_ID, YAMATO_PW
from driver import create_test_driver, create_driver
from logger import init_logging

logger = init_logging(__name__)


def login(driver):
    """login"""
    try:
        driver.get(
            'https://bmypage.kuronekoyamato.co.jp/'
            'bmypage/servlet/jp.co.kuronekoyamato.wur.hmp.servlet.user.HMPLGI0010JspServlet')
        f.try_wait_by(driver, By.NAME, 'CSTMR_CD')
        driver.find_element_by_name('CSTMR_CD').send_keys(YAMATO_ID)
        driver.find_element_by_name('CSTMR_PSWD').send_keys(YAMATO_PW)
        driver.find_element_by_class_name('nav-login-btn').find_element_by_tag_name('a').click()
    except Exception:
        logger.error('ログインに失敗しました。')
    else:
        logger.info('ログインしました。')


def wait_and_click(driver, by, target):
    try:
        f.try_wait_by(driver, by, target)
        driver.find_element(by, target).click()
    except Exception:
        logger.error('遷移に失敗しました。')
    else:
        logger.info('遷移に成功しました。')


def fetch(driver):
    today = date.today()
    try:
        f.try_wait_by(driver, By.ID, 'Search')
        f.try_wait_by_loading(driver, By.ID, 'indi_Set')
        driver.find_element_by_id('shipment_plan_from').clear()
        driver.find_element_by_id('shipment_plan_to').clear()
        driver.find_element_by_id('shipment_plan_from').send_keys(today.strftime('%Y/%m/%d'))
        driver.find_element_by_id('shipment_plan_to').send_keys(today.strftime('%Y/%m/%d'))
        f.try_wait_by_loading(driver, By.ID, 'indi_Set')
        f.js_click(driver, By.ID, 'Search')
        time.sleep(1.0)
    except Exception:
        logger.error('期間の指定に指定に失敗しました。')
    else:
        logger.info('期間の指定に成功しました。')

    try:
        Alert(driver).accept()
    except Exception:
        logger.info('データが存在しています。')
    else:
        logger.info('今日のデータはありません。')
        driver.close()
        return 1

    try:
        f.js_click(driver, By.CLASS_NAME, 'allCheck')
        f.js_click(driver, By.ID, 'issue_data_btn')

        f.wait_all(driver)
        iframe = driver.find_element_by_class_name('fancybox-iframe')
        f.try_wait_by_loading(driver, By.ID, 'indi_Set')
        time.sleep(1)
        driver.switch_to.frame(iframe)
        el = driver.find_element_by_id('output_file')
        time.sleep(1)
        driver.execute_script("arguments[0].click();", el)
    except Exception:
        logger.error('「ファイルに出力」に失敗しました。')
    else:
        logger.info('「ファイルに出力」に成功しました。')
    # wait for download
    while True:
        try:
            driver.find_element_by_xpath('//div[contains(text(),"ダウンロード準備が完了しました。")]')
        except Exception:
            time.sleep(1)
        else:
            break


def write_data(driver):
    today = date.today()
    file_dir = os.path.join('result', today.strftime('%Y%m%d'))
    os.makedirs(file_dir, exist_ok=True)

    data = driver.execute_script('return parent.exportDataList')
    with open(file_dir + '/yamato.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(data)
    logger.info('データの書き出しが完了しました。')


def main():
    driver = create_driver()
    login(driver)
    wait_and_click(driver, By.XPATH, '//*[@id="nav-sub-01"]/div[2]/ul/li/a')

    while True:
        try:
            driver.find_element_by_id('modalIframe')
        except Exception:
            break
        else:
            driver.refresh()

    f.try_wait_by_loading(driver, By.ID, 'loading_area')
    time.sleep(1)
    wait_and_click(driver, By.XPATH, '//*[@id="issue_search"]/div/a')

    if fetch(driver):
        return
    write_data(driver)
    driver.close()
