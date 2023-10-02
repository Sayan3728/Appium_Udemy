from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
desired_capabilities = {
    "platformName": "android",
    "appium:deviceName": "Android SDK built for x86",
    "appium:automationName": "UIAutomator2",
    "appium:appPackage": "com.code2lead.kwad",
    "appium:appActivity": "com.code2lead.kwad.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

ele_xpath=driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn1"]')#Bycon-dec
ele_xpath.click()
time.sleep(2)
# ele_xpath=driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')
# ele_xpath=driver.find_element(AppiumBy.XPATH,'//android.widget.Button[3]')#index
ele_xpath2=driver.find_element(AppiumBy.XPATH,'//android.widget.EditText')
ele_xpath2.send_keys("Sayan")
