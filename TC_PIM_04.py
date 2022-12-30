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

        #xpath for submit
        submit_xpath = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        submit = driver.find_element(By.XPATH, submit_xpath).click()
        time.sleep(7)

        #xpath for personal details tab
        personal_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'
        print(driver.find_element(By.XPATH,personal_xpath).accessible_name)
        time.sleep(3)

        #xpath for contact details tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a').accessible_name)
        time.sleep(2)

        #xpath for emergency contacts tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a').accessible_name)
        time.sleep(2)

        #xpath for dependents tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a').accessible_name)
        time.sleep(2)

        #xpath for Immigration tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a').accessible_name)
        time.sleep(2)

        #xpath for Job tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a').accessible_name)
        time.sleep(2)

        #xpath for salary tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a').accessible_name)
        time.sleep(2)

        #xpath for tax exemptions tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a').accessible_name)
        time.sleep(2)

        #xpath for Report to tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a').accessible_name)
        time.sleep(2)

        #xpath to qualifications tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a').accessible_name)
        time.sleep(2)

        #xpath to memberships tab
        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[11]/a').accessible_name)
        time.sleep(2)

a=username_1()
a.name_password()