import os
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

async def get_schedule():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-first-run')
    #chrome_options.add_argument('--use-fake-ui-for-media-stream')
    #chrome_options.add_argument('--use-fake-device-for-media-stream')
    chrome_options.add_argument('--disable-sync')
    driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

    driver.get("https://fap.fpt.edu.vn/")
    select = Select(driver.find_element_by_id('ctl00_mainContent_ddlCampus'))
    select.select_by_visible_text('FU-Hồ Chí Minh')

    main_window_handle = None
    while not main_window_handle:
     main_window_handle = driver.current_window_handle

    driver.implicitly_wait(15)

    x_path = '/html/body/div/div[2]/div/form/table/tbody/tr[1]/td/div/div/div/div[2]/div/fieldset/div/center/div/div[2]/div/div/div'
    button = driver.find_elements_by_xpath(x_path)
    button[0].click()

    driver.implicitly_wait(15)
    #print('sign-in-clicked')

    signin_window_handle = None
    while not signin_window_handle:
     for handle in driver.window_handles:
      if handle != main_window_handle:
       signin_window_handle = handle
       break
    #print(signin_window_handle)
    driver.switch_to.window(signin_window_handle)
    #driver.get("https://accounts.google.com/signin")
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

    driver.switch_to.window(main_window_handle)
    driver.implicitly_wait(20)

    while True:
        if driver.current_url == 'https://fap.fpt.edu.vn/Student.aspx':
            break

    x_path = '/html/body/div/div[2]/div/form/table/tbody/tr[1]/td/div/div[2]/div[1]/div[2]/div/table/tbody/tr/td/table/tbody/tr[1]/td[2]/ul/li[3]/a'
    link = driver.find_elements_by_xpath(x_path)
    link[0].click()
    driver.implicitly_wait(15)

    #element=driver.find_element_by_xpath('/html/body/div/div[2]/div/form/table/tbody/tr[1]/td/div/table/tbody/tr[1]/td[1]')
    #element.location_once_scrolled_into_view
    driver.fullscreen_window()
    driver.execute_script("window.scrollTo(0, 220);")
    driver.save_screenshot('schedule.png')
    driver.quit()
