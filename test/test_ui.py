import pytest
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from UIPage import MovieSearch
from config import ticket_url, media_url


driver = webdriver.Chrome()


@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Портал Kinopoisk.ru")
@allure.story("Автоматизированное UI-тестирование портала Kinopoisk.ru")
@allure.feature("Пользовательские сценарии взаимодействия с интерфейсом")
@allure.title("Выполнение стандартных действий")
@allure.description("Нажатие кнопок, переход на страницы")
@pytest.mark.ui
def test_search_movie():
    film = MovieSearch(driver)
    with allure.step("Найти в поиске фильм по названию"):
        film.search_film_by_name()
        with allure.step("Перейти на страницу фильма, для просмотра"):
            film.open_film()
            with allure.step("Проверить, что метод вернул правильный title фильма"):
                assert driver.title('Мимино') in film.open_film()


@pytest.mark.ui
def test_by_ticket():
    ticket = MovieSearch(driver)
    with allure.step("Купить билет в кино"):
        current_url = ticket.by_ticket()
        with allure.step("Проверить, что совершён переход на страницу с ожидаемым URL"):
            expected_url = ticket_url
            assert current_url == expected_url, f'Expected URL: {expected_url}, but got: {current_url}'


@pytest.mark.ui
def test_media_page():
    media = MovieSearch(driver)
    with allure.step("Перейти с главной страницы на страницу с медиа-материалами"):
        current_url = media.media_page()
        with allure.step("Проверить, что совершён переход на страницу с ожидаемым URL"):
            expected_url = media_url
            assert current_url == expected_url, f'Expected URL: {expected_url}, but got: {current_url}'


@pytest.mark.ui
def test_search_actor():
    actor = MovieSearch(driver)
    with allure.step("Найти актёра по имени"):
        actor.search_actor_by_name()
        with allure.step("Проверить, что совершён переход на страницу с ожидаемым текстом"):
            assertion = driver.find_element(By.CSS_SELECTOR, '.film-page-section-title.styles_rootTitle__2rava.styles_title__hon80.styles_rootMd__bQlVg.styles_root__pftHi.styles_rootDark__XwGcT')
            text = assertion.text
            assert text == 'О персоне', f'Expected text: "О персоне", but got: "{text}"'


@pytest.mark.ui
def test_uncorrect_request():
    uncorrect = MovieSearch(driver)
    with allure.step("Запустить поиск по некорректным данным"):
        uncorrect.uncorrect_request()
        with allure.step("Проверить, что по запросу ничего не найдено"):
            unassertion = driver.find_element(By.CSS_SELECTOR, '[height="75"]')
            text = unassertion.text
            assert text == 'К сожалению, по вашему запросу ничего не найдено...', f'Expected text: "К сожалению, по вашему запросу ничего не найдено...", but got: "{text}"'
