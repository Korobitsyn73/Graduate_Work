from KinopApi import MovieAPI
import pytest
import allure


@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Портал Kinopoisk.ru")
@allure.story("Автоматизированное API-тестирование портала Kinopoisk.ru")
@allure.feature("Проверка сценариев поиска")
@allure.title("Выполнение GET-запросов")
@allure.description("Поиск в бэкенде по имени и ID")
@pytest.mark.api
def test_get_film_from_name():
    api = MovieAPI()
    with allure.step("Найти фильм по названию"):
        response = api.search_movie(page=1, limit=1, query="Полосатый рейс")
        with allure.step("Проверить соответствие статус-кода ожидаемому"):

            assert response.status_code == 200

            if response.status_code == 200:
                print('Тест пройден: статус-код 200')
            else:
                print(f'Ошибка: статус-код {response.status_code}')

            json_data = response.json()
            print('Тело ответа:', json_data)


@pytest.mark.api
def test_get_film_from_ID():
    api = MovieAPI()
    with allure.step("Найти фильм по ID"):
        response = api.search_movie_from_ID(page=1, limit=1, query=785)
        with allure.step("Проверить соответствие статус-кода ожидаемому"):

            assert response.status_code == 200

            if response.status_code == 200:
                print('Тест пройден: статус-код 200')
            else:
                print(f'Ошибка: статус-код {response.status_code}')

            json_data = response.json()
            print('Тело ответа:', json_data)


@pytest.mark.api
def test_get_actor_from_name():
    api = MovieAPI()
    with allure.step("Найти актёра по имени"):
        response = api.search_actor_from_name(page=1, limit=1, query="Фрунзик")
        with allure.step("Проверить соответствие статус-кода ожидаемому"):

            assert response.status_code == 200

            if response.status_code == 200:
                print('Тест пройден: статус-код 200')
            else:
                print(f'Ошибка: статус-код {response.status_code}')

            json_data = response.json()
            print('Тело ответа:', json_data)


@pytest.mark.api
def test_get_film_uncorrect_ID():
    api = MovieAPI()
    with allure.step("Попытка поиска фильма по некорректному ID (негативный)"):
        response = api.uncorrect_ID_movie(page=1, limit=1, query=10)
        with allure.step("Проверить соответствие статус-кода ожидаемому"):
            assert response.status_code == 400

            if response.status_code == 400:
                print('Тест пройден: статус-код 400')
            else:
                print(f'Ошибка: статус-код {response.status_code}')

            json_data = response.json()
            print('Тело ответа:', json_data)


@pytest.mark.api
def test_get_without_token():
    api = MovieAPI()
    with allure.step("Попытка отправки GET-запроса на поиск фильма по ID, без токена (негативный)"):
        response = api.without_token(page=1, limit=1, query=457)
        with allure.step("Проверить соответствие статус-кода ожидаемому"):
            assert response.status_code == 401

            if response.status_code == 401:
                print('Тест пройден: статус-код 401')
            else:
                print(f'Ошибка: статус-код {response.status_code}')

            json_data = response.json()
            print('Тело ответа:', json_data)
