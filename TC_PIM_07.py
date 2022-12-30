from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class username_1():
    def name_password(self):
        driver=webdriver.Edge()
        url="https://opensource-demo.orangehrmlive.com/"
        driver.get(url)
        time.sleep(3)
        driver.maximize_window()
        time.sleep(3)

#xpath to username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(3)

#xpath to password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(3)

#xpath to login button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(5)

#xpath to myinfo tab
        driver.find_element(By.XPATH, '//a[@href="/web/index.php/pim/viewMyDetails"]').click()
        time.sleep(3)

#xpath to Emergency contact details tab
        driver.find_element(By.XPATH,'//a[text()="Contact Details"]/following::div[1]').click()
        time.sleep(4)

#xpath Assigned emergency details
        driver.find_element(By.XPATH,'//h6[text()="Assigned Emergency Contacts"]/following::button[1]').click()
        time.sleep(4)

#xpath for name
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Ayaan")
        time.sleep(4)

#xpath for Relationship
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').send_keys("Friend")
        time.sleep(4)

#xpath for home telephone
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input').send_keys("147852963")
        time.sleep(4)

#xpath for mobile
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input').send_keys("9874155879")
        time.sleep(4)

#xpath for work telephone
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input').send_keys("5698746546")
        time.sleep(4)

#xpath to save
        driver.find_element(By.XPATH,'//label[text()="Mobile"]/following::button[2]').click()
        time.sleep(6)


a=username_1()
a.name_password()
