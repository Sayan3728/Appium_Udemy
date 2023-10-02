from appium import webdriver
import unittest

class SampleTest(unittest.TestCase):
    def setUp(self):
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
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

    def test_sample(self):
        pass

    def tearDown(self):
        self.driver.quit()