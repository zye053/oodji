from datetime import time
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from base.base_class import Base


class Jackets_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    slider = "//*[@id='priceSlider']/span[1]"
    down_jacket = "//*[@id='catalog-width']/div[1]/div[8]/div[3]/a"

    # Getters

    def get_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider)))

    def get_down_jacket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.down_jacket)))

    # Actions
    def scroll_jackets_page(self):
        self.driver.execute_script('window.scrollTo(0,700)')
        print('Scroll jackets page')

    def move_slider(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_slider()).move_by_offset(110, 0).release().perform()
        print('Move_slider')

    def scroll_filtered_jackets_page(self):
        self.driver.execute_script('window.scrollTo(0,400)')
        print('Scroll filtered page')

    def click_down_jacket(self):
        self.get_down_jacket().click()
        print('Click down jacket')

    # Methods

    def choose_jacket(self):
        self.scroll_jackets_page()
        self.move_slider()
        time.sleep(10)
        self.scroll_filtered_jackets_page()
        time.sleep(10)
        self.click_down_jacket()


