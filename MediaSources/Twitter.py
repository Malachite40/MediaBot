from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from MediaSource import MediaSource as _mediaSource
import os
from time import sleep
from Post import Post

class Twitter(_mediaSource):
    _supportedVideoTypes = ['.gif', '.mp4']
    _supportedImageTypes = ['.png', '.jpeg']    

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def post(self, post):
        v = False
        i = False
        for p in self._supportedVideoTypes:
            if str(post.image).endswith(str(p)):
                print('Video File Detected')
                v = True
                pass
        for i in self._supportedImageTypes:
            if str(post.image).endswith(str(i)):
                print('Image File Detected')
                i = True
                pass
        if v == True:
            self.postVideoTweet(post)
        elif i == True:
            self.postImageTweet(post)
        else:
            self.postTextTweet(post)
        pass
    def postTextTweet(self, post):
        driver = self.loginToHomePage()

        try:
            # driver.find_element_by_id("global-new-tweet-button").click()
            # wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//input[@data-original-title="Add photos or video" and @name="media[]"]')))
            # wait.send_keys(post.image)
            driver.find_element_by_xpath('//div[@name="tweet"]').send_keys(post.text)
            driver.find_element_by_xpath('//button[@class="tweet-action EdgeButton EdgeButton--primary js-tweet-btn"]').click()
            wait = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="TweetBoxExtras tweet-box-extras"]')))            
            wait = WebDriverWait(driver, 100).until_not(EC.visibility_of_element_located((By.XPATH, '//div[@class="TweetBoxExtras tweet-box-extras"]')))
            driver.quit()
        except:
            print('Failed')
    def postImageTweet(self, post):
        driver = self.loginToHomePage()

        try:
            # driver.find_element_by_id("global-new-tweet-button").click()
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//input[@data-original-title="Add photos or video" and @name="media[]"]')))
            wait.send_keys(post.image)
            driver.find_element_by_xpath('//div[@name="tweet"]').send_keys(post.text)
            driver.find_element_by_xpath('//button[@class="tweet-action EdgeButton EdgeButton--primary js-tweet-btn"]').click()
            wait = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="TweetBoxExtras tweet-box-extras"]')))            
            wait = WebDriverWait(driver, 100).until_not(EC.visibility_of_element_located((By.XPATH, '//div[@class="TweetBoxExtras tweet-box-extras"]')))
            driver.quit()
        except:
            print('Failed')
    def postVideoTweet(self, post):
        # open twitter and login
        driver = self.loginToHomePage()

        try:
            # driver.find_element_by_id("global-new-tweet-button").click()
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//input[@data-original-title="Add photos or video" and @name="media[]"]')))
            wait.send_keys(post.image)
            driver.find_element_by_xpath('//div[@name="tweet"]').send_keys(post.text)
            driver.find_element_by_xpath('//button[@class="tweet-action EdgeButton EdgeButton--primary js-tweet-btn"]').click()
            wait = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="TweetBoxExtras tweet-box-extras"]')))            
            wait = WebDriverWait(driver, 100).until_not(EC.visibility_of_element_located((By.XPATH, '//div[@class="TweetBoxExtras tweet-box-extras"]')))
            driver.quit()
        finally:
            print('done')
    def loginToHomePage(self):
        # disable notifications
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        chromedriver = './chromedriver.exe'
        driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
        driver.set_page_load_timeout(100)

        # login
        driver.get('https://twitter.com/login')
        driver.find_element(By.XPATH, '//input[@placeholder="Phone, email or username"]').send_keys(self.username)
        driver.find_element(By.XPATH, '//input[@class="js-password-field"]').send_keys(self.password)        
        driver.find_element(By.XPATH, '//button[text()="Log in"]').click()

        return driver
    def getMediaName(self):
        return 'Twitter'
    def getMediaUserName(self):
        return self.username
    def getMediaPassword(self):
        return self.password

# image = 'C:\\Users\\Dylan\\Desktop\\Media\\Twitter\\TwitterImage2.png'
# image = 'C:\\Users\\Dylan\\Desktop\\Media\\Twitter\\Gifs\\RainBalloon10mb.gif'
# text = 'text as;dfklj'
# time = {}
# title = "here is a title"
# _newPost = Post(image, text, time, title, 1)

# _twitter = Twitter('Dylancronkhite1@gmail.com', 'Cronkhite2')

# _twitter.postTextTweet(_newPost)