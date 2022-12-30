from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class username_1():
    def name_password(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/"
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)

        #xpath for username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(4)

        #xpath for password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(4)

        #xpath for login button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(4)

        #xpath for PIM
        PIM_xpath='//a[@href="/web/index.php/pim/viewPimModule"]'
        PIM=driver.find_element(By.XPATH,PIM_xpath).click()
        time.sleep(4)

        #xpath for ADD
        ADD_xpath='//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        ADD=driver.find_element(By.XPATH,ADD_xpath).click()
        time.sleep(4)

        #xpath for FIRSTNAME
        FIRSTNAME_xpath='//input[@placeholder="First Name"]'
        FIRSTNAME=driver.find_element(By.XPATH,FIRSTNAME_xpath).send_keys("Azarudin")
        time.sleep(4)

        #xpath for MIDDLENAME
        MIDDLENAME_xpath='//input[@placeholder="Middle Name"]'
        MIDDLENAME=driver.find_element(By.XPATH,MIDDLENAME_xpath).send_keys("Mohamed")
        time.sleep(4)

        #xpath for LASTNAME
        LASTNAME_xpath='//input[@placeholder="Last Name"]'
        LASTNAME=driver.find_element(By.XPATH,LASTNAME_xpath).send_keys("Asharaf")
        time.sleep(4)

        #xpath for createdetails toggle
        createdetails_xpath='//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]'
        toggle=driver.find_element(By.XPATH,createdetails_xpath).click()
        time.sleep(4)

        #xpath for username
        username_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
        name=driver.find_element(By.XPATH,username_xpath).send_keys("Azarudin Mohamed Asharaf")
        time.sleep(5)

        #xpath for Radio button
        radio_button_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        radio=driver.find_element(By.XPATH,radio_button_xpath).click()
        time.sleep(3)

        #xpath for password1
        pwrd_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
        pwrd=driver.find_element(By.XPATH,pwrd_xpath).send_keys("Guvi@123456")
        time.sleep(3)

        #xpath for confirm password
        cnfm_pwrd_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
        cnfmpwrd=driver.find_element(By.XPATH,cnfm_pwrd_xpath).send_keys("Guvi@123456")
        time.sleep(4)

        #xpath for submit
        submit_xpath='//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        submit=driver.find_element(By.XPATH,submit_xpath).click()
        time.sleep(4)

        print("New Employee Details has been Successfully Created and Saved")
a=username_1()
a.name_password()