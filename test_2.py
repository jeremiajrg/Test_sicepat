from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

##@pytest.fixture
##def setup():
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(10)

username = 'standard_user'
password = 'secret_sauce'

def test_login_user_berhasil():
    driver.find_element(By.ID,'user-name').send_keys(username)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()
    time.sleep(5)
    Product = driver.find_element(By.CLASS_NAME,"title").text
    assert Product == "Products"

def test_add_to_cart_sukses():
    driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack').click()
    time.sleep(2)
    Keranjang = driver.find_element(By.CLASS_NAME,'shopping_cart_link').text
    assert Keranjang == '1'

def test_harga_sesuai():
    driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    time.sleep(2)
    Check_Price = driver.find_element(By.CLASS_NAME,'inventory_item_price').text
    assert Check_Price == '$29.99'

def test_checkout_berhasil():
    driver.find_element(By.ID,'checkout').click()
    time.sleep(2)
    driver.find_element(By.ID,'first-name').send_keys('Je')
    driver.find_element(By.ID,'last-name').send_keys('Test')
    driver.find_element(By.ID,'postal-code').send_keys('12098')
    time.sleep(2)
    driver.find_element(By.ID,'continue').click()
    time.sleep(2)
    driver.find_element(By.ID,'finish').click()
    time.sleep(2)
    Finish = driver.find_element(By.CSS_SELECTOR,'.complete-header').text
    assert Finish == 'Thank you for your order!'
    driver.quit()