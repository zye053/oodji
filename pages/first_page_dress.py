from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class First_dress(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    yellow_color = "//*[@id='catalog-width']/div[1]/dl/dd[1]/div/div[2]/span[7]/a/picture/img"
    xs_size = "//*[@id='available']/div[2]/div/div[1]/label/input"
    button_add_to_cart = "//*[@id='available']/div[3]/div[1]/div[2]/a[1]"
    return_to_women_collection = "/html/body/div[2]/div/div/div[1]/ul/li[2]/a"

    # Getters
    def get_yellow_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.yellow_color)))

    def get_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xs_size)))

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_return_to_women_collection(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.return_to_women_collection)))

    # Actions
    def click_yellow_color(self):
        self.get_yellow_color().click()
        print('Choose for dress yellow color')

    def click_xs_size(self):
        self.get_size().click()
        print('Choose dress size')

    def scroll_dress_page(self):
        self.driver.execute_script('window.scrollTo(0,200)')
        print('Scroll dress page')

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print('Add to cart')

    def click_return_to_women_collection(self):
        self.get_return_to_women_collection().click()
        print('Return to women collection')

    # Methods

    def add_to_cart(self):
        self.click_yellow_color()
        self.click_xs_size()
        self.scroll_dress_page()
        self.click_button_add_to_cart()
        self.click_return_to_women_collection()

