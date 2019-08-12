import inspect
import pytest
import sys
sys.path.append('../page/')
sys.path.append('../common/')

import WebDriverFactory,DataProvider,AbstractSelenium,OLoginPage

class TestLoginNew(AbstractSelenium.AbstractSelenium):

    @pytest.mark.parametrize('userName,userPassword',[('admin','admin123')])
    def test_verifyLoginSuccessfully(self,userName,userPassword):
        print ("************ in test",userName,userPassword)
        OLoginPage.OLoginPage().navigateToLoginPage().loginOrangeHRM(userName,userPassword)
    

