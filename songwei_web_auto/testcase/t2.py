from selenium import webdriver
from common.base import Base

profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\s6qtifzn.default'

profile = webdriver.FirefoxProfile(profile_directory)

driver = webdriver.Firefox(profile)
driver.get('https://www.baidu.com/')
r = Base(driver)

print(r.is_title('百度一下，你就知道'))
print(r.is_title_contains('百度'))
loctor = ('id', 'su')
print(r.is_text_in_element(loctor, ''))
print(r.is_value_in(loctor, '百度一'))