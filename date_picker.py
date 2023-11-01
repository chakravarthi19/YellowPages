import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://www.makemytrip.com/flights/")
#
# time.sleep(3)
# driver.find_element(By.CLASS_NAME, "commonModal__close").click()
# time.sleep(3)
# driver.find_element(By.XPATH, '//p[@data-cy = "departureDate"]').click()
# time.sleep(3)
#
# # driver.find_element(By.XPATH, '//p[@data-cy = "departureDate"]').send_keys("21Nov23")
# # desired_date = driver.find_element(By.XPATH, "//td[text()='20']")  # Assuming the day is selectable by text
# # desired_date.click()
# # time.sleep(10)
#
# # driver.find_element(By.XPATH, '//span[@aria-label="Next Month"]').click()
# # time.sleep(2)
# # Find the element that contains the date "20 Nov 2023"
# date_picker = driver.find_element(By.CLASS_NAME, "DayPicker-Body")
#
# # Locate and click the desired date element
# desired_date_element = date_picker.find_element(By.XPATH, "//div[@aria-label='Wed Dec 20 2023']")
# desired_date_element.click()
# time.sleep(5)

driver.get('https://jqueryui.com/datepicker/')
time.sleep(3)
driver.find_element(By.CLASS_NAME, "hasDatepicker").click()
time.sleep(2)
driver.find_element(By.ID, "datepicker").send_keys('12/12/2023')
time.sleep(10)

