from urllib import response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import config, download

def init_driver():
    print('Abrindo navegador...')
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('prefs', {'download.default_directory' : config.FILES2})
    #chromeOptions.add_argument('log-level=3')
    driver = webdriver.Chrome(config.CHROMEDRIVER, options=chromeOptions)
    return driver

def wait(elementName):
    driver = init_driver()
    try:
        myElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, elementName))
    )
    finally:
        driver.quit()

def main():
    #driver = init_driver()
    #download.tarifas(driver)
    
    download.rename()

if __name__ == '__main__':
    main()