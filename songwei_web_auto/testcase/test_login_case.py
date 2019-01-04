import unittest
from selenium import webdriver
from pages.login_page import LoginPage, login_url
import ddt


class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test01(self):
        '''输入admin123，密码admin123,点击登录成功登陆'''
        self.loginp.input_user('admin123')
        self.loginp.input_psw('admin123')
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == 'admin123')

    def test02(self):
        """输入admin123,点击登录"""
        self.loginp.input_user('admin123')
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == '')

    def test03(self):
        '''输入admin123，密码admin123,点击记住密码，登录成功登陆'''
        self.loginp.input_user('admin123')
        self.loginp.input_psw('admin123')
        self.loginp.click_keep_login()
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == 'admin123')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()