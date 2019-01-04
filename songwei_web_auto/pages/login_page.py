import time
from selenium import webdriver
from common.base import Base

login_url = "https://leisongwei.5upm.com/user-login.html"


class LoginPage(Base):
    #    定位登录
    loc_user = ('id', 'account')
    loc_psw = ('name', 'password')
    loc_button = ('id', 'submit')
    loc_keep = ('id', 'keepLoginon')
    loc_login_name = ('css selector', '.user-name')

    def input_user(self, text=''):
        self.sendText(self.loc_user, text)

    def input_psw(self, text=''):
        self.sendText(self.loc_psw, text)

    def click_login_button(self):
        self.click(self.loc_button)

    def click_keep_login(self):
        self.click(self.loc_keep)

    def get_login_name(self):
        try:
            r = self.get_text(self.loc_login_name)
            return r
        except:
            return ''

    def login(self, user='admin123', password='admin123'):
        """直接登录流程"""
        self.driver.get(login_url)
        self.input_user(user)
        self.input_psw(password)
        self.click_login_button()

    def is_alert_exist(self):
        a = self.is_alert()
        if a:
            print(a.text)
            a.accept()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    login_page.login()
    # driver.get(login_url)
    # login_page.input_user('admin123')
    # login_page.input_psw('admin123')
    # login_page.click_keep_login()
    # login_page.click_login_button()

