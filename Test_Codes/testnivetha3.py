from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Test_Data.data import Nivetha_Data
from Test_locators.locators import Nivetha_locators
import pytest 
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys



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
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().PIM_locator).click()
        self.driver.implicitly_wait(25)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().Add_locator).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.NAME, value=Nivetha_locators().firstName_locator).send_keys(Nivetha_Data().first_Name)
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.NAME, value=Nivetha_locators().middlename_locator).send_keys(Nivetha_Data().middle_Name)
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.NAME, value=Nivetha_locators().lastname_locator).send_keys(Nivetha_Data().last_Name)
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().createlogindetails_locator).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().u_locator).send_keys(Nivetha_Data().u_name)
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().p_locator).send_keys(Nivetha_Data().pwd)
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().cp_locator).send_keys(Nivetha_Data().c_pwd)
        self.driver.implicitly_wait(8)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().save_locator).click()
        self.driver.implicitly_wait(8)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input').send_keys('kutty')
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input').send_keys('989898')
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys('9878789098')
        self.driver.implicitly_wait(8)

        self.driver.find_element(by=By.XPATH, value =Nivetha_locators().license_l).send_keys(Nivetha_Data().license)
        self.driver.implicitly_wait(8)
        self.driver.find_element(by=By.XPATH, value = Nivetha_locators().SSN_l).send_keys(Nivetha_Data().SSN)
        self.driver.implicitly_wait(8)
        self.driver.find_element(by=By.XPATH, value = Nivetha_locators().SIN_l).send_keys(Nivetha_Data().SIN)
        self.driver.implicitly_wait(8)

        dropdown_element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]')
        action_chains = ActionChains(self.driver)
        action_chains.click(dropdown_element).perform()
        self.driver.implicitly_wait(10)
        option_element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[84]').click()
        
        marital_dropdown = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[1]')
        action_chains.click(on_element=marital_dropdown).perform()
        self.driver.implicitly_wait(10)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[3]').click()
        action = ActionChains(self.driver)
        self.driver.implicitly_wait(10)

        dob_dropdown = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').send_keys('1989-04-08')
        sleep(5)
        self.driver.find_element(by=By.XPATH, value = Nivetha_locators().gender_l).click()
        sleep(5)  
        self.driver.find_element(by=By.XPATH, value = Nivetha_locators().militaryservice_l).send_keys(Nivetha_Data().militaryservice)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().save_l).click()
                  
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().save_cf).click() 

        
