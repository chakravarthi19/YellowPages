
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key
from pynput.keyboard import Controller
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.eluctpad.com/examples/")
driver.find_element(By.ID, "uploader browse").click()
time.sleep(3)
# Initialize the keyboard controller
keyboard = Controller()
# keyboard.Controller()
keyboard.type("C:\\Users\\anstromar\\PycharmProjects\\SeleniumTutorial\\rites\\example, file.png")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

str_ = "dad mom child dad"

li = []
dict_ = {}
for i in str_.split():
    if i == i[::-1]:
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] += 1
        li.append(i)

print(dict_)
print(">>>>", max(dict_.values()))
print(max(dict_, key=dict_.get))
for ii, jj in dict_.items():
    if jj == max(dict_.values()):
        print(ii, jj)
# print(sorted(li))

# print(li.count('dad'))
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("some url")

select_drop_down_ele = driver.find_element(By.ID, "")

select_ = Select(select_drop_down_ele)
li_list = []
for each_ele in select_.options:
    li_list.append(each_ele.text)

print(sorted(li_list))


def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence


# Change the value of 'n' to generate a different number of terms

n = 10  # Change this to the desired number of terms
fibonacci_series = generate_fibonacci(n)
for number in fibonacci_series:
    print(number, end=" ")

# Generate and print prime numbers from 1 to 100
for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')

print()  # Print a newline for formatting

# Generate and print prime numbers from 1 to 100
for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')

print()  # Print a newline for formatting


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


# Generate and print prime numbers from 1 to 100
for number in range(1, 101):
    if is_prime(number):
        print(number, end=' ')

print()  # Print a newline for formatting

x = lambda a: a + 10
print(x(5))  # Output: 15

import datetime
datetime.datetime.now = lambda: datetime.datetime(2012, 12, 12)


a = lambda x, y: x*y
print(a(7, 19))