from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert

global driver

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.ffasecurity.com")
driver.implicitly_wait(0.5)
user_box = driver.find_element(By.NAME, value='username')
pass_box = driver.find_element(By.NAME, value='password')
login_button = driver.find_element(By.XPATH, value="//input[@type='submit']")


user_box.send_keys('ryker2333@gmail.com')

pass_box.send_keys('Bulletstorm2333')
login_button.click()

driver.implicitly_wait(2.0)
driver.get("https://www.ffasecurity.com/admin/schedules/view/84")
driver.implicitly_wait(2.0)

#shifts = driver.find_elements(By.XPATH, value="//tr[td[text()[contains(.,'Monday')]]]/following-sibling::tr[1]/td/a[1] | //tr[td[text()[contains(.,'Tuesday')]]]/following-sibling::tr[1]/td/a[1] | //tr[td[text()[contains(.,'Wednesday')]]]/following-sibling::tr[1]/td/a[1]")
#
#for shift in shifts:
#    shift.click()
#    WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())
#    alert = Alert(driver)
#    print(alert.text)
#    alert.dismiss()

while(True):
    shifts = driver.find_elements(By.XPATH, value="//tr[td[text()[contains(.,'Monday')]]]/following-sibling::tr[1]/td/a[1] | //tr[td[text()[contains(.,'Tuesday')]]]/following-sibling::tr[1]/td/a[1] | //tr[td[text()[contains(.,'Wednesday')]]]/following-sibling::tr[1]/td/a[1]")

    for shift in shifts:
        shift.click()
        WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())
        alert = Alert(driver)
        print(alert.text)
        alert.accept()
    driver.refresh()
    driver.implicitly_wait(3)

    
driver.implicitly_wait(30)
driver.close()