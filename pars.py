from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random

tema = input('Введите выбранную Вами тему: ')
browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(tema)
search_box.send_keys(Keys.RETURN)

def choise_1():
    browser = webdriver.Chrome()  # Прописываем код
    browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(tema)
    search_box.send_keys(Keys.RETURN)
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:  # Для перебора пишем цикл
        print(paragraph.text)

def choise_2():
    browser = webdriver.Chrome()  # Прописываем код
    browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(tema)
    search_box.send_keys(Keys.RETURN)
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)
    print(hatnotes)
    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)

choice = '0'
while choice < '3':
    print('Выберите дальнейшие действия:')
    print('1 - Просматривать параграфы текущей статьи')
    print('2 - Перейти на страницу')
    print('3 - Выйти из программы')
    choise = input('Ваш выбор: ')
    if choise == '1':
        choise_1()
    elif choise == '2':
        choise_2()
    else: break
    while choice < '3':
        print('Выберите дальнейшие действия:')
        print('1 - Просматривать параграфы текущей статьи')
        print('2 - Перейти на страницу')
        print('3 - Выйти из программы')
        choise = input('Ваш выбор: ')
        if choise == '1':
            choise_1()
        elif choise == '2':
            choise_2()
        else: break
