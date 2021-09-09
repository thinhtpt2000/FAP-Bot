import os
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


async def get_schedule():
    driver = webdriver.Chrome()
    driver.get("https://accounts.google.com/signin")
    driver.implicitly_wait(15)

    x_path = '//*[@id="identifierId"]'
    input_box = driver.find_element_by_xpath(x_path)
    input_box.send_keys(os.getenv('FPT_MAIL'))

    x_path = '//*[@id ="identifierNext"]'
    button = driver.find_elements_by_xpath(x_path)
    button[0].click()

    x_path = '//*[@id ="password"]/div[1]/div / div[1]/input'
    input_box = driver.find_element_by_xpath(x_path)
    input_box.send_keys(os.getenv('PASS'))

    x_path = '//*[@id ="passwordNext"]'
    button = driver.find_elements_by_xpath(x_path)
    button[0].click()
    print('Login Successful...!!')
    
    driver.implicitly_wait(15)

    driver.get("https://fap.fpt.edu.vn/")
    select = Select(driver.find_element_by_id('ctl00_mainContent_ddlCampus'))
    select.select_by_visible_text('FU-Hồ Chí Minh')

    driver.implicitly_wait(15)
    time.sleep(3)

    x_path = '/html/body/div/div[2]/div/form/table/tbody/tr[1]/td/div/div/div/div[2]/div/fieldset/div/center/div/div[2]/div/div/div'
    button = driver.find_elements_by_xpath(x_path)
    button[0].click()

    driver.implicitly_wait(15)

    while True:
        if driver.current_url == 'https://fap.fpt.edu.vn/Student.aspx':
            break

    x_path = '/html/body/div/div[2]/div/form/table/tbody/tr[1]/td/div/div[2]/div[1]/div[2]/div/table/tbody/tr/td/table/tbody/tr[1]/td[2]/ul/li[3]/a'
    link = driver.find_elements_by_xpath(x_path)
    link[0].click()
    driver.implicitly_wait(15)
    driver.fullscreen_window()
    driver.save_screenshot('schedule.png')
    driver.quit()