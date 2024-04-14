import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.avito.ru/avito-care/eco-impact")
url=driver.current_url
time.sleep(5)
capture_path = 'D:/OUTPUT/1.png'
driver.save_screenshot(capture_path)
time.sleep(2)
driver.find_element("name", "arrow").click()
time.sleep(2)
capture_path = 'D:/OUTPUT/2.png'
driver.save_screenshot(capture_path)
time.sleep(2)
driver.find_element("name", "arrow").click()
time.sleep(2)
capture_path = 'D:/OUTPUT/3.png'
driver.save_screenshot(capture_path)