from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Nivetha_Data
from Test_locators.locators import Nivetha_locators
import pytest
from time import sleep
# from selenium.webdriver.support.wait import WebDriverWait



class Test_Nivetha:
    
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
   
    def test_get_title(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.get(Nivetha_Data().url)
        assert self.driver.title == 'nivetha'
        print("SUCCESS : Web Title Captured")
   
    def test_login(self, boot):
        self.driver.get(Nivetha_Data().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Nivetha_locators().username_locator).send_keys(Nivetha_Data().username)
        self.driver.find_element(by=By.NAME, value=Nivetha_locators().password_locator).send_keys(Nivetha_Data().password)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().submitBox_locator).click()
        assert self.driver.title =='OrangeHRM'
        print("SUCCESS : Logged in with the Username {a} & {b}".format(a=Nivetha_Data().username, b=Nivetha_Data().password))
    

    # def test_PIM(self, boot):    
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().PIM_locator).click()
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().empname_l).send_keys(Nivetha_Data().empname)
        sleep(5)
     #    self.driver.find_element(by=By.XPATH, value=self.empid_locator).send_keys(self.empid)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().search_locator).click()
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().editbutton_locator).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().nation_l).send_keys(Nivetha_Data().nation)
        sleep(5)
     #    self.driver.find_element(by=By.XPATH, value=self.nation_l).click()
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().save_l).click()
    # def maritalstatus(self): 
        self.driver.find_element(by=By.XPATH, value =Nivetha_locators().maritalstatus_l).send_keys(Nivetha_Data().maritalstatus_s)  

