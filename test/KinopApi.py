import requests
import allure
from config import api_url, token


class MovieAPI:

    """
    Этот класс содержит методы, вызываемые тестовым набором test_api.py, для тестирования бэкенда портала Kinopoisk.ru.
    """

    def __init__(self):
        self.api_url = api_url
        self.headers = {'X-API-KEY': token}

    @allure.step("Отправить GET-запрос на поиск фильма по названию")
    def search_movie(self, query, page, limit):
        """
        Метод search_movie вызывается из теста test_api.py/test_get_film_from_name,
        метод отправляет GET-запрос с текстом. Получает статус-код и тело ответа в формате JSON.
        """
        req = 'v1.4/movie/search?page=1&limit=1&query="Полосатый рейс"'
        url = self.api_url + req
        response = requests.get(url, headers=self.headers)
        return response

    @allure.step("Отправить GET-запрос на поиск фильма по ID")
    def search_movie_from_ID(self, query, page, limit):
        """
        Метод search_movie_from_ID вызывается из теста test_api.py/test_get_film_from_ID,
        метод отправляет GET-запрос с определённым ID. Получает статус-код и тело ответа в формате JSON.
        """
        req = 'v1.4/movie/785'
        url = self.api_url + req
        response = requests.get(url, headers=self.headers)
        return response

    @allure.step("Отправить GET-запрос на поиск актёра по имени")
    def search_actor_from_name(self, query, page, limit):
        """
        Метод search_actor_from_name вызывается из теста test_api.py/test_get_actor_from_name,
        метод отправляет GET-запрос с текстом. Получает статус-код и тело ответа в формате JSON.
        """
        req = 'v1.4/person/search?page=1&limit=2&query=”Фрунзик”'
        url = self.api_url + req
        response = requests.get(url, headers=self.headers)
        return response

    @allure.step("Отправить GET-запрос на поиск фильма по некорректному ID (негативный)")
    def uncorrect_ID_movie(self, query, page, limit):
        """
        Метод uncorrect_ID_movie вызывается из теста test_api.py/test_get_film_uncorrect_ID,
        метод отправляет GET-запрос с некорректным ID. Получает статус-код и тело ответа в формате JSON.
        """
        req = 'v1.4/movie/10'
        url = self.api_url + req
        response = requests.get(url, headers=self.headers)
        return response

    @allure.step("Отправить GET-запрос на поиск фильма по ID, без токена (негативный)")
    def without_token(self, query, page, limit):
        """
        Метод without_token вызывается из теста test_api.py/test_get_without_token,
        метод отправляет GET-запрос с определённым ID, не содержащий токена авторизации. Получает статус-код и тело ответа в формате JSON.
        """
        req = 'v1.4/movie/457'
        url = self.api_url + req
        response = requests.get(url)
        return response
