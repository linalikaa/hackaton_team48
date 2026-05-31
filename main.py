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


