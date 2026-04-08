from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import ui_url
import allure


driver = webdriver.Chrome()


class MovieSearch:
    """
    Этот класс содержит методы, вызываемые тестовым набором test_ui.py, для тестирования функционала интерфейса портала Kinopoisk.ru, содержащего пользовательские сценарии, не требующие авторизации
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(ui_url)
        self.driver.maximize_window()

    @allure.step("Ввести в поле поиска название искомого фильма и нажать кнопку поиска")
    def search_film_by_name(self):
        """
        Метод search_film_by_name вызывается из теста test_ui.py/test_search_movie,
        метод вводит в поле поиска главной страницы портала Кинопоиск название фильма и нажатием кнопки поиска вызывает список результатов, соответствующих запросу.
        """
        self.driver.find_element(By.CSS_SELECTOR, 'input.styles_input__WCRXt.kinopoisk-header-search-form-input__input').send_keys('Мимино')
        self.driver.find_element(By.CSS_SELECTOR, 'svg.styles_icon__a6f9D.search-form-submit-button__icon').click()

    @allure.step("Перейти на страницу фильма и увидеть кнопку просмотра")
    def open_film(self):
        """
        Метод open_film вызывается из теста test_ui.py/test_search_movie,
        выбирает фильм из списка результатов, кликом переходит на страницу фильма и дожидается появления кнопки 
        "Смотреть фильм".
        """
        self.driver.find_element(By.CSS_SELECTOR, '[href="/film/46638/sr/1/"]').click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[text() = 'Смотреть фильм']")))
        return self.driver.title

    @allure.step("Купить билет в кино")
    def by_ticket(self):
        """
        Метод by_ticket вызывается из теста test_ui.py/test_by_ticket,
        нажимает по локатору на кнопку "Билеты в кино", переходит на страницу с выбором фильма, нажимает на раздел выбранного фильма и переходит на его страницу, нажимает по локатору на кнопку "Купить билеты" и переходит на страницу "Афиша", для выбора сеансов.Возвращает для проверки текущий URL.
        """
        self.driver.find_element(By.CSS_SELECTOR, '[href="/lists/movies/movies-in-cinema/"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="movie-list-item"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[href="/film/6155731/afisha/city/1/"]').click()
        return self.driver.current_url

    @allure.step("Перейти на страницу с медиа-материалами")
    def media_page(self):
        """
        Метод media_page вызывается из теста test_ui.py/test_media_page,
        Нажимает по локатору кнопку "Медиа" на главной странице портала Кинопоиск и переходит на страницу с медиа-материалами. Возвращает для проверки текущий URL.
        """
        self.driver.find_element(By.XPATH, "//*[text() = 'Медиа']").click()
        return self.driver.current_url

    @allure.step("Найти информацию об актёре")
    def search_actor_by_name(self):
        """
         Метод search_actor_by_name вызывается из теста test_ui.py/test_search_actor,
         метод вводит в поле поиска имя актёра, нажимает кнопку поиска, переходит на страницу с результатами, нажимает раздел с выбранным актёром и переходит на его персональную страницу.
        """
        self.driver.find_element(By.CSS_SELECTOR, 'input.styles_input__WCRXt.kinopoisk-header-search-form-input__input').send_keys('Фрунзик')
        self.driver.find_element(By.CSS_SELECTOR, 'svg.styles_icon__a6f9D.search-form-submit-button__icon').click()
        self.driver.find_element(By.XPATH, "//*[text() = 'Фрунзик Мкртчян']").click()

    @allure.step("Ввести некорректный запрос в поле поиска")
    def uncorrect_request(self):
        """
        Метод uncorrect_request вызывается из теста test_ui.py/test_uncorrect_request,
        метод вводит в поле поиска некорректный запрос, состоящий из букв, цифр и спецсимволов, нажимает кнопку поиска.
        """
        self.driver.find_element(By.CSS_SELECTOR, 'input.styles_input__WCRXt.kinopoisk-header-search-form-input__input').send_keys('%#*@^4g901j46;$%')
        self.driver.find_element(By.CSS_SELECTOR, 'svg.styles_icon__a6f9D.search-form-submit-button__icon').click()
