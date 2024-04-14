import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.avito.ru/avito-care/eco-impact")
url=driver.current_url
driver.fullscreen_window()
time.sleep(3)
capture_path = 'D:/OUTPUT/1.png'
driver.save_screenshot(capture_path)
time.sleep(1)
driver.find_element("name", "arrow").click()
time.sleep(1)
capture_path = 'D:/OUTPUT/2.png'
driver.save_screenshot(capture_path)
time.sleep(1)
driver.find_element("name", "arrow").click()
time.sleep(1)
capture_path = 'D:/OUTPUT/3.png'
driver.save_screenshot(capture_path)
time.sleep(1)
driver.execute_script("window.scrollBy(0,850)","")
capture_path = 'D:/OUTPUT/4.png'
driver.save_screenshot(capture_path)
time.sleep(1)
