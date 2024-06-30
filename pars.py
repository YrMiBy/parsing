import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://www.divan.ru/search?ProductSearch%5Bname%5D=светильники&categories%5B%5D=2246"
driver.get(url)
time.sleep(5)

svets = driver.find_elements(By.CLASS_NAME, '_Ud0k')
print(svets) # Выводим вакансии на экран
parsed_data = []
for svet in svets:
    try:
        name = svet.find_element(By.CSS_SELECTOR, 'div.lsooF').text # название
        prise = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2').text # цена
        url = svet.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue

    parsed_data.append([name, prise, url])
driver.quit()

with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)
