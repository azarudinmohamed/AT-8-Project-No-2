from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class username_1():
    def name_password(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/"
        driver.get(url)
        time.sleep(3)
        driver.maximize_window()
        time.sleep(3)

#xpath to username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(2)

#xpath to password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(2)

#xpath to login button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(3)

#xpath to search box
        search_box=driver.find_element(By.XPATH,'//input[@class="oxd-input oxd-input--active"]')
        time.sleep(2)

#import list method here
        search_list=['Admin','Pim','Leave','Time','Recruitment','My info','Performance','Dashboard','Directory','Maintenance','Buzz']

#run with upper case & lower case
        for a in search_list:
            search_box.send_keys(a.upper())
            time.sleep(3)
            search_box.send_keys(Keys.CONTROL, 'a')
            search_box.send_keys(Keys.BACKSPACE)
            search_box.send_keys(a.lower())
            time.sleep(2)
            search_box.send_keys(Keys.CONTROL, 'a')
            search_box.send_keys(Keys.BACKSPACE)

#printing the statement
        print("The code has been successfully ran both the upper and lower cases of the menu options")

a=username_1()
a.name_password()
