from common.base import Base
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.acfun.cn/login/?returnUrl=http%3A%2F%2Fwww.acfun.cn%2F')
check = Base(driver)
loc1 = ('id', 'login-account-switch')

r1 = check.isElementExict(loc1)
print(r1)