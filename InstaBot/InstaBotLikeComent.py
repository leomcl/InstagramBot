from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class InstaBotScript:  # like first post in feed
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.pw = pw
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]") \
            .click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(pw)
        sleep(0.5)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()
        sleep(2.5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".\\_8Rm4L:nth-child(1) .fr66n .\\_8-yf5") \
            .click()
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".\\_15y0l .\\_8-yf5").click()  # click comment button
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".\\_15y0l .\\_8-yf5").click()  # click comment button
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".Ypffh").send_keys("hello world")  # enter comment in box
        sleep(1.5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Post')]") \
            .click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".\\_15y0l .\\_8-yf5").click()  # click comment button
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".Ypffh").send_keys(
            "hello world")  # enter comment in box
        sleep(1.5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Post')]") \
            .click()


class InstaBotScriptDirectlink:  # likes specific post through link
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.pw = pw
        link = input('Enter link:')
        self.driver.get(link)  # insert photo link here
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]") \
            .click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Log In')]") \
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(pw)
        sleep(0.5)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()
        sleep(2.5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "span > .\\_8-yf5") \
            .click()  # click like
        sleep(1)
        # self.driver.find_element_by_xpath("//button[contains(text(), 'OK')]") \
        #    .click()
        # sleep(2)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".\\_15y0l .\\_8-yf5").click()  # click comment button
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".\\_15y0l .\\_8-yf5").click()  # click comment button
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".Ypffh").send_keys(
            "Hello world)")  # enter comment in box
        sleep(1.5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Post')]") \
            .click()
        sleep(2)


class InstaBotScriptLogin:  # logs on bots in
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.pw = pw
        self.driver.get("https://www.instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]") \
            .click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(pw)
        sleep(0.5)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        sleep(2)



# all bots username and passwords
print('Option 1: Like first post in bots feed')
print('option 2: Like post through specific link')
print('Option 3: Log all bots in')
option = input('enter choice:')
if option == '1':
    bot1 = InstaBotScript('leonavincent9', 'instabot123')
    bot2 = InstaBotScript('bobbysanyyyers', 'leoleoleo1')
    bot3 = InstaBotScript('nadiasimons7', 'instagrambot123')

elif option == '2':
    my_bot1 = InstaBotScriptDirectlink('leonavincent9', 'instabot123')
    my_bot2 = InstaBotScriptDirectlink('bobbysanyyyers', 'leoleoleo1')
    my_bot3 = InstaBotScriptDirectlink('nadiasimons7', 'instagrambot123')

elif option == '3':
    my_bot1 = InstaBotScriptLogin('leonavincent9', 'instabot123')
    my_bot2 = InstaBotScriptLogin('bobbysanyyyers', 'leoleoleo1')
    my_bot3 = InstaBotScriptLogin('nadiasimons7', 'instagrambot123')
