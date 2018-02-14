from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from MediaSource import MediaSource as _mediaSource
import os
from time import sleep
from Post import Post


class Instagram(_mediaSource):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def post(self, post):
        print('Instagram Post')

    def postVideoToPage(self, post):
        
        driver = self.loginToHomePage()

        try:
            # driver.find_element_by_xpath('//div[@class="_crp8c coreSpriteFeedCreation"]').send_keys(post.image)
            # driver.find_element_by_xpath('//nav[@role="navigation"]//form[@enctype="multipart/form-data"]').send_keys(post.image)
            # wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//nav[@role="navigation"]//form//input')))            
            # wait.find_element_by_xpath('//nav[@role="navigation"]//form//input').send_keys(post.image)
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//nav//form//input')))            
            wait.find_element_by_xpath('//nav//form//input').send_keys(post.image)
            # //nav//form//input
            sleep(1000)
            
        finally:
            print('done')

    def getMediaName(self):
        return 'Instagram'

    def getMediaUserName(self):
        return self.username

    def getMediaPassword(self):
        return self.password

    def loginToHomePage(self):
        # disable notifications
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        mobile_emulation = { "deviceName": "iPhone X" }
        chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chromedriver = './chromedriver.exe'
        driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
        driver.set_page_load_timeout(100)

        # login
        driver.get('https://www.instagram.com/')
        driver.find_element_by_xpath('//a[@href="/accounts/login/"]').click()
        driver.find_element_by_xpath('//input[@name="username"]').send_keys(self.username)
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(self.password)
        driver.find_element_by_xpath('//button[text()="Log in"]').click()
        
        # driver.find_element_by_id("email").send_keys(self.username)
        # driver.find_element_by_id("pass").send_keys(self.password)
        # driver.find_element_by_id("loginbutton").click()
        return driver

# image = 'C:\\Users\\Dylan\\Desktop\\Media\\Twitter\\TwitterImage2.png'
# text = 'text as;dfklj'
# time = {}
# title = "here is a title"
# _newPost = Post(image, text, time, title, 1)

# _instagram = Instagram('Doodleplanes@gmail.com', 'q1w2e3r4t5Y^U&I*O(P)')
# _instagram.postVideoToPage(_newPost)
