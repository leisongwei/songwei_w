
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Base():
    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 5
        self.t = 0.5

    def js_focus_element(self,locator):
        """画面滚动到指定元素，聚焦元素"""
        target = self.findElement(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', target)

    def js_scroll_top(self):
        self.driver.execute_script('window.scrollTo(0,0)')

    def js_scroll_end(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    def select_by_index(self, loctor, index=0):
        """通过索引查找选择select选项框"""
        element = self.findElement(loctor)
        Select(element).select_by_index(index)

    def selet_by_value(self, loctor, value):
        """通过value查找选择select选项框"""
        element = self.findElement(loctor)
        Select(element).select_by_value(value)

    def selet_by_text(self, loctor, text):
        """通过文本查找选择select选项框"""
        element = self.findElement(loctor)
        Select(element).select_by_visible_text(text)

    def findElement(self, loctor):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loctor))
        return ele

    def findElementNew(self,loctor):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loctor))
        return ele

    def sendText(self,loctor,text):
        ele = self.findElementNew(loctor)
        ele.send_keys(text)

    def click(self, loctor):
        ele = self.findElement(loctor)
        ele.click()


    def isElementExict(self, loctor):
        try:
            ele = self.findElement(loctor)
            return True
        except:
            return False

    def is_title(self, _title):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
        return ele

    def is_title_contains(self, _title):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
        return ele

    def is_text_in_element(self, loctor, _text):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(loctor, _text))
        return ele

    def is_value_in(self, loctor, _value):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(loctor, _value))
        return ele

    def get_text(self, locator):
        try:
            t = self.findElement(locator).text
            return t
        except:
            print('获取文本失败，返回""')
            return ''

    def get_title(self):
        return self.driver.title

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def move_to_element(self, locator):
        """鼠标悬停操作"""
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://passport.bilibili.com/login')
    bili = Base(driver)
    loc1 = ('xpath', "//*[@id = 'login-username']")
    bili.sendText(loc1, '777777777')
    bili.move_to_element()
