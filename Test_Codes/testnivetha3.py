from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Test_Data.data import Nivetha_Data
from Test_locators.locators import Nivetha_locators
import pytest 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
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
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().PIM_locator).click()

    # def test_Add(self, boot):
        self.driver.implicitly_wait(25)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().Add_locator).click()

    # def test_Addemployee(self, boot):
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
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().save_locator).click()
        
        
    # def test_personal_details(self, boot):
     
    #     self.driver.find_element(by=By.XPATH, value=Nivetha_locators().Nickname_l).send_keys(Nivetha_Data().Nickname)
        # self.driver.find_element(by=By.XPATH, value=Nivetha_locators().otherid_l).send_keys(Nivetha_Data().otherid)
#         self.driver.find_element(by=By.XPATH, value=Nivetha_locators().dln_l).send_keys(Nivetha_Data().dln)
#         self.driver.find_element(by=By.XPATH, value=Nivetha_locators().save_l).click()
    # def test_select_license_ed(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value =Nivetha_locators().license_l).send_keys(Nivetha_Data().license)
        # self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.XPATH, value = Nivetha_locators().SSN_l).send_keys(Nivetha_Data().SSN)
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.XPATH, value = Nivetha_locators().SIN_l).send_keys(Nivetha_Data().SIN)
     
    
    # def select_by_nationality(self):
#         print('method-select_by_nationality')
#         sleep(3)
        # self.driver.implicitly_wait(20)
        # nationality = self.driver.find_element(by=By.XPATH, value =Nivetha_locators().nationality_l).click()
        # nationality_dropdown = Select(nationality)
        # nationality_dropdown.select_by_visible_text("American")

    # def test_select_marital_status(self, boot): 
        self.driver.implicitly_wait(10)
        marital_status = self.driver.find_element(by=By.XPATH, value =Nivetha_locators().maritalstatus_l)
        marital_status_dropdown = Select(marital_status)
        marital_status_dropdown.select_by_visible_text('married')
        

    # def test_select_by_dob(self, boot):
        self.driver.implicitly_wait(10)
        dob = self.driver.find_element(by=By.XPATH , value=Nivetha_locators().dob_l).click()
        dob_dropdown = Select(dob)    
        dob_dropdown.select_by_value('1992-02-10')   
     
    # def test_gender(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value = Nivetha_locators().gender_l).click()
    # def test_militaryservice(self, boot):
        self.driver.implicitly_wait(10)  
        self.driver.find_element(by=By.XPATH, value = Nivetha_locators().militaryservice_l).send_keys(Nivetha_Data().militaryservice)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().save_pd).click()
    # def test_blood_type(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value = Nivetha_locators().bloodtype_l).send_keys(Nivetha_Data().bloodtype)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=Nivetha_locators().save_cf).click() 


