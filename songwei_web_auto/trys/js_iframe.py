from selenium import webdriver
from pages.login_page import LoginPage


driver = webdriver.Firefox()
login_js = LoginPage(driver)
login_js.login()
driver.get('https://leisongwei.5upm.com/bug-create-1-0-moduleID=0.html')
text = 'hello,hello,hello,hellohello,hellohellohellohello'
js = "document.getElementsByClassName('ke-edit-iframe')[0].contentWindow.document.body.innerHTML='%s'" % text
driver.execute_script(js)
