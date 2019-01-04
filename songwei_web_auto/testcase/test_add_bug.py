import time
import unittest
from selenium import webdriver
from pages.add_bug_page import ZenTaoBug
from pages.login_page import Login


class TestAddBug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.bug = ZenTaoBug(cls.driver)
        cls.a = Login(cls.driver)
        cls.a.login()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_bug(self):
        str = time.strftime('%Y_%m_%d_%H_%M_%S')
        title = '测试标题bug' + str
        self.bug.add_bug(title)
        result = self.bug.is_add_success(title)
        print(result)
        assert result


if __name__ == '__main__':
    unittest.main()

