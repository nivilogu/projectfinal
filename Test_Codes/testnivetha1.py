from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Test_Data.data import Nivetha_Data
from Test_locators.locators import Nivetha_locators
import pytest 


class Test_Nivetha:
    
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
   
    def test_get_title(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.get(Nivetha_Data().url)
        assert self.driver.title =='OrangeHRM'
        print("SUCCESS : Web Title Captured")
   
    def test_login(self, boot):
        self.driver.get(Nivetha_Data().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Nivetha_locators().username_locator).send_keys(Nivetha_Data().username)
        self.driver.find_element(by=By.NAME, value=Nivetha_locators().password_locator).send_keys(Nivetha_Data().password)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().submitBox_locator).click()
        print("SUCCESS : Logged in with the Username {a} & {b}".format(a=Nivetha_Data().username, b=Nivetha_Data().password))
    
    

 