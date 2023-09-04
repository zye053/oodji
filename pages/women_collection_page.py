from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Women_collection(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    dresses = "//*[@id='bx_4153539902_271']/a/span"
    jackets = "//*[@id='bx_4153539902_199']/a/span"

    # Getters
    def get_dresses(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dresses)))

    def get_jackets(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.jackets)))


    # Actions

    def click_dresses(self):
        self.get_dresses().click()
        print('Choose dresses')

    def scroll_page(self):
        self.driver.execute_script('window.scrollTo(0,400)')
        print('Scroll page to jackets')

    def click_jackets(self):
        self.get_jackets().click()
        print('Choose jackets')

    # Methods

    def choosing_dress(self):
        self.click_dresses()

    def choosing_jacket(self):
        self.scroll_page()
        self.click_jackets()
