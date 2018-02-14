
from MediaSources.Post import Post
from MediaSources.Facebook import Facebook
from MediaSources.MediaSource import MediaSource
from MediaSources.Instagram import Instagram
from MediaSources.Twitter import Twitter
import json
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename
import datetime
import threading
import time

class MediaBot():

    _mediaSources = []
    _posts = []
    _curPostID = 0
    _userInfo = {}
    _postInfo = {}
    _threads = []
    def __init__(self):
        pass
    # UTILITY
    def cls(self):
        clear = lambda: os.system('cls')
        clear()
    def setUp(self):
        if self.doesFileExist('UserInfo.json'):
            pass
        else:
            print('It looks like this is your first time using Media Warrior')
            self.setupFacebookPage()
            self.setupTwitter()
            # self.setupInstagram()
            self.createUserInfo()
        # load
        self.loadUserInfo()
        self.loadMediaSources()
        self.loadPostInfo()
        self.loadPosts()
        self.createAutoPostThread()
        pass   
    def createAutoPostThread(self):
        newThread = threading.Thread(target=self.autoPostHandler, args=())
        newThread.setDaemon(True)
        newThread.start()
        self._threads.append(newThread)
    def printAllMediaSources(self):
        for s in self._mediaSources:
            print(s.getMediaName())
    def loadMediaSources(self):

        # facebook
        try:
            user = self._userInfo['Facebook']['username']
            password = self._userInfo['Facebook']['password']
            page = self._userInfo['Facebook']['page']
            _facebook = Facebook(user, password, page)
            self._mediaSources.append(_facebook)
            print('Facebook is enabled')
        except:
            print('No Facebook acctount info')
        finally:
            pass

        # twitter
        try:
            username = self._userInfo['Twitter']['username']
            password = self._userInfo['Twitter']['password']       
            _twitter = Twitter(username,password)
            self._mediaSources.append(_twitter)
            print('Twitter is enabled')
        except:
            print('No Twitter acctount info')
        finally:
            pass
        # instagram
        try:
            pass
        except:
            print('No Instagram acctount info')
        finally:
            pass

        r = raw_input('')
        
        pass
    def createUserInfo(self):
        path = './Info/'
        fileName = 'UserInfo'
        data = {}
        final = {}

        for s in self._mediaSources:  
            data = {
                "username": s.getMediaUserName(),
                "password": s.getMediaPassword(),
                "page": s.getPageName()             
            }

            final[s.getMediaName()] = data

        
        # create file with info
        filePathNameWExt = './' + path + '/' + fileName + '.json'
        with open(filePathNameWExt, 'w') as fp:
            json.dump(final, fp)
    def prettyPrintJsonFile(self):

        pass
    def loadUserInfo(self):
        files = os.listdir('./Info/')
        for f in files:
            if f == 'UserInfo.json':
                self._userInfo = json.load(open(os.path.join('./Info/', f)))
                break
        pass
    def doesFileExist(self, name):
        exists = False

        files = os.listdir('./Info/')
        for f in files:
            if f == name:
                exists = True
        return exists
    def printAllMediaSources(self):
        self.cls()
        for s in self._mediaSources:
            print(s.getMediaName)
        a = raw_input()   
    def autoPostHandler(self):
        while True:
            # print('jere')
            self.postIfReady()
            time.sleep(1)
    # CREATE ACCOUNTS
    def addAccount(self):
        self.cls()
        print('Add Facebook Account   -f')
        print('Add Twitter Account    -t')
        # print('Add Instagram Account  -i')
        print('Exit                   -e')        
        ans2 = raw_input()
        if ans2 == '-f':
            self.setupFacebookPage()
            self.deleteUserInfo()
            self.createUserInfo()
        elif ans2 == '-t':
            self.setupTwitter()
            self.deleteUserInfo()
            self.createUserInfo()
        elif ans2 == '-i':
            pass
            # self.setupInstagram()
            # self.deleteUserInfo()
            # self.createUserInfo()
    def setupTwitter(self):
        self.cls()        
        for s in self._mediaSources:
            if s.getMediaName() == "Twitter":
                self.cls()
                print('Looks like you already have a Twitter page... press any key to continue')
                a = raw_input()
                return
        
        ans = raw_input("Would you like to set up a Twitter page? [Y/N]")
        complete = False
        while complete == False:
            if ans == "Y" or ans == "y":
                username = raw_input("Enter your Login Email: ")
                password = raw_input("Enter your Password: ")

                self.cls()
                print("Is this information correct? [Y/N]")
                print('Login: {}'.format(username))
                print('Password: {}'.format(password))

                ans2 = raw_input()

                if ans2 == "Y" or ans2 == "y":
                    complete = True

                    twitter = Twitter(username,password)
                    self._mediaSources.append(twitter)

            else:
                print('Twitter media sign in skipped...')
                complete = True
                pass
    def setupFacebookPage(self):
        self.cls()
        for s in self._mediaSources:
            if s.getMediaName() == "Facebook":
                self.cls()                
                print('Looks like you already have a facebook page... press any key to continue')
                a = raw_input()
                return
        ans = raw_input("Would you like to set up a Facebook page? [Y/N]")
        complete = False
        while complete == False:
            if ans == "Y" or ans == "y":
                username = raw_input("Enter your Login Email: ")
                password = raw_input("Enter your Password: ")
                page = raw_input("Enter the page name you would like to post to: ")

                self.cls()
                print("Is this information correct? [Y/N]")
                print('Login: {}'.format(username))
                print('Password: {}'.format(password))
                print('Page: {}'.format(page))  

                ans2 = raw_input()

                if ans2 == "Y" or ans2 == "y":
                    complete = True

                    facebook = Facebook(username, password, page)
                    self._mediaSources.append(facebook)

            else:
                print('Facebook media sign in skipped...')
                complete = True
                pass
    def setupInstagram(self):
        self.cls()
        for s in self._mediaSources:
            if s.getMediaName() == "Instagram":
                self.cls()                
                print('Looks like you already have a Instagram page... press any key to continue')
                a = raw_input()
                return
        
        ans = raw_input("Would you like to set up a Instagram page? [Y/N]")
        complete = False
        while complete == False:
            if ans == "Y" or ans == "y":
                username = raw_input("Enter your Login Email: ")
                password = raw_input("Enter your Password: ")

                self.cls()
                print("Is this information correct? [Y/N]")
                print('Login: {}'.format(username))
                print('Password: {}'.format(password))

                ans2 = raw_input()

                if ans2 == "Y" or ans2 == "y":
                    complete = True

                    _instagram = Instagram(username, password)
                    self._mediaSources.append(_instagram)

            else:
                print('Instagram media sign in skipped...')
                complete = True
                pass
    # DELETE ACCOUNTS
    def deleteFacebook(self):
        for s in self._mediaSources:
            if s.getMediaName() == 'Facebook':
                self._mediaSources.remove(s)
        pass
    def deleteTwitter(self):
        for s in self._mediaSources:
            if s.getMediaName() == 'Twitter':
                self._mediaSources.remove(s)
        pass
    def deleteInstagram(self):
        for s in self._mediaSources:
            if s.getMediaName() == 'Instagram':
                self._mediaSources.remove(s)
        pass
    def deleteUserInfo(self):
        files = os.listdir('./')
        for f in files:
            if f == 'UserInfo.json':
                os.remove(f)
                break
        pass
    def deleteAccount(self):
        self.cls()
        print('Delete Facebook Account   -f')
        print('Delete Twitter Account    -t')
        # print('Delete Instagram Account  -i')
        print('Delete All                -a')
        print('Exit                      -e')     
        ans2 = raw_input()
        if ans2 == '-f':
            self.deleteFacebook()
            self.deleteUserInfo()
            self.createUserInfo()
        elif ans2 == '-t':
            self.deleteTwitter()
            self.deleteUserInfo()
            self.createUserInfo()
        elif ans2 == '-i':
            pass
            # self.setupInstagram()
            # self.deleteUserInfo()
            # self.createUserInfo()
        elif ans2 == '-a':
            self.deleteUserInfo()
            self._mediaSources = []
    # post
    def listPosts(self):
        self.cls()
        for p in self._posts:
            print('____________')
            print('[Post ID: {}]'.format(p.postID))   
            print('Path: {}'.format(p.image))     
            print('Title: {}'.format(p.title))   
            print('Text: {}'.format(p.text))   
            print('Time: {}'.format(p.time))               

        a = raw_input()
        pass
    def postNow(self):
        newPost = self.createPostForNow()
        self.postAll(newPost)
        r = raw_input('Intended Pause...')
        pass
    def createPostForLater(self):
        newPost = self.createPost()
        self._posts.append(newPost)         
        self.deletePostInfo()
        self.createPostInfo()
    def createPost(self):
        done = False
        while done == False:
            # file
            filepath = self.askForFile()

            # text
            text = self.askForText()
            
            # title
            title = self.askForTitle()
            
            print('')
            # time
            datet = self.askForTime()

            self.cls()

            print('Video File: {}'.format(filepath))
            print('Title: {}'.format(title))
            print('Text: {}'.format(text))
            print('Date: {}'.format(datet))
            
            
            ans2 = raw_input('Is this correct? [Y/N]')

            if ans2 == 'Y' or ans2 == 'y':
                done = True
                # create and add post
                newPost = Post(filepath, text, datet, title, self._curPostID)
                self._curPostID += 1
                return newPost

        pass
    def createPostForNow(self):
        done = False
        while done == False:
            # file
            filepath = self.askForFile()

            # text
            text = self.askForText()
            
            # title
            title = self.askForTitle()

            self.cls()

            print('Video File: {}'.format(filepath))
            print('Title: {}'.format(title))
            print('Text: {}'.format(text))
            
            
            ans2 = raw_input('Is this correct? [Y/N]')

            if ans2 == 'Y' or ans2 == 'y':
                done = True
                # create and add post
                newPost = Post(filepath, text, '', title, self._curPostID)
                self._curPostID += 1
                return newPost
        pass
    def askForTitle(self):
        self.cls()
        titledone = False
        while titledone == False:
            a = raw_input('Facebook requires a title for videos what would you like it to be: ')
            if len(a) > 40:
                print('Text max length is 40 character! Try again...')
            else:
                titledone = True
                return a
    def askForText(self):
        self.cls()
        textdone = False
        while textdone == False:
            a = raw_input('What would you like your post to say: ')
            if len(a) > 280:
                print('Text max length is 280 character! Try again...')
            else:
                textdone = True
                return a
    def askForTime(self):
        self.cls()        
        print('Enter a date and time for this to be posted...')        
        done = False
        while done == False:
            try:
                # time
                year = raw_input('Year (Example: 2018):')
                month = raw_input('Month (Example: 2):')
                day = raw_input('Day (Example: 9):')
                hour = raw_input('Hour in Military time (Example: 13):')
                minute = raw_input('Minute (Example: 50):')
                
                dt = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), 0, 0)
                done = True
                return dt
            except:
                print('Something was entered incorrect, try again.')
                r = raw_input()
    def askForFile(self):
        self.cls()
        ans2 = raw_input('Would you like to an attach a file? [Y/N]')

        if ans2 == 'Y' or ans2 == 'y':
            print('Select the file')
            Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            filepath = askopenfilename()
            return filepath
        pass
    def deletePostInfo(self):
        files = os.listdir('./')
        for f in files:
            if f == 'PostInfo.json':
                os.remove(f)
                break
        pass
    def createPostInfo(self):
        path = './Info/'
        fileName = 'PostInfo'
        data = {}
        final = {}
        
        itemnum = 0
        for s in self._posts:  
            data = {
                "imagepath": s.image,
                "text": s.text,
                "title": s.title,
                "year": s.time.year,
                "month": s.time.month,
                "day": s.time.day,
                "hour": s.time.hour,
                "minute": s.time.minute
            }

            final[itemnum] = data
            itemnum += 1
        
        # create file with info
        filePathNameWExt = './' + path + '/' + fileName + '.json'
        with open(filePathNameWExt, 'w') as fp:
            json.dump(final, fp)
        pass
    def loadPostInfo(self):
        files = os.listdir('./Info/')
        for f in files:
            if f == 'PostInfo.json':
                self._postInfo = json.load(open(os.path.join('./Info/', f)))
                break
        pass
    def loadPosts(self):
        x = 0
        done = False
        while done == False:
            try:
                p = self._postInfo[str(x)]
                image = p['imagepath']
                text = p['text']
                title = p['title']
                year = p['year']
                month = p['month']
                day = p['day']
                hour = p['hour']
                minute = p['minute']
                
                dt = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), 0, 0)

                newPost = Post(image, text, dt, title, self._curPostID)
                self._posts.append(newPost)

                self._curPostID += 1
                x += 1
                print(x)
            except:
                done = True
                print("End")
    def deletePost(self):
        self.cls()
        done = False
        while done == False:
            ans2 = raw_input('ID of post to delete:')

            try:
                for p in self._posts:   
                    if int(p.postID) == int(ans2):
                        self._posts.remove(p)
                        print('Removed')
                        pass
                self._postInfo = {}
                self.deletePostInfo()
                self.createPostInfo()
                self.loadPostInfo()
            except:
                print('Invalid ID')

            ans3 = raw_input('Delete another post? [Y/N]')
            
            if ans3 == 'Y' or ans3 == 'y':
                pass
            else:
                done = True
        
        pass
    def postIfReady(self):
        for p in self._posts:
            if p.time < datetime.datetime.now():
                print('Post ID {} is now posting'.format(p.postID))
                self.postAll(p)
                self._posts.remove(p)
                self._postInfo = {}
                self.deletePostInfo()
                self.createPostInfo()
                self.loadPostInfo()
    def postAll(self, post):
        for m in self._mediaSources:
            m.post(post)
    def main(self):
        self.setUp()

        # options loop
        end = False
        while end == False:
            self.cls()
            print('Options')                          
            print('Create post for later  -p')
            print('Create post for now    -n')
            print('Delete post by ID      -dp')
            print('Add Account            -a')  
            print('Delete Account         -d')  
            print('List Accounts          -l')     
            print('List Posts             -lp')              
            print('Exit                   -e')
            ans = raw_input()

            if ans == '-e':
                end = True
            elif ans == '-l':
                self.printAllMediaSources()
            elif ans == '-a':
                self.addAccount()
            elif ans == '-d':
                self.deleteAccount()
            elif ans == '-n':
                self.postNow()
            elif ans == '-p':
                self.createPostForLater()
            elif ans == '-lp':
                self.listPosts()
            elif ans == '-dp':
                self.deletePost()
        

        return



_mediaBot = MediaBot()
_mediaBot.main()

# print(os.listdir('./Info/'))