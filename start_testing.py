import tests

mainPageQuestion = tests.MainPageQuestion(tests.driver)
order_scooter = tests.OrderScooter(tests.driver)
navigation_on_the_page = tests.NavigationOnThePage(tests.driver)
def test_question1():
    mainPageQuestion.test_click_on_the_question1()
def test_question2():
    mainPageQuestion.test_click_on_the_question2()
def test_question3():
    mainPageQuestion.test_click_on_the_question3()
def test_question4():
    mainPageQuestion.test_click_on_the_question4()
def test_question5():
    mainPageQuestion.test_click_on_the_question5()
def test_question6():
    mainPageQuestion.test_click_on_the_question6()
def test_question7():
    mainPageQuestion.test_click_on_the_question7()
def test_question8():
    mainPageQuestion.test_click_on_the_question8()
def test_order_scooter():
    order_scooter.test_scooter_order()
def test_yandex_button():
    navigation_on_the_page.test_navigation_on_the_page_yandex_button()
def test_scooter_button():
    navigation_on_the_page.test_navigation_on_the_page_scooter_button()