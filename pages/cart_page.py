
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart_word = "//*[@id='basket-root']/div[1]/div/h1"
    dress_text = "/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/div/ul/li[1]/div[1]/a"
    jacket_text = "/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/div/ul/li[2]/div[1]/a"

    # Getters

    def get_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_word)))

    def get_dress_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dress_text)))

    def get_jacket_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.jacket_text)))

    #Actions

    # Methods

    def cart_check(self):
        self.get_current_url()
        self.assert_url('https://www.oodji.com/cart/')
        self.assert_word(self.get_dress_text(), 'Платье трикотажное базовое')
        self.assert_word(self.get_jacket_text(), 'Пуховик на молнии с воротником-стойкой')
