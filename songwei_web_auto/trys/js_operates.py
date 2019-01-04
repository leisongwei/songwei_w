from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://leisongwei.5upm.com/user-login-L2J1Zy1jcmVhdGUtMS0wLW1vZHVsZUlEPTAuaHRtbA==.html')


js = """document.getElementById('account').value='admin123';
        document.getElementsByName('password').value='admin123';
        document.getElementById('keepLoginon').click();
        document.getElementById('submit').click();
    """
driver.execute_script(js)

jquery = '$('#account').val('123')'
driver.execute_script(jquery)