from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from MediaSource import MediaSource as _mediaSource
import os
from time import sleep
from Post import Post

class Facebook(_mediaSource):
    _supportedVideoTypes = ['.gif', '.mp4']
    _supportedImageTypes = ['.png', '.jpeg']    
    def __init__(self, username, password, page):
        self.username = username
        self.password = password
        self.page = page

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
            self.postVideoToPage(self.page, post)
        elif i == True:
            self.postImageToPage(self.page, post)
        else:
            self.postTextToPage(self.page, post)
        pass
    def getMediaName(self):
        return 'Facebook'
    def getMediaUserName(self):
        return self.username
    def getMediaPassword(self):
        return self.password
    def getPageName(self):
        return self.page
    def postVideoToPage(self, pageName, post):
        # open facebook and login
        driver = self.loginToHomePage()

        try:
            # go to page - by name
            driver.find_element_by_link_text(pageName).click()
            wait = WebDriverWait(driver, 100).until_not(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Photo/Video')))
    
            # click photo/video button
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Photo/Video')))        
            wait.click()

            # upload file
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//input[@data-testid="media-attachment-add-photo"]')))
            wait.send_keys(post.image)

            # fill title in popup
            element = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Write a title"]')))
            element.send_keys(post.title)

            # fill text in popup
            element = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Say something about this video. This description will appear with your video across Facebook."]')))
            element.send_keys(post.text)

            # publish when done uploading
            publish = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//span[text()="100.0%"]')))
            driver.find_element(By.XPATH, '//button[@type="submit" and text()="Publish"]').click()

            # exit when done finializing
            wait = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@role="progressbar"]')))
            wait = WebDriverWait(driver, 300).until_not(EC.presence_of_element_located((By.XPATH, '//div[@role="progressbar"]')))
            driver.quit()
        finally:
            print('done')
    def postImageToPage(self, pageNmae, post):
        driver = self.loginToHomePage()

        try:
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.LINK_TEXT, pageNmae)))
            wait.click()

            wait = WebDriverWait(driver, 100).until_not(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Photo/Video')))
    
            # click photo/video button
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Photo/Video')))        
            wait.click() 

            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//input[@data-testid="media-attachment-add-photo"]')))
            wait.send_keys(post.image)

            driver.find_element_by_xpath('//div[@aria-autocomplete="list"]').send_keys(post.text)
            # driver.find_element_by_xpath('//button[@data-testid="react-composer-post-button"]').click()
            wait = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="react-composer-post-button"]')))
            wait.click()

            wait = WebDriverWait(driver, 100).until_not(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, '//button[@data-testid="react-composer-post-button"]')))
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Photo/Video')))                    
            

            driver.quit()            
        except:
            print('Failed')
            pass
        finally:
            pass
    def postTextToPage(self, pageNmae, post):
        driver = self.loginToHomePage()

        try:
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.LINK_TEXT, pageNmae)))
            wait.click()

            wait = WebDriverWait(driver, 100).until_not(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Photo/Video')))
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Photo/Video')))

            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//textarea[@data-testid="status-attachment-mentions-input"]')))            
            wait.click()
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-autocomplete="list"]')))            
            wait.send_keys(post.text)

            wait = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="react-composer-post-button"]')))
            wait.click()

            wait = WebDriverWait(driver, 100).until_not(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, '//button[@data-testid="react-composer-post-button"]')))
            wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Photo/Video')))                    
            
            driver.quit()            
        except:
            print('Failed')
            pass
        finally:
            pass
    def loginToHomePage(self):
        # disable notifications
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        chromedriver = './chromedriver.exe'
        driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
        driver.set_page_load_timeout(100)

        # login
        driver.get('https://facebook.com')
        driver.find_element_by_id("email").send_keys(self.username)
        driver.find_element_by_id("pass").send_keys(self.password)
        driver.find_element_by_id("loginbutton").click()

        return driver

# image = 'C:\\Users\\Dylan\\Desktop\\Media\\Twitter\\Gifs\\RainBalloon10mb.gif'
# image = 'C:\\Users\\Dylan\\Desktop\\Media\\Twitter\\TwitterImage2.png'
# text = 'Doodle Planes!'
# time = {}
# title = "here is a title"
# _newPost = Post(image, text, time, title, 1)

# _facebook = Facebook('Dylanc400@hotmail.com','Cronkhite2', 'Doodle Planes')
# _facebook.postTextToPage('Doodle Planes', _newPost)
