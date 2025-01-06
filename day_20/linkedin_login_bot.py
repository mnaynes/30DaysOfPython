import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(PATH)

def linkedin_func():
    try:
        linkedin_home_page = 'https://www.linkedin.com/login'
        driver.get(linkedin_home_page)
        driver.implicitly_wait(3)

        # Get the username field
        username = driver.find_element(By.ID, 'username')

        # Get password field
        password = driver.find_element(By.ID, 'password')

        # Get login/submit button
        login = driver.find_element(By.XPATH, '//button[@type = \'submit\']')

        # Send login credentials to the form
        username.send_keys('')
        password.send_keys('')
        login.click()

    except Exception as e:
        print(e)

# Call the function
linkedin_func()