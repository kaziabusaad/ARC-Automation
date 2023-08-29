import time

import pyautogui as pyautogui
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from config import sleep_timeout_long, sleep_timeout_dwnld
from config import sleep_timeout_short
from config import sleep_timeout_medium
from config import sleep_timeout_long1
from config import sleep_timeout_long
from config import sleep_timeout_longTime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromeOptions = Options()


def supervisor(driver, url):
    # driver.get(url)
    sleep_timeout_long()

    # Sign in
    try:
        driver.find_element(By.ID, 'email').send_keys('kera@kera.com')
        sleep_timeout_medium()
        driver.find_element(By.ID, 'password').send_keys('Password')
        sleep_timeout_medium()
        driver.find_element(By.ID, 'sign-in').click()
        sleep_timeout_long()
        sleep_timeout_long()
        print('Supervisor SignIn: Successful ✔')
    except Exception as e:
        print('Supervisor SignIn: Failed! 👎')
        print(f"Error from Supervisor SignIn: {e}")

    # Dashboard
    try:
        # KPI List
        # wait = WebDriverWait(driver, 20)
        # element = wait.until(EC.visibility_of_element_located((By.ID, 'radix-:r0:-trigger-password')))
        # element.click()
        driver.find_element(By.ID, 'kpi-list').click()
        sleep_timeout_long()
        # TODO: Pagination
        print('Supervisor Dashboard: Successful ✔')
    except Exception as e:
        print('Supervisor Dashboard: Failed! 👎')
        print(f"Error from Supervisor Dashboard: {e}")

    # KPI
    try:
        driver.find_element(By.ID, 'dashboard-kpi').click()
        sleep_timeout_long()
        # # Pagination
        # # Scroll to the element
        # button_element = driver.find_element(By.ID, "next")
        # driver.execute_script("arguments[0].scrollIntoView();", button_element)
        # button_element.click()
        # # driver.find_element(By.ID, 'next').click()
        # sleep_timeout_medium()
        # driver.find_element(By.ID, 'previous').click()
        # sleep_timeout_long()
        # Search By Name
        driver.find_element(By.ID, 'search-input').send_keys('Rasel')
        sleep_timeout_medium()
        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        sleep_timeout_medium()
        act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        sleep_timeout_medium()
        act.key_up(Keys.BACKSPACE).send_keys('Asha').key_down(Keys.CONTROL).perform()
        sleep_timeout_medium()
        input_field = driver.find_element(By.ID, 'search-input')
        input_field.clear()
        input_field.send_keys(Keys.BACKSPACE)
        # act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        # sleep_timeout_medium()
        # act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        # sleep_timeout_medium()
        # act.key_up(Keys.BACKSPACE).send_keys('').key_down(Keys.CONTROL).perform()
        sleep_timeout_long()
        print('Supervisor KPI: Successful ✔')
    except Exception as e:
        print('Supervisor KPI: Failed! 👎')
        print(f"Error from Supervisor KPI: {e}")

    # KPI Indicator
    try:
        driver.find_element(By.ID, 'dashboard-kpi-indicator').click()
        sleep_timeout_long()
        print('Supervisor KPI Indicator: Successful ✔')
    except Exception as e:
        print('Supervisor KPI Indicator: Failed! 👎')
        print(f"Error from Supervisor KPI Indicator: {e}")

    # My Profile
    try:
        driver.find_element(By.ID, 'avatar').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'my-profile').click()
        sleep_timeout_long()
        sleep_timeout_long()
        driver.find_element(By.ID, 'name').send_keys(' ')
        sleep_timeout_short()
        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        sleep_timeout_medium()
        act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        sleep_timeout_medium()
        act.key_up(Keys.BACKSPACE).send_keys('Kera Bro').key_down(Keys.CONTROL).perform()
        sleep_timeout_medium()
        # input_field = driver.find_element(By.ID, 'name')
        # input_field.clear()
        # input_field.send_keys(Keys.BACKSPACE)
        # sleep_timeout_short()
        # driver.find_element(By.ID, 'name').send_keys('Kera Bhai')
        # sleep_timeout_short()
        driver.find_element(By.ID, 'phone').send_keys(' ')
        sleep_timeout_short()
        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        sleep_timeout_medium()
        act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        sleep_timeout_medium()
        act.key_up(Keys.BACKSPACE).send_keys('+8801917200115').key_down(Keys.CONTROL).perform()
        sleep_timeout_medium()
        # input_field = driver.find_element(By.ID, 'phone')
        # input_field.clear()
        # input_field.send_keys(Keys.BACKSPACE)
        # sleep_timeout_short()
        # driver.find_element(By.ID, 'phone').send_keys('+8801917200114')
        # sleep_timeout_medium()
        driver.find_element(By.ID, 'submit').click()
        sleep_timeout_long()
        print('Supervisor My Profile: Successful ✔')
    except Exception as e:
        print('Supervisor My Profile: Failed! 👎')
        print(f"Error from Supervisor My Profile: {e}")

    # Reset Password
    try:
        driver.find_element(By.ID, 'avatar').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'reset-password').click()
        sleep_timeout_long()
        sleep_timeout_long()
        driver.find_element(By.ID, 'old_password').send_keys('Password')
        sleep_timeout_short()
        driver.find_element(By.ID, 'reset-input-password').send_keys('password')
        sleep_timeout_short()
        driver.find_element(By.ID, 'confirm-password').send_keys('password')
        sleep_timeout_long()
        driver.find_element(By.ID, 'submit').click()
        sleep_timeout_long()
        driver.find_element(By.ID, 'email').send_keys('kera@kera.com')
        sleep_timeout_medium()
        driver.find_element(By.ID, 'password').send_keys('Password')
        sleep_timeout_medium()
        driver.find_element(By.ID, 'sign-in').click()
        sleep_timeout_long()
        print('Supervisor Reset Password: Successful ✔')
    except Exception as e:
        print('Supervisor Reset Password: Failed! 👎')
        print(f"Error from Supervisor Reset Password: {e}")

    # Log Out
    try:
        # driver.find_element(By.ID, 'avatar').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'log-out').click()
        sleep_timeout_long()
        print('Supervisor Log Out: Successful ✔')
    except Exception as e:
        print('Supervisor Log Out: Failed! 👎')
        print(f"Error from Supervisor Log Out: {e}")

