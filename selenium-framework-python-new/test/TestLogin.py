import inspect
import pytest
import sys
sys.path.append('../page/')
sys.path.append('../common/')

import WebDriverFactory,DataProvider,AbstractSelenium,LoginPage

class TestLogin(AbstractSelenium.AbstractSelenium):

    @pytest.mark.parametrize("userName,userPassword", [("admin","admin123")])
    def test_verifyLoginSuccessfully(self,userName,userPassword):
        print("*********** in test1",userName)
        LoginPage.LoginPage().navigateToLoginPage().login(userName,userPassword)
    @pytest.mark.parametrize("userName", [("vaibhavz"),("zodge")])
    def test_verifyLoginForInvalidUser(self,userName):
        print("*********** in test1",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForInvalidUser(userName)

    @pytest.mark.parametrize("TC_ID,TC_NAME,userName",DataProvider.DataProvider.getData("test_verifyLoginForInvalidUser"))
    def test_verifyLoginForInvalidUser(self,TC_ID,TC_NAME,userName):
        print("*********** in test1",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForInvalidUser(userName)
         
