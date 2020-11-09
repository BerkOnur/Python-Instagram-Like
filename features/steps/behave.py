from behave import given, when, then 
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

global foto_sayisi
driver = webdriver.Chrome()
@given('I visit instagram')
def visit(context):
    driver.get('https://www.instagram.com/')

@when('I see log in form')
def check(context):
    wait = WebDriverWait(driver, 10)
    wait.until(presence_of_element_located((By.NAME, "username")))

@then('login with username "{username}" and password "{password}"')
def login(context, username, password):
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password + Keys.ENTER)

@then('I close popup "Accept"')
def look(context):
    wait = WebDriverWait(driver, 10)
    wait.until(presence_of_element_located((By.XPATH, '//button[text()="Şimdi Değil"]'))).click()

@then('I close popup "Şimdi Degil"')
def close(context):
    wait = WebDriverWait(driver, 10)
    wait.until(presence_of_element_located((By.XPATH, '//button[text()="Şimdi Değil"]'))).click()
    sleep(2)

@then('I click search form')
def anasayfa(context):
    driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys('user_name' + Keys.ENTER)

@then ('I click user profil')
def user(context):
    global foto_sayisi
    wait = WebDriverWait(driver, 10)
    wait.until(presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div'))).click()
    sleep(2)
    foto_sayisi = int(wait.until(presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span'))).text)

@then('I scroll all the way down')
def scroll(context):
    element = driver.find_element_by_tag_name('footer')
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        element.location_once_scrolled_into_view
        sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        else:
            last_height = new_height
            
@then ('I scroll all the way up')
def photo(context):
    element = driver.find_element_by_tag_name('header')
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        element.location_once_scrolled_into_view
        sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        else:
            last_height = new_height


@then('I click first photo')
def click(context):
    sleep(3)
    wait = WebDriverWait(driver, 10)
    wait.until(presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a"))).click()
    sleep(2)
    
@then('I click like button and continue')
def like(context):
    global foto_sayisi
    for sayi in range(foto_sayisi-1):
        elements = driver.find_elements_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button")
        for element in elements:
            sleep(2)
            tikla = driver.find_elements_by_xpath('//article//section//button//*[@aria-label="Beğen"]')
            for a in tikla:
                a.click()
        sleep(2)
        webdriver.ActionChains(driver).move_to_element(element).send_keys(Keys.RIGHT).perform()
        sleep(2)
        