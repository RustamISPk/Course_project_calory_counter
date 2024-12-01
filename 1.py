from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

gecko_options = Options()
proxy_username = 'cVXD8c'
proxy_password = 'AW7hB7'
proxy_address = '185.97.79.178'
proxy_port = '8000'
proxy_url = f'http://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}'
gecko_options.add_argument(f'--proxy-server={proxy_url}')
gecko_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
gecko_options.add_argument("--headless")

driver = webdriver.Firefox(options=gecko_options)

try:
    url = 'https://www.avito.ru/moskva/kommercheskaya_nedvizhimost/sdam_ofisnoe_pomeschenie_486.2_m_2206803695?context=H4sIAAAAAAAA_wEfAOD_YToxOntzOjEzOiJsb2NhbFByaW9yaXR5IjtiOjA7fQseF2QfAAAA';
    # url = "https://www.avito.ru/moskva/kommercheskaya_nedvizhimost"
    driver.get(url)
    time.sleep(5)
    page_content = driver.page_source
    print("Содержимое страницы:")
    print(page_content)
    file = open('file.html', 'w')
    file.write(page_content)
finally:
    driver.quit()
