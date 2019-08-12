from selenium import webdriver

class WebDriverFactory:

	def setDriver():
		WebDriverFactory.driver = webdriver.Chrome(r"c:\Users\amit\Selenium\chromedriver.exe") #set driver object to static driver object
		
	def getDriver():
		return WebDriverFactory.driver
