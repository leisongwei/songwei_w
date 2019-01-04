from time import sleep
from selenium import webdriver
# 加载插件
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\s6qtifzn.default'
profile = webdriver.FirefoxProfile(profile_directory)
# 打开浏览器
driver = webdriver.Firefox(profile)
driver.get("http://gz.ganji.com/")
sleep(1)

# 滚动到底部
js = 'window.scrollTo(0,document.body.scrollHeight)'
driver.execute_script(js)

# 滚动到顶部
sleep(1)
driver.execute_script("window.scrollTo(0, 0)")

# 滚动到指定位置
ele = driver.find_element_by_link_text('新车')
js = 'arguments[0].scrollIntoView();'
driver.execute_script(js, ele)