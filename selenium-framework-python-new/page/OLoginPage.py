import WebDriverFactory
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import BasePage

class OLoginPage(BasePage.BasePage):
		
	
	elmUserName=(By.ID,"txtUsername")
	elmPassword=(By.ID,"txtPassword")
	elmLoginButton=(By.ID,"btnLogin")
	
	
	
	
	def __init__(self):
		self.wait=WebDriverWait(WebDriverFactory.WebDriverFactory.getDriver(),20)
		self.driver=WebDriverFactory.WebDriverFactory.getDriver()
		
	def navigateToLoginPage(self):
		self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
		return self
		
	def loginOrangeHRM(self,strUserName,strUserPassword):
		self.findElementBy(self.elmUserName).send_keys(strUserName)
		self.findElementBy(self.elmPassword).send_keys(strUserPassword)
		self.findElementBy(self.elmLoginButton).click()
		return self
	
