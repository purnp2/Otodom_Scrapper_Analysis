from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
url = 'https://www.otodom.pl/pl/oferta/2-pokojowe-mieszkanie-37m2-balkon-ID4oXEA'

def get_data_from_home_page(home_page_url):
    driver.get(home_page_url)
    # Scroll to the end of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for the page to load
    time.sleep(5)
    # find button id onetrust-accept-btn-handler and click it
    button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    button.click()

    # Get page source and parse it
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    anchor_ele = soup.find('a', title="Zgłoś do Google błędy na mapie drogowej lub na zdjęciach.")
    # wait if anchor_ele is None

    # find the button with id "map" and click it
    button = driver.find_element(By.ID, "map")
    button.click()

    while anchor_ele is None:
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        anchor_ele = soup.find('a', title="Zgłoś do Google błędy na mapie drogowej lub na zdjęciach.")
        if anchor_ele:
            break
        else:
            continue
    return anchor_ele
print(get_data_from_home_page(url))

