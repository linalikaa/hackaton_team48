import pytest
from classifier import EmailClassifier

def get_category(text):
    return EmailClassifier(text).classify()

def test_access_word_access():
    assert get_category("Мне еще не выдан доступ к системе") == "Запросы на предоставление доступа"
def test_access_word_rights():
    assert get_category("Мне необходимы права администратора, чтобы выполнить задачу") == "Запросы на предоставление доступа"
def test_access_word_lgin():
    assert get_category("Не могу найти логин") == "Запросы на предоставление доступа"
def test_access_word_password():
    assert get_category("Нужно восстановить пароль") == "Запросы на предоставление доступа"
def test_access_uppercase():
    assert get_category("ПАРОЛЬ ПОТЕРЯН") == "Запросы на предоставление доступа"


def test_incident_word_error():
    assert get_category("Ошибка при входе") == "Сообщения о внештатных ситуациях"
def test_incident_word_work():
    assert get_category("Система не работает") == "Сообщения о внештатных ситуациях"
def test_incident_word_starts():
    assert get_category("Программа не запускается") == "Сообщения о внештатных ситуациях"
def test_incident_word_open():
    assert get_category("Тз не открывается") == "Сообщения о внештатных ситуациях"
def test_incident_word_cant():
    assert get_category("Я не могу войти") == "Сообщения о внештатных ситуациях"
def test_incident_word_unavailable():
    assert get_category("Сайт был недоступен вчера") == "Сообщения о внештатных ситуациях"
def test_incident_word_freezes():
    assert get_category("Прога зависает постоянно") == "Сообщения о внештатных ситуациях"
def test_incident_uppercase():
    assert get_category("СИСТЕМА НЕ РАБОТАЕТ") == "Сообщения о внештатных ситуациях"







