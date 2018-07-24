from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
        self.wd = webdriver.Firefox(executable_path=r'E:\GitHub_trainign\geckodriver-v0.21.0-win64\geckodriver.exe',
                                    firefox_binary=binary)
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group - GroupHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()