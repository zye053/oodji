from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Second_jacket(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    s_size = "//*[@id='available']/div[2]/div/div[3]/label/input"
    button_add_to_cart = "//*[@id='available']/div[3]/div[1]/div[2]/a[1]"
    main_page_link = "/html/body/div[2]/div/div/div[1]/ul/li[1]/a/span"

    # Getters
    def get_s_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.s_size)))

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_main_page_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_page_link)))

    # Actions
    def click_s_size(self):
        self.get_s_size().click()
        print('Choose s size jacket')

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print('Add jacket to cart')

    def click_main_page_link(self):
        self.get_main_page_link().click()
        print('Return to main page')

    # Methods

    def add_jacket_to_cart(self):
        self.click_s_size()
        self.click_button_add_to_cart()
        self.click_main_page_link()


