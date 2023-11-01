import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/automation-practice-form')
driver.execute_script("document.body.style.zoom = '50%'")
time.sleep(2)

target_element = driver.find_element(By.ID, "state")
driver.execute_script("arguments[0].scrollIntoView(true)", target_element)
time.sleep(2)
upload_pic = (driver.find_element(By.ID, "uploadPicture").send_keys
              ("C://Users//ADMIN//OneDrive//Pictures//details_07_09_23.png"))
time.sleep(3)

# # Rajasthan
# state_ele = driver.find_element(By.ID, "state")
# # state_ele = driver.find_element(By.XPATH, '//div[@class=" css-yk16xz-control"][1]')
# # state_ele.click()
# state_opt = Select(state_ele)
# # for each_st in state_opt.
# state_opt.select_by_visible_text("Rajasthan")
# time.sleep(5)
# Find the state input element by its ID (assuming it's an input element)
state_input = driver.find_element(By.ID, "state")  # Replace with the actual ID

# Click to open the dropdown (if it's a custom dropdown)
state_input.click()

# Locate and click on the desired state in the dropdown (you may need to customize this part)
state_option = driver.find_element(By.XPATH, "//div[contains(text(), 'Rajasthan')]")
state_option.click()


# # from options get all options text and select either
# ascending order or descending order
#
# driver.get("some url")
#
# select_drop_down_ele = driver.find_element(By.ID, "")
#
# select_ = Select(select_drop_down_ele)
# li_list = []
# for each_ele in select_.options:
#     li_list.append(each_ele.text)
#
# print(sorted(li_list))
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# # Initialize a WebDriver (e.g., Chrome)
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
#
# # Navigate to the webpage with the dropdown
# driver.get('https://example.com')  # Replace with your URL
#
# # Locate the dropdown element by its ID or other selector
# dropdown_element = driver.find_element(By.ID, 'your_dropdown_id')  # Replace with the actual ID
#
# # Create a Select object to work with the dropdown
# select = Select(dropdown_element)
#
# # Get all text options from the dropdown
# all_options = [option.text for option in select.options]
#
# # Choose the sorting order (ascending or descending)
# sort_ascending = False  # Change to True for ascending order
#
# # Sort the options based on the chosen order
# sorted_options = sorted(all_options, reverse=not sort_ascending)
#
# # Select the first (or last) option from the sorted list
# if sort_ascending:
#     select.select_by_visible_text(sorted_options[0])
# else:
#     select.select_by_visible_text(sorted_options[-1])
#
# # Close the WebDriver
# driver.quit()

class vehicle:
    def __init__(self):
        print ("Engine started")
        self.name = "corolla" #Public
        self. model = 1999 #Protected
        self. make = "toyota" #Private


class car (vehicle):
    pass


c = car()
print(c.name)
print(c.model)
print(c.make) # it will show error in output













