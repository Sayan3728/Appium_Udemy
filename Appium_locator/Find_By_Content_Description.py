
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

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

ele_cd=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("Btn3")')
ele_cd.click()