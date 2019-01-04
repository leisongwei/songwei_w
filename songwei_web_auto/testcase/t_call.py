from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
r = EC.title_is('百度一下，你就知道')(driver)
print(r)
assert r == True

loc1 = ('id', 'kw')
r = EC.presence_of_element_located(loc1)(driver)
print(r)
