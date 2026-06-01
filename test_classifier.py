import pytest
from classifier import EmailClassifier

class TestEmailClassifier(EmailClassifier):
    def is_draft(self):
        return False

def get_category(text):
    return TestEmailClassifier(text).classify()

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
    assert get_category("Ошибка при работе") == "Сообщения о внештатных ситуациях"
def test_incident_word_work():
    assert get_category("Система не работает") == "Сообщения о внештатных ситуациях"
def test_incident_word_starts():
    assert get_category("Программа не запускается") == "Сообщения о внештатных ситуациях"
def test_incident_word_open():
    assert get_category("Тз не открывается") == "Сообщения о внештатных ситуациях"
def test_incident_word_freezes():
    assert get_category("Прога зависает постоянно") == "Сообщения о внештатных ситуациях"
def test_incident_uppercase():
    assert get_category("СИСТЕМА НЕ РАБОТАЕТ") == "Сообщения о внештатных ситуациях"


def test_incident_word_notebook():
    assert get_category("ноутбук неисправен") == "Вопросы по поводу оборудования"
def test_incident_word_headset():
    assert get_category("гарнитура вышла из строя") == "Вопросы по поводу оборудования"
def test_incident_word_scanner():
    assert get_category("сканер плохо работает") == "Вопросы по поводу оборудования"
def test_equipment_uppercase():
    assert get_category("СКАНЕР ПЛОХО РАБОТАЕТ") == "Вопросы по поводу оборудования"



def test_spam_word_win():
    assert get_category("Вы выиграли автомобиль") == "Спам"
def test_spam_word_winner():
    assert get_category("Вы победитель розыгрыша") == "Спам"
def test_spam_word_discount():
    assert get_category("Скидка 90%") == "Спам"
def test_spam_word_confirm():
    assert get_category("Подтвердите личность для выигрыша") == "Спам"
def test_spam_word_prize():
    assert get_category("Ваш приз уже ждет") == "Спам"
def test_spam_word_card():
    assert get_category("Введите номер банковской карты") == "Спам"
def test_spam_uppercase():
    assert get_category("ВЫ ВЫИГРАЛИ ПРИЗ") == "Спам"

def test_hr_word_vacation():
    assert get_category("Хочу согласовать отпуск") == "Кадровые вопросы"
def test_hr_word_sick():
    assert get_category("Я открыла больничный") == "Кадровые вопросы"
def test_hr_word_registration():
    assert get_category("Занимаюсь оформлением документов") == "Кадровые вопросы"
def test_hr_word_new_employee():
    assert get_category("Скоро появится новый сотрудник") == "Кадровые вопросы"
def test_hr_word_start_work():
    assert get_category("Здраствуйте!Когда произойдет выход на работу") == "Кадровые вопросы"
def test_hr_word_hr_department():
    assert get_category("Обратитесь в отдел кадров") == "Кадровые вопросы"
def test_hr_word_disability():
    assert get_category("Справка о нетрудоспособности") == "Кадровые вопросы"
def test_hr_word_schedule():
    assert get_category("Пришлите график работы") == "Кадровые вопросы"
def test_hr_word_employee_starts():
    assert get_category("Сотрудник приступает к работе 13.01") == "Кадровые вопросы"
def test_hr_word_uppercase():
    assert get_category("ОТПУСК СОГЛАСОВАН") == "Кадровые вопросы"

def test_info_word_digest():
    assert get_category("Отправляем дайджест") == "Информационные сообщения"
def test_info_word_monitoring():
    assert get_category("Результаты мониторинга") == "Информационные сообщения"
def test_info_word_report():
    assert get_category("Отчёт за май") == "Информационные сообщения"
def test_info_word_invitation():
    assert get_category("Приглашение на конференцию") == "Информационные сообщения"
def test_info_word_demo():
    assert get_category("Нужно сделать демо") == "Информационные сообщения"
def test_info_word_call():
    assert get_category("Созвон в 15:00") == "Информационные сообщения"
def test_info_word_maintenance():
    assert get_category("Технические работы запланированы на 14.05") == "Информационные сообщения"
def test_info_word_uppercase():
    assert get_category("ДАЙДЖЕСТ ЗА НЕДЕЛЮ") == "Информационные сообщения"

def test_other_empty_string():
    assert get_category("") == "Прочее"
def test_other_only_spaces():
    assert get_category("    ") == "Прочее"
def test_other_random_text():
    assert get_category("Привет, как дела?") == "Прочее"
def test_other_only_digits():
    assert get_category("12345") == "Прочее"
def test_other_only_punctuation():
    assert get_category("...") == "Прочее"
def test_other_latin_text():
    assert get_category("hello, how are you?") == "Прочее"


def test_keyword_at_start_of_text():
    assert get_category("пароль — забыл, помогите") == "Запросы на предоставление доступа"
def test_keyword_at_end_of_text():
    assert get_category("помогите восстановить пароль") == "Запросы на предоставление доступа"
def test_keyword_is_entire_text():
    assert get_category("пароль") == "Запросы на предоставление доступа"
def test_very_long_text_with_keyword_at_end():
    long_text = "яблоко " * 300 + "принтер сломался"
    assert get_category(long_text) == "Вопросы по поводу оборудования"
def test_very_long_text_without_keywords():
    long_text = "яблоко " * 500
    assert get_category(long_text) == "Прочее"
def test_result_is_always_deterministic():
    text = "принтер не работает"
    assert get_category(text) == get_category(text)
def test_two_keywords_from_different_categories():
    text = "ошибка при печати на принтере"
    result1 = get_category(text)
    result2 = get_category(text)
    assert result1 == result2
    assert result1 in ("Сообщения о внештатных ситуациях", "Вопросы по поводу оборудования")
def test_keyword_with_punctuation_around_it():
    assert get_category("(пароль)") == "Запросы на предоставление доступа"
def test_keyword_with_newline():
    assert get_category("\nпароль\n") == "Запросы на предоставление доступа"
def test_result_is_string():
    assert isinstance(get_category("любой текст"), str)
def test_result_is_not_empty_string():
    assert get_category("любой текст") != ""

emails = [
    (
        "Доброе утро! Нужно выдать стажеру права на чтение к базе данных",
        "Запросы на предоставление доступа"
    ),
    (
        "Срочно! Не открывается CRM, клиенты не видны",
        "Сообщения о внештатных ситуациях"
    ),
    (
        "ПОЗДРАВЛЯЕМ! Ваш приз уже ждёт. Перейдите по ссылке!",
        "Спам"
    ),
    (
        "Прошу согласовать отпуск с 15 по 30 июля",
        "Кадровые вопросы"
    ),
    (
        "Готов итоговый отчёт по проекту за первый квартал",
        "Информационные сообщения"
    ),
    (
        "Сырки привезли",
        "Прочее"
    ),
    (
        "   ",
        "Прочее"
    ),
]
@pytest.mark.parametrize("text, expected", emails)
def test_realistic_email(text, expected):
    assert get_category(text) ==expected





