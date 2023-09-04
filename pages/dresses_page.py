from datetime import time
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains

from base.base_class import Base


class Women_dresses(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    filter = "//*[@id='sort_section_top']"
    filter_criterion = "//*[@id='sort_section_top']/option[1]"
    dress = "//*[@id='catalog-width']/div[1]/div[8]/div[3]/a"
    pages_button = "//*[@id='catalog-width']/div[1]/div[5]/div/div[2]/a[5]"

    # Getters
    def get_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter)))

    def get_filter_criterion(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_criterion)))

    def get_dress(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dress)))

    def get_pages_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pages_button)))


    # Actions
    def click_filter(self):
        self.get_filter().click()
        print('Click filter')

    def up_filter(self):
        self.get_filter().send_keys(Keys.UP)
        print('Move to filter')

    def click_filter_criterion(self):
        self.get_filter_criterion().click()
        print('Click filter criterion')

    def scroll_dress(self):
        self.driver.execute_script('window.scrollTo(0,450)')
        print('Scroll to dress')

    def click_dress(self):
        self.get_dress().click()
        print('Click dress')

    # Methods

    def choosing_dress(self):
        self.click_filter()
        self.up_filter()
        time.sleep(5)
        self.click_filter_criterion()
        time.sleep(5)
        self.scroll_dress()
        time.sleep(5)
        self.click_dress()




