# coding=utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest


class login(unittest.TestCase):
    def denglu(self):
        try:
            my_count = self.driver.find_element_by_css_selector('.wp.header-top-con.clearfix').text
            print(my_count)
            print(my_count[15: 19])
            t = my_count[15: 19]
            print(t)
            return t
        except:
            t = ''
            print('发生了')
            return t

    def setUp(self):
        # 打开网站
        self.driver.get('http://www.acfun.cn/')
        sleep(1)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print('bbb')
        cls.driver.quit()

    @classmethod
    def setUpClass(cls):
        print('aaa')
        # 加载插件
        profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\s6qtifzn.default'
        profile = webdriver.FirefoxProfile(profile_directory)
        cls.driver = webdriver.Firefox(profile)

    def test1(self):
        # 点击登录账号
        self.driver.find_element_by_css_selector('.item.user-login').click()
        # 切换窗口
        handle_all = self.driver.window_handles
        print(handle_all)
        self.driver.switch_to.window(handle_all[-1])
        # 切换为账号密码登录
        self.driver.find_element_by_css_selector('#login-account-switch').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#ipt-account-login').send_keys('13250472225')
        self.driver.find_element_by_css_selector('#ipt-pwd-login').send_keys('199209281114')
        self.driver.find_element_by_css_selector('.btn-login').click()
        sleep(5)
        print(self.driver.title)

        mouse = self.driver.find_element_by_css_selector('.user-avatar.item')
        ActionChains(self.driver).move_to_element(mouse).perform()
        sleep(2)
        my_count = self.driver.find_element_by_css_selector('.wp.header-top-con.clearfix').text
        print(my_count)
        print(my_count[15: 19])
        t = my_count[15: 19]
        sleep(1)
        self.assertTrue(t == '天然的书')

    def test2(self):
        # 点击登录账号
        self.driver.find_element_by_css_selector('.item.user-login').click()
        # 切换窗口
        handle_all = self.driver.window_handles
        self.driver.switch_to.window(handle_all[-1])
        # 切换为账号密码登录
        self.driver.find_element_by_css_selector('#login-account-switch').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#ipt-account-login').send_keys('13250472225')
        self.driver.find_element_by_css_selector('#ipt-pwd-login').send_keys('199209281114!')
        self.driver.find_element_by_css_selector('.btn-login').click()
        sleep(5)
        print(self.driver.title)
        mouse = self.driver.find_element_by_css_selector('.user-avatar.item')
        ActionChains(self.driver).move_to_element(mouse).perform()
        sleep(2)
        a = self.denglu()
        self.assertTrue(a == '')
