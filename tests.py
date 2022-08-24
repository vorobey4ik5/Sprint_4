from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from Page_object import *

driver = webdriver.Firefox(executable_path=r'C:\Users\vorob\PycharmProjects\Sprint_4_v_2\geckodriver.exe')
driver.maximize_window()


def test_click_on_the_question1():
    driver.get('https://qa-scooter.praktikum-services.ru/')
    time.sleep(1)
    element = driver.find_element(*question_button_1)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    answer_text = driver.find_element(*answer_button_1)
    assert answer_text.text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

def test_click_on_the_question2():
    element = driver.find_element(*question_button_2)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    answer_text = driver.find_element(*answer_button_2)
    assert answer_text.text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'


def test_click_on_the_question3():
    element = driver.find_element(*question_button_3)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    answer_text = driver.find_element(*answer_button_3)
    assert answer_text.text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

def test_click_on_the_question4():
    element = driver.find_element(*question_button_4)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    answer_text = driver.find_element(*answer_button_4)
    assert answer_text.text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'


def test_click_on_the_question5():
    element = driver.find_element(*question_button_5)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    answer_text = driver.find_element(*answer_button_5)
    assert answer_text.text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'


def test_click_on_the_question6():
    element = driver.find_element(*question_button_6)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    answer_text = driver.find_element(*answer_button_6)
    assert answer_text.text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'


def test_click_on_the_question7():
    element = driver.find_element(*question_button_7)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    answer_text = driver.find_element(*answer_button_7)
    assert answer_text.text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'


def test_click_on_the_question8():
    element = driver.find_element(*question_button_8)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    answer_text = driver.find_element(*answer_button_8)
    assert answer_text.text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'




def test_scooter_order():
    #driver.get('https://qa-scooter.praktikum-services.ru/')
    element = driver.find_element(*button_order_on_the_header)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)
    driver.find_element(*field_firstname_in_the_order_form).send_keys('Дима')
    driver.find_element(*field_secondname_in_the_order_form).send_keys('Воробьев')
    driver.find_element(*field_adress_in_the_order_form).send_keys('улица Пушкина дом 5')
    driver.find_element(*field_station_in_the_order_form).click()
    driver.find_element(By.CSS_SELECTOR, "[value='1']").click()
    driver.find_element(*field_phonenumber_in_the_order_form).send_keys('89605902102')
    driver.find_element(*button_next_in_the_order_form).click()
    driver.find_element(*data_order).send_keys('01.01.2023')
    driver.find_element(*data_order).send_keys(Keys.ENTER)
    driver.find_element(*rental_time).click()
    driver.find_element(*time_delivery).click()
    driver.find_element(*black_color_scooter).click()
    driver.find_element(*comment_for_courier).send_keys('Скорее')
    time.sleep(1)
    driver.find_element(*button_next_in_the_order_form).click()
    time.sleep(1)
    driver.find_element(*button_next_in_the_order_form).click()
    driver.find_element(*button_order_on_the_form).click()
    time.sleep(1)
    driver.find_element(*button_yes).click()
    if driver.find_element(*modal_window_order).is_enabled():
        print('Заказ оформлен')
    else:
        print('Заказ не оформлен')
    driver.find_element(*view_status_button).click()

def test_navigation_on_the_page_yandex_button():
    driver.get('https://qa-scooter.praktikum-services.ru/')
    time.sleep(1)
    driver.find_element(*link_logo_yandex).click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, '//div[@class="modal__close"]').click()
    time.sleep(1)
    if driver.find_element(*logo_yandex).is_enabled:
        print('Открыта вкладка Яндекса')
    else:
        print('Что-то пошло не так')

def test_navigation_on_the_page_scooter_button():
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(*link_logo_scooter).click()
    time.sleep(3)
    text = driver.find_element(*header_text_main_page_scooter)
    if text.is_enabled:
        print('Открыта главная страница Самоката')
    else:
        print('Что-то пошло не так')
    driver.quit()




