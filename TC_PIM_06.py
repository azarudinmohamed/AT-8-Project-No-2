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

#xpath to admin tab
        admin_xpath='//a[@href="/web/index.php/admin/viewAdminModule"]'
        admin=driver.find_element(By.XPATH,admin_xpath).click()
        time.sleep(4)

#xpath to myinfo details
        driver.find_element(By.XPATH,'//a[@href="/web/index.php/pim/viewMyDetails"]').click()
        time.sleep(3)

#xpath to contact details
        driver.find_element(By.XPATH,'//a[@href="/web/index.php/pim/contactDetails/empNumber/7"]').click()
        time.sleep(4)

#xpath to street1
        street1_xpath=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input')
        street1_xpath.send_keys(Keys.CONTROL, 'a')
        street1_xpath.send_keys(Keys.BACKSPACE)
        street1_xpath.send_keys("D Block")
        time.sleep(4)

#xpath to street2
        street2_xpath=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input')
        street2_xpath.send_keys(Keys.CONTROL, 'a')
        street2_xpath.send_keys(Keys.BACKSPACE)
        street2_xpath.send_keys("abc street")
        time.sleep(4)

#xpath to city
        City_xpath=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input')
        City_xpath.send_keys(Keys.CONTROL, 'a')
        City_xpath.send_keys(Keys.BACKSPACE)
        City_xpath.send_keys("Chennai")
        time.sleep(4)

#xpath to state
        state_xpath=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input')
        state_xpath.send_keys(Keys.CONTROL, 'a')
        state_xpath.send_keys(Keys.BACKSPACE)
        state_xpath.send_keys("Tamilnadu")
        time.sleep(4)

#xpath to zip
        zip_xpath=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input')
        zip_xpath.send_keys(Keys.CONTROL, 'a')
        zip_xpath.send_keys(Keys.BACKSPACE)
        zip_xpath.send_keys("600009")
        time.sleep(4)

#xpath to country
        driver.find_element(By.XPATH, '//label[text()="Country"]/following::div[3]').click()
        time.sleep(4)

#xpath to india dropdown
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="India"][1]').click()
        time.sleep(4)

#xpath to Telephone(Home)
        homeph_xpath=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input')
        homeph_xpath.send_keys(Keys.CONTROL, 'a')
        homeph_xpath.send_keys(Keys.BACKSPACE)
        homeph_xpath.send_keys("15978435")
        time.sleep(4)

#xpath to Telephone(Mobile)
        mobile_xpath=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input')
        mobile_xpath.send_keys(Keys.CONTROL, 'a')
        mobile_xpath.send_keys(Keys.BACKSPACE)
        mobile_xpath.send_keys("9874512355")
        time.sleep(4)

#xpath to other email
        otheremail_xpath=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input')
        otheremail_xpath.send_keys(Keys.CONTROL, 'a')
        otheremail_xpath.send_keys(Keys.BACKSPACE)
        otheremail_xpath.send_keys("def@gmail.com")

        time.sleep(4)

#xpath to save button
        driver.find_element(By.XPATH,'//label[text()="Work Email"]/following::button[1]').click()
        time.sleep(5)

        print("Contact Details of the employee has been filled successfully")
a=username_1()
a.name_password()


