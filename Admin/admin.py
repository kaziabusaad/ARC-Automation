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


def admin(driver, url):
    # driver.get(url)
    sleep_timeout_long()

    # Sign in
    try:
        driver.find_element(By.ID, 'email').send_keys('hasib@hasib.com')
        sleep_timeout_medium()
        driver.find_element(By.ID, 'password').send_keys('Password')
        sleep_timeout_medium()
        driver.find_element(By.ID, 'sign-in').click()
        sleep_timeout_long()
        sleep_timeout_long()
        print('Admin SignIn: Successful ✔')
    except Exception as e:
        print('Admin SignIn: Failed! 👎')
        print(f"Error from Admin SignIn: {e}")

    # Dashboard
    try:
        # KPI List
        # wait = WebDriverWait(driver, 20)
        # element = wait.until(EC.visibility_of_element_located((By.ID, 'radix-:r0:-trigger-password')))
        # element.click()
        driver.find_element(By.ID, 'kpi-list').click()
        sleep_timeout_long()
        # TODO: Pagination
        print('Admin Dashboard: Successful ✔')
    except Exception as e:
        print('Admin Dashboard: Failed! 👎')
        print(f"Error from Admin Dashboard: {e}")

    # KPI
    try:
        driver.find_element(By.ID, 'dashboard-kpi-winner').click()
        sleep_timeout_long()
        # Pagination
        # Scroll to the element
        button_element = driver.find_element(By.ID, "next")
        driver.execute_script("arguments[0].scrollIntoView();", button_element)
        button_element.click()
        # driver.find_element(By.ID, 'next').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'previous').click()
        sleep_timeout_long()
        # Search By Name
        driver.find_element(By.ID, 'search-input').send_keys('Farhana')
        sleep_timeout_medium()
        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        sleep_timeout_medium()
        act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        sleep_timeout_medium()
        act.key_up(Keys.BACKSPACE).send_keys('Mahmud').key_down(Keys.CONTROL).perform()
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
        print('Admin KPI: Successful ✔')
    except Exception as e:
        print('Admin KPI: Failed! 👎')
        print(f"Error from Admin KPI: {e}")

    # Employee
    try:
        driver.find_element(By.XPATH, '//*[@id="dashboard-employees"]/span[2]').click()
        sleep_timeout_long()
        sleep_timeout_long()
        # Pagination
        driver.find_element(By.ID, 'next').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'previous').click()
        sleep_timeout_long()
        sleep_timeout_long()
        # Create
        driver.find_element(By.ID, 'create').click()
        sleep_timeout_long()
        sleep_timeout_long()
        # Scrolling
        # iframe = driver.find_element(By.ID, 'submit')
        # ActionChains(driver).scroll_to_element(iframe).perform()
        # sleep_timeout_medium()
        # driver.find_element(By.ID, 'submit').click()
        # sleep_timeout_medium()
        driver.find_element(By.ID, 'name').send_keys('Myself Saad')
        sleep_timeout_short()
        driver.find_element(By.ID, 'email').send_keys('myself@saad.com')
        sleep_timeout_short()
        driver.find_element(By.ID, 'phone').send_keys('01732456890')
        sleep_timeout_short()
        driver.find_element(By.ID, 'password').send_keys('12345678')
        sleep_timeout_short()
        driver.find_element(By.ID, 'confirmPassword').send_keys('12345678')
        sleep_timeout_short()
        # Scrolling
        iframe = driver.find_element(By.ID, 'submit')
        ActionChains(driver).scroll_to_element(iframe).perform()
        sleep_timeout_medium()
        # driver.find_element(By.ID, 'submit').click()
        # sleep_timeout_medium()
        # Dropdowns
        dropdown = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/form/div[6]/select'))
        desired_value = "Supervisor"
        dropdown.select_by_visible_text(desired_value)
        # driver.find_element(By.ID, 'role_name').click()
        # sleep_timeout_medium()
        # driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/form/div[6]/select/option[5]').click()
        sleep_timeout_medium()
        dropdown = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/form/div[7]/select'))
        desired_value = "Jr. SQA Engineer"
        dropdown.select_by_visible_text(desired_value)
        # driver.find_element(By.ID, 'designation_id').click()
        # sleep_timeout_medium()
        # driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/form/div[7]/select/option[9]').click()
        sleep_timeout_medium()
        dropdown = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/form/div[8]/select'))
        desired_value = "Fahim Chawdhury"
        dropdown.select_by_visible_text(desired_value)
        # driver.find_element(By.ID, 'supervisor_id').click()
        # sleep_timeout_medium()
        # driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/form/div[8]/select/option[7]').click()
        sleep_timeout_medium()

        # file_input = driver.find_element(By.ID, 'upload-avatar')
        # file_input.click()
        print("click on file upload")
        sleep_timeout_longTime()
        driver.find_element(By.ID, 'upload-avatar').click()
        sleep_timeout_short()
        file_path = "C:\\Users\kazia\OneDrive\Pictures\Screenshots\mask-man.jpg"
        pyautogui.write(file_path)
        pyautogui.press("enter")
        sleep_timeout_medium()
        driver.find_element(By.ID, 'submit').click()
        sleep_timeout_long()
        # Search By Name
        driver.find_element(By.ID, 'search-input').send_keys('Saad')
        sleep_timeout_long()
        # Edit
        driver.find_element(By.ID, 'moreHorizontal').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'edit').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'name').send_keys('Myself Kazi Saad')
        sleep_timeout_short()
        driver.find_element(By.ID, 'phone').send_keys('01732456891')
        sleep_timeout_short()

        file_input = driver.find_element(By.ID, 'upload-avatar')
        file_input.click()
        sleep_timeout_short()
        file_path = "C:\\Users\kazia\OneDrive\Pictures\Screenshots\mask-man2.jpg"
        pyautogui.write(file_path)
        pyautogui.press("enter")
        sleep_timeout_medium()
        driver.find_element(By.ID, 'submit').click()
        sleep_timeout_medium()
        # Search By Name
        driver.find_element(By.ID, 'search-input').send_keys('Saad')
        sleep_timeout_long()
        # Delete
        driver.find_element(By.ID, 'moreHorizontal').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'delete').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'cancel')
        sleep_timeout_short()
        driver.find_element(By.ID, 'delete').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'confirm').click()
        sleep_timeout_long()
        print('Admin Employee: Successful ✔')
    except Exception as e:
        print('Admin Employee: Failed! 👎')
        print(f"Error from Admin Employee: {e}")

    # Metrics Management
    try:
        driver.find_element(By.ID, 'dashboard-metrics').click()
        sleep_timeout_long()
        sleep_timeout_long()
        # Pagination
        driver.find_element(By.ID, 'next').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'previous').click()
        sleep_timeout_medium()
        # Create
        driver.find_element(By.ID, 'create').click()
        sleep_timeout_long()
        sleep_timeout_long()
        dropdown = Select(driver.find_element(By.XPATH, '//*[@id="select-supervisor-id"]/select'))
        desired_value = "Keramot Ali"
        dropdown.select_by_visible_text(desired_value)
        # driver.find_element(By.ID, 'supervisor_id').click()
        # sleep_timeout_medium()
        # driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/form/div/div[1]/select/option[4]').click()
        sleep_timeout_medium()
        dropdown = Select(driver.find_element(By.XPATH, '//*[@id="select-subordinate-id"]/select'))
        desired_value = "Najia Esrat"
        dropdown.select_by_visible_text(desired_value)
        # driver.find_element(By.ID, 'subordinate_id').click()
        # sleep_timeout_medium()
        # driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/form/div/div[2]/select/option[14]').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'kpi-keys-1').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'kpi-keys-2').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'kpi-keys-3').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'kpi-keys-4').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'submit').click()
        sleep_timeout_long()
        # Search By Name
        driver.find_element(By.ID, 'search-input').send_keys('Najia')
        sleep_timeout_long()
        driver.find_element(By.ID, 'MoreHorizontal').click()
        sleep_timeout_medium()
        # Edit
        driver.find_element(By.ID, 'edit').click()
        sleep_timeout_long()
        sleep_timeout_long()
        dropdown = Select(driver.find_element(By.XPATH, '//*[@id="select-subordinate-id"]/select'))
        desired_value = "Myself Saad"
        dropdown.select_by_visible_text(desired_value)
        sleep_timeout_medium()
        driver.find_element(By.ID, 'submit').click()
        # Search By Name
        driver.find_element(By.ID, 'search-input').send_keys('Saad')
        sleep_timeout_long()
        driver.find_element(By.ID, 'MoreHorizontal').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'delete').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'cancel').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'delete').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'confirm').click()
        sleep_timeout_long()
        print('Admin Metrics Management: Successful ✔')
    except Exception as e:
        print('Admin Metrics Management: Failed! 👎')
        print(f"Error from Admin Metrics Management: {e}")

    # KPI Indicator
    try:
        driver.find_element(By.ID, 'dashboard-kpi-indicator').click()
        sleep_timeout_long()
        print('Admin KPI Indicator: Successful ✔')
    except Exception as e:
        print('Admin KPI Indicator: Failed! 👎')
        print(f"Error from Admin KPI Indicator: {e}")

    # My Profile
    try:
        driver.find_element(By.ID, 'avatar').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'my-profile').click()
        sleep_timeout_long()
        sleep_timeout_long()
        input_field = driver.find_element(By.ID, 'name')
        input_field.clear()
        input_field.send_keys(Keys.BACKSPACE)
        sleep_timeout_short()
        driver.find_element(By.ID, 'name').send_keys('Bro Hasib')
        sleep_timeout_short()
        input_field = driver.find_element(By.ID, 'phone')
        input_field.clear()
        input_field.send_keys(Keys.BACKSPACE)
        sleep_timeout_short()
        driver.find_element(By.ID, 'phone').send_keys('+8801917200114')
        sleep_timeout_short()
        dropdown = Select(driver.find_element(By.XPATH, '//*[@id="select-supervisor-id"]/select'))
        desired_value = "Tariq Abdullah"
        dropdown.select_by_visible_text(desired_value)
        sleep_timeout_medium()
        driver.find_element(By.ID, 'submit').click()
        sleep_timeout_long()
        print('Admin My Profile: Successful ✔')
    except Exception as e:
        print('Admin My Profile: Failed! 👎')
        print(f"Error from Admin My Profile: {e}")

    # Reset Password
    try:
        driver.find_element(By.ID, 'avatar').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'reset-password').click()
        sleep_timeout_long()
        sleep_timeout_long()
        driver.find_element(By.ID, 'old_password').send_keys('password')
        sleep_timeout_short()
        driver.find_element(By.ID, 'reset-input-password').send_keys('Password')
        sleep_timeout_short()
        driver.find_element(By.ID, 'confirm-password').send_keys('Password')
        sleep_timeout_long()
        driver.find_element(By.ID, 'submit').click()
        sleep_timeout_long()
        driver.find_element(By.ID, 'email').send_keys('hasib@hasib.com')
        sleep_timeout_medium()
        driver.find_element(By.ID, 'password').send_keys('password')
        sleep_timeout_medium()
        driver.find_element(By.ID, 'sign-in').click()
        sleep_timeout_long()
        print('Admin Reset Password: Successful ✔')
    except Exception as e:
        print('Admin Reset Password: Failed! 👎')
        print(f"Error from Admin Reset Password: {e}")

    # Log Out
    try:
        # driver.find_element(By.ID, 'avatar').click()
        sleep_timeout_medium()
        driver.find_element(By.ID, 'log-out').click()
        sleep_timeout_long()
        print('Admin Log Out: Successful ✔')
    except Exception as e:
        print('Admin Log Out: Failed! 👎')
        print(f"Error from Admin Log Out: {e}")
