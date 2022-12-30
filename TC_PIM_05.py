from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class username_1():
    def name_password(self):
        driver=webdriver.Edge()
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
        MIDDLENAME=driver.find_element(By.XPATH,MIDDLENAME_xpath).send_keys("M")
        time.sleep(4)

        #xpath for LASTNAME
        LASTNAME_xpath='//input[@placeholder="Last Name"]'
        LASTNAME=driver.find_element(By.XPATH,LASTNAME_xpath).send_keys("Mohamed")
        time.sleep(4)

        #xpath for submit
        submit_xpath = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        submit = driver.find_element(By.XPATH, submit_xpath).click()
        time.sleep(7)

        #xpath to nickname
        driver.find_element(By.XPATH,'//label[text()="Nickname"]/following::input[1]').send_keys("Azar")
        time.sleep(3)

        #xpath to other ID
        driver.find_element(By.XPATH,'//label[text()="Other Id"]/following::input[1]').send_keys("4156985")
        time.sleep(3)

        #xpath to driving licence number
        driver.find_element(By.XPATH,'''//label[text()="Driver's License Number"]/following::input[1]''').send_keys("10002000")
        time.sleep(3)

        #xpath to licence expiry date
        driver.find_element(By.XPATH,'//label[text()="License Expiry Date"]/following::input[1]').send_keys("2025-10-25")
        time.sleep(3)

        #xpath to SSN number
        driver.find_element(By.XPATH,'//label[text()="SSN Number"]/following::input[1]').send_keys("5000")
        time.sleep(3)

        #xpath to SIN number
        driver.find_element(By.XPATH,'//label[text()="SIN Number"]/following::input[1]').send_keys("2000")
        time.sleep(3)

        #xpath to Nationality
        driver.find_element(By.XPATH,'//label[text()="Nationality"]/following::div[2]').click()
        time.sleep(3)

        #xpath to Indian
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Indian"]').click()
        time.sleep(3)

        #xpath to Marital status
        driver.find_element(By.XPATH,'//label[text()="Marital Status"]/following::div[3]').click()
        time.sleep(3)

        #xpath to Married
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Married"]').click()
        time.sleep(3)

        #xpath to DOB
        driver.find_element(By.XPATH,'//label[text()="Date of Birth"]/following::input[1]').send_keys("1992-05-03")
        time.sleep(3)

        #xpath to Gender
        driver.find_element(By.XPATH,'//label[text()="Gender"]/following::span[1]').click()
        time.sleep(3)

        #xpath to Military service
        service=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input').send_keys("No")
        time.sleep(3)

        #xpath to smoker
        driver.find_element(By.XPATH,'//label[text()="Smoker"]/following::i[1]').click()
        time.sleep(3)

        #xpath to save
        driver.find_element(By.XPATH,'//label[text()="Military Service"]/following::button[1]').click()
        time.sleep(6)

        #xpath to blood type
        driver.find_element(By.XPATH,'//label[text()="Blood Type"]/following::div[3]').click()
        time.sleep(3)

        #xpath to AB+
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="AB+"]').click()
        time.sleep(3)

        #xpath to save
        driver.find_element(By.XPATH,'//label[text()="Military Service"]/following::button[2]').click()
        time.sleep(5)
        print("Successfully created")

a=username_1()
a.name_password()