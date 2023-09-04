from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.base_class import Base
from pages.cart_page import Cart_page
from pages.dresses_page import Women_dresses
from pages.first_page_dress import First_dress
from pages.jackets_page import Jackets_page
from pages.main_page import Main_page
from pages.second_page_jacket import Second_jacket
from pages.women_collection_page import Women_collection


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print('Start test')

    main_page = Main_page(driver)
    main_page.authorisation()

    wc = Women_collection(driver)
    wc.choosing_dress()

    women_dresses = Women_dresses(driver)
    women_dresses.choosing_dress()

    first_dress = First_dress(driver)
    first_dress.add_to_cart()

    wc = Women_collection(driver)
    wc.choosing_jacket()

    jp = Jackets_page(driver)
    jp.choose_jacket()

    sj = Second_jacket(driver)
    sj.add_jacket_to_cart()

    main_page = Main_page(driver)
    main_page.go_to_cart()

    cp = Cart_page(driver)
    cp.cart_check()


    print('Finish test')