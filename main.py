from selenium import webdriver
from rich.console import Console
from rich.theme import Theme
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Admin.admin import admin
from Supervisor.supervisor import supervisor

chromeOptions = Options()

custom_theme = Theme({'success': 'green', 'error': 'bold red'})

serv_obj = Service("C:/BrowserDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
console = Console(theme=custom_theme)

driver.get("https://arc-monorepo-arc-web-jkey.vercel.app/")
driver.maximize_window()

# # Admin
#
# try:
#     admin(driver, "https://arc-monorepo-arc-web-jkey.vercel.app/dashboard")
#     console.print('Admin: Successful ✔', style='success')
# except Exception as e:
#     console.print('Admin: Failed! 👎', style='error')
#     console.print(f"Error from Admin: {e}")

# Supervisor

try:
    supervisor(driver, "https://arc-monorepo-arc-web-jkey.vercel.app/dashboard")
    console.print('Supervisor: Successful ✔', style='success')
except Exception as e:
    console.print('Supervisor: Failed! 👎', style='error')
    console.print(f"Error from Supervisor: {e}")

