import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):
    url = 'https://www.oodji.com/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    account_link = "//a[@data-src='#popup_login']"
    email = "//input[@id='USER_LOGIN']"
    password = "//input[@id='USER_PASSWORD']"
    enter_button = "//*[@id='login']/div[4]/button"
    women_button = "/html/body/div[2]/header/div[2]/div/div[2]/ul/li[3]/a"
    cart_button = "/html/body/div[2]/header/div[2]/div/div[3]/div[1]/div/a/span[2]"

    # Getters

    def get_account_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_link)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_women_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.women_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    # Actions

    def click_authorisation_button(self):
        self.get_account_link().click()
        print('Click authorisation')

    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Input e-mail')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_enter_button(self):
        self.get_enter_button().click()
        time.sleep(5)
        print('Click enter button')

    def click_women_button(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_women_button()).click().perform() #наводим на кнопку 'женщины'
        time.sleep(5)
        self.get_women_button().click() #кликаем на кнопку 'женщины'
        time.sleep(5)
        print("Go to the section of the women's collection")

    def click_cart_button(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_cart_button()).click().perform()  # наводим на кнопку 'корзина'
        time.sleep(5)
        self.get_cart_button().click()  # кликаем на кнопку 'корзина'
        time.sleep(5)
        print("Go to the cart")

    # Methods

    def authorisation(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        # self.click_authorisation_button()
        # self.input_email('zye053@gmail.com')
        # self.input_password('Oodji123')
        # self.click_enter_button()
        self.click_women_button()

    def go_to_cart(self):
        self.click_cart_button()