class LogIn():
    def __init__(self, llq):
        self.driver = llq

    def login(self, user='13250472225', password='199209281114'):

        self.driver.get('http://www.acfun.cn/')
        # self.driver.find_element_by_css_selector('#ipt-account-login').send_keys(user)
        # self.driver.find_element_by_css_selector('#ipt-pwd-login').send_keys(password)
        # self.driver.find_element_by_css_selector('.btn-login').click()


if __name__ == "__main__":
    from selenium import webdriver
    huohullq = webdriver.Firefox()
    a = LogIn(huohullq)
    a.login()



