from selenium import webdriver
import time
from fake_useragent import UserAgent
import pickle
from multiprocessing import Pool
from random import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_extension("MetaMask.crx")
options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")

# options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)

try:

    private = input("You Private Key: ")
    passw = input("Password MetaMask: ")
    cd = int(input("Кд: "))
    cikl = int(input("Кол-во Циклов: "))


    driver.get("https://sunflower-farmers.com/play/")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
    print("Начинаем настройку MetaMask")
    time.sleep(2)
    item = driver.find_element_by_xpath("//button[@role='button']")
    print(item)
    print(item.text)
    item.click()
    time.sleep(3)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/select-action")
    time.sleep(2)
    # item2 = driver.find_element_by_xpath("//button[@class='first-time-flow__button']")
    driver.find_element_by_class_name("first-time-flow__button").click()
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/metametrics-opt-in")
    time.sleep(2)
    driver.find_element_by_xpath("//button[@data-testid='page-container-footer-next']").click()
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")
    time.sleep(2)
    print("Начинаем импортировать ключи и добавлять пароль")
    clu4iki = driver.find_element_by_xpath("//input[@type='password']")
    # clu4iki = driver.find_element_by_xpath("MuiInput-input")
    clu4iki.send_keys(private)
    time.sleep(1)
    password1 = driver.find_element_by_id("password")
    password1.send_keys(passw)
    password2 = driver.find_element_by_id("confirm-password")
    password2.send_keys(passw)
    print("Были импортированны ключи и добавлен пароль")
    time.sleep(2)
    driver.find_element_by_class_name("first-time-flow__terms").click()
    time.sleep(2)
    driver.find_element_by_class_name("first-time-flow__button").click()
    time.sleep(5)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/end-of-flow")
    time.sleep(5)
    driver.find_element_by_class_name("popover-header__button").click()
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network")
    time.sleep(2)
    elems = driver.find_elements_by_class_name("form-field__input")
    print("Начинаем добавлять сеть Polygon")
    time.sleep(2)
    elems[0].send_keys("Matic Mainnet")
    elems[1].send_keys("https://rpc-mainnet.maticvigil.com/")
    elems[2].send_keys("137")
    elems[3].send_keys("MATIC")
    elems[4].send_keys("https://explorer.matic.network/")
    print("Сеть Polygon добавлена")
    time.sleep(5)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(3)
    driver.get("https://sunflower-farmers.com/play/")
    time.sleep(3)
    driver.find_element_by_xpath("//div[@id='welcome']/div/span").click()
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")
    time.sleep(2)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(3)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(2)
    driver.get("https://sunflower-farmers.com/play/")
    time.sleep(3)
    driver.find_element_by_xpath("//div[@id='welcome']/div/span").click()
    time.sleep(3)


    p = input("Стартуем? ")
    while True:
        i = 0
        b = 0
        while b != cikl:
            i = i + 1
            print(f"Цикл {i}")
            driver.find_element_by_xpath("//div[@id='container']/div[601]/div[6]/div/img[2]").click()
            driver.find_element_by_xpath("//div[@id='container']/div[601]/div[6]/div/div[2]").click()
            time.sleep(1)
            driver.find_element_by_xpath("//div[@id='container']/div[601]/div[8]/div/img[2]").click()
            driver.find_element_by_xpath("//div[@id='container']/div[601]/div[8]/div/div[2]").click()
            time.sleep(1)
            driver.find_element_by_xpath("//div[@id='first-sunflower']/div/img[2]").click()
            driver.find_element_by_xpath("//div[@id='first-sunflower']/div/div[2]/div").click()
            # driver.find_element_by_xpath("//div[@id='first-sunflower']/div/div[2]/div[2]')]").click()
            time.sleep(1)
            driver.find_element_by_xpath("//div[@id='container']/div[601]/div[10]/div/img[2]").click()
            driver.find_element_by_xpath("//div[@id='container']/div[601]/div[10]/div").click()
            time.sleep(1)
            driver.find_element_by_xpath("//div[@id='container']/div[601]/div[7]/div/img[2]").click()
            driver.find_element_by_xpath("//div[@id='container']/div[601]/div[7]/div/div[2]").click()
            time.sleep(cd-3)
            b = b + 1

        driver.find_element_by_xpath(
            "//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAo0lEQVQYlWOUEFH9z4AHsICk9ifJMTy/8gZFlaSOCIPjvEcQBXNOfGNgYOBCNQYsxsAAsgJE/1+xfTuKfISnJ0O0lggjA0hBsZ0liP4PAyD2gdN3wOIsz1/fYpAUVWN4/voWo6SoGszBjCBi6bU3DIz//0PEQJLPLtuA2VK6R8CKQJrBCsCSs/hR3CCV9hGsCBwOIG9iA3BvoocBMsAfkgwMDACLZkKUzRSogAAAAABJRU5ErkJggg==')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='save-error-buttons']/div").click()
        time.sleep(10)
        # driver.execute_script("window.open('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#');")
        time.sleep(5)
        driver.execute_script("window.open('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#');")
        driver.switch_to.window(driver.window_handles[2])
        time.sleep(0.5)
        driver.refresh()
        time.sleep(0.5)
        driver.refresh()
        time.sleep(0.5)
        # driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#confirm-transaction/3372859370146788/token-method")
        y = input("Подтвердил? ")
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        h = input("Сохранилось? ")
        time.sleep(5)
        driver.refresh()
        time.sleep(10)
        driver.find_element_by_xpath("//div[@id='welcome']/div/span").click()
        time.sleep(3)
        h = input("Вошло в аккаунт? ")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
    
