from typing import Tuple, Any

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:

    n = "нет"
    m = "мед.справка"
    o = "объяснительная"

    month_text = "Март"

    dolv = "14"
    dolv2 = 3

    PRIC = "" + o + ""

    link = "https://system.fgoupsk.ru/student/login"
    link2 = "https://system.fgoupsk.ru/student/?mode=ucheba&act=group&act2=prog&m=2&d=27"
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.ID, "input_id").send_keys("1027556")

    browser.find_element(By.ID, "input_password").send_keys("111111")

    browser.find_element(By.ID, "input_submit").click()

    browser.find_element(By.XPATH, "(//a[text()='Учёба'])").click()

    browser.find_element(By.XPATH, "(//a[text()='Группа'])").click()

    browser.find_element(By.XPATH, "(//a[text()='пропуски'])").click()

    browser.find_element(By.XPATH, "(//a[text()='" + month_text + "'])").click()

    browser.get(link2)

    rows = len(browser.find_elements(by=By.XPATH, value="/html/body/div[@class='container']/section/table["
                                                        "@class='table table-bordered table-prog']/tbody/tr[1]/td"))

    cols = len(browser.find_elements(by=By.XPATH, value="/html/body/div[@class='container']/section/table["
                                                        "@class='table table-bordered table-prog']/tbody/tr/td[3]"))

    denDer = len(browser.find_elements(by=By.XPATH, value="/html/body/div[@class='container']/section/table["
                                                          "@class='table table-bordered table-prog']/tbody/tr[1]/td["
                                                          "@class='danger']"))




    def dangers1():
        browser.find_element(By.XPATH, f'//tbody/tr[{dolv}]/td[{dolv2}]').click()

        browser.find_element(By.ID, "check_nb").click()
       # browser.find_element(By.ID, "select_type").click()
       # browser.find_element(By.XPATH, "//option[text()='" + PRIC + "']").click()
       # browser.find_element(By.ID, "select_type").click()
        browser.find_element(By.XPATH, "//button[text()='Сохранить']").click()


    for c in range(cols + 1):
        for r in range(1, rows + 1):
            dangers1()
            dolv2 += 1

# i: int = 1

# while i < len(b):
#    browser.find_element(By.XPATH,
#                        "/html/body/div[@class='container']/section/table[@class='table table-bordered "
#                         "table-prog']/tbody/tr[14]/td[@class='danger'][" + str(i) + "]").click()
#    browser.find_element(By.ID, "select_type").click()
#     browser.find_element(By.XPATH, "//option[text()='" + PRIC + "']").click()
#     browser.find_element(By.ID, "select_type").click()
#    browser.find_element(By.XPATH, "//button[text()='Сохранить']").click()

finally:
    time.sleep(5)
    browser.quit()
