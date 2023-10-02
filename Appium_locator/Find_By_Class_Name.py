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

ele_id=driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")
ele_id.click()
time.sleep(8)

ele_classname=driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText")
ele_classname.send_keys("Skill2lead")
