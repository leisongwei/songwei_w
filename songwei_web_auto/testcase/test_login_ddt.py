import unittest
from selenium import webdriver
from pages.login_page import LoginPage, login_url
import ddt
from common.read_excel import ExcelUtil

profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\s6qtifzn.default'
profile = webdriver.FirefoxProfile(profile_directory)

# testdatas = [
#     {'user': 'admin123', 'psw': 'admin123', 'expect': 'admin123'},
#     {'user': 'admin123', 'psw': '', 'expect': ''},
#     {'user': 'admin111', 'psw': 'admin123', 'expect': ''}
# ]

filepath = "C:\\web_test\\common\\datas.xls"
data = ExcelUtil(filepath)
testdatas = data.dict_data()
print(testdatas)

@ddt.ddt
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(profile)
        cls.loginp = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def login_case(self, user, psw, expect):
        self.loginp.input_user(user)
        self.loginp.input_psw(psw)
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        print('测试结果 %s' % result)
        self.assertTrue(result == expect)

    @ddt.data(*testdatas)
    def test01(self, data):
        '''输入admin123，密码admin123,点击登录成功登陆'''
        print('-------------开始测试：test01---------------')
        print('测试数据：%s' % data)
        self.login_case(data['user'], data['psw'], data['expect'])
        print('-------------结束测试：pass---------------', end='\n\n\n\n\n')

    # def test02(self):
    #     """输入admin123,点击登录"""
    #     print('-------------开始测试：test02---------------')
    #     data2 = testdatas[1]
    #     self.login_case(data2['user'], data2['psw'], data2['expect'])
    #     print('-------------结束测试：pass---------------')
    #
    # def test03(self):
    #     '''输入admin111，密码admin123'''
    #     print('-------------开始测试：test03---------------')
    #     data3 = testdatas[2]
    #     self.login_case(data3['user'], data3['psw'], data3['expect'])
    #     print('-------------结束测试：pass---------------')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()