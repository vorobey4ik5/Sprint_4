from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from Page_object import *

driver = webdriver.Firefox(executable_path=r'C:\Users\vorob\PycharmProjects\Sprint_4_v_2\geckodriver.exe')
driver.maximize_window()

class MainPageQuestion:

    def __init__(self, driver):
        self.driver = driver

    def test_click_on_the_question1(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        time.sleep(1)
        element = self.driver.find_element(*question_button_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        answer_text = self.driver.find_element(*answer_button_1)
        assert answer_text.text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_click_on_the_question2(self):
        element = self.driver.find_element(*question_button_2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        answer_text = self.driver.find_element(*answer_button_2)
        assert answer_text.text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def test_click_on_the_question3(self):
        element = self.driver.find_element(*question_button_3)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        answer_text = self.driver.find_element(*answer_button_3)
        assert answer_text.text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    def test_click_on_the_question4(self):
        element = self.driver.find_element(*question_button_4)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        answer_text = self.driver.find_element(*answer_button_4)
        assert answer_text.text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_click_on_the_question5(self):
        element = self.driver.find_element(*question_button_5)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        answer_text = self.driver.find_element(*answer_button_5)
        assert answer_text.text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_click_on_the_question6(self):
        element = self.driver.find_element(*question_button_6)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        answer_text = self.driver.find_element(*answer_button_6)
        assert answer_text.text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_click_on_the_question7(self):
        element = self.driver.find_element(*question_button_7)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        answer_text = self.driver.find_element(*answer_button_7)
        assert answer_text.text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_click_on_the_question8(self):
        element = self.driver.find_element(*question_button_8)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        answer_text = self.driver.find_element(*answer_button_8)
        assert answer_text.text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'



class OrderScooter:
    def __init__(self, driver):
        self.driver = driver

    def test_scooter_order(self):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        element = driver.find_element(*button_order_on_the_header)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element(*field_firstname_in_the_order_form).send_keys('Дима')
        self.driver.find_element(*field_secondname_in_the_order_form).send_keys('Воробьев')
        self.driver.find_element(*field_adress_in_the_order_form).send_keys('улица Пушкина дом 5')
        self.driver.find_element(*field_station_in_the_order_form).click()
        self.driver.find_element(By.CSS_SELECTOR, "[value='1']").click()
        self.driver.find_element(*field_phonenumber_in_the_order_form).send_keys('89605902102')
        self.driver.find_element(*button_next_in_the_order_form).click()
        self.driver.find_element(*data_order).send_keys('01.01.2023')
        self.driver.find_element(*data_order).send_keys(Keys.ENTER)
        self.driver.find_element(*rental_time).click()
        self.driver.find_element(*time_delivery).click()
        self.driver.find_element(*black_color_scooter).click()
        self.driver.find_element(*comment_for_courier).send_keys('Скорее')
        time.sleep(1)
        self.driver.find_element(*button_next_in_the_order_form).click()
        time.sleep(1)
        self.driver.find_element(*button_next_in_the_order_form).click()
        self.driver.find_element(*button_order_on_the_form).click()
        time.sleep(1)
        self.driver.find_element(*button_yes).click()
        if self.driver.find_element(*modal_window_order).is_enabled():
            print('Заказ оформлен')
        else:
            print('Заказ не оформлен')
        self.driver.find_element(*view_status_button).click()

class NavigationOnThePage:
    def __init__(self, driver):
        self.driver = driver
    def test_navigation_on_the_page_yandex_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        time.sleep(3)
        self.driver.find_element(*link_logo_yandex).click()
        time.sleep(3)
        self.driver.switch_to.window(driver.window_handles[1])
        self.driver.find_element(By.XPATH, '//div[@class="modal__close"]').click()
        time.sleep(1)
        assert self.driver.find_element(*logo_yandex).is_enabled


    def test_navigation_on_the_page_scooter_button(self):
        self.driver.switch_to.window(driver.window_handles[0])
        self.driver.find_element(*link_logo_scooter).click()
        time.sleep(3)
        text = self.driver.find_element(*header_text_main_page_scooter)
        assert text.is_enabled
        driver.quit()


