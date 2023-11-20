import time
from selenium import webdriver

from driver_setup import handler

print("Started")
chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
target_url = r"https://squareup.com/dashboard/sales/transactions"
driver = handler(chrome_path, chrome_driver_path, target_url)
curr_time = time.strftime("%H:%M:%S",time.localtime())
time.sleep(4)   
email = "apps@dedicatedmkt.com"
password = ".354FubWNNXG8Ej"

try:
    driver.send_prompt(email, "Email address")
    print("email entered")
    time.sleep(1)

    driver.send_prompt(password, "Password")
    print("password entered")
    time.sleep(1)
except:
    print("login not found")

driver.click_item("Export")
driver.click_item("Generate Transactions CSV")
working = False
while (working is False):
    try:
        driver.click_item("Download Transactions CSV")
        working = True
    except Exception as e:
        print(f"loading")
print("download time")
driver.quit()
