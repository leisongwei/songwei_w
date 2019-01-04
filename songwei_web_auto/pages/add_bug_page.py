import time
from selenium import webdriver
from common.base import Base
from pages.login_page import LoginPage


class AddBugPage(Base):
    #  定位bug
    loc_test = ('link text', '测试')
    loc_bug = ('link text', 'Bug')
    loc_Add_Bug = ('css selector', '.btn-primary>.icon.icon-plus')
    loc_struck = ('css selector', '#openedBuild_chosen>.chosen-choices')
    loc_struck_add = ('css selector', '.active-result.highlighted')
    loc_input_title = ('id', 'title')
    loc_input_body = ('css selector', '.article-content>p')
    loc_save = ('css selector', '#submit')
    # 新增加的列表
    loc_new = ('xpath', ".//*[@id='bugList']/tbody/tr[1]/td[3]/a")

    def add_bug(self, title='测试标题BUG'):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_Add_Bug)
        self.click(self.loc_struck)
        self.click(self.loc_struck_add)
        self.sendText(self.loc_input_title, title)
        # 输入Body
        self.driver.switch_to.frame(1)
        self.sendText(self.loc_input_body, 'bug中文')
        self.driver.switch_to.default_content()
        self.click(self.loc_save)

    def is_add_success(self, text):
        return self.is_text_in_element(self.loc_new, text)


# 加载插件
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\s6qtifzn.default'
profile = webdriver.FirefoxProfile(profile_directory)

if __name__ == '__main__':
    driver = webdriver.Firefox(profile)
    degnlu = LoginPage(driver)
    degnlu.login()
    zentao = AddBugPage(driver)
    str = time.strftime('%Y_%m_%d_%H_%M_%S')
    title = '测试标题bug'+str
    zentao.add_bug(title)
    result = zentao.is_add_success(title)
    print(result)




