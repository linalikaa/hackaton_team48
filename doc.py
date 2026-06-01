from classifier import EmailClassifier
from reportHTML.report_html import ReportHTML
import os
import sys
import shutil

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
INBOX_FOLDER = os.path.join(PROJECT_FOLDER, "inbox")
RESULTS_FOLDER = os.path.join(PROJECT_FOLDER, "results")

if not os.path.exists(INBOX_FOLDER):
    print(f"Ошибка: папка 'inbox' не найдена по пути {INBOX_FOLDER}")
    sys.exit(1)

os.makedirs(RESULTS_FOLDER, exist_ok=True)

files = os.listdir(INBOX_FOLDER)

total_stats = {
    "Запросы на предоставление доступа": 0,
    "Сообщения о внештатных ситуациях": 0,
    "Вопросы по поводу оборудования": 0,
    "Спам": 0,
    "Кадровые вопросы": 0,
    "Информационные сообщения": 0,
    "Черновик": 0,
    "Прочее": 0
}

for filename in files:
    if filename.endswith(".txt"):
        file_path = os.path.join(INBOX_FOLDER, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
        except UnicodeDecodeError:
            with open(file_path, "r", encoding="cp1251") as file:
                text = file.read()

        category = EmailClassifier(text).classify()
        total_stats[category] += 1

        category_folder = os.path.join(RESULTS_FOLDER, category)
        os.makedirs(category_folder, exist_ok=True)
        shutil.copy2(file_path, os.path.join(category_folder, filename))

        print(f"Название письма:'{filename}' и его категория: '{category}'")

print("Статистика:")
for category, count in total_stats.items():
    print(f"{category}: {count}")
print("Всего обработано писем:", sum(total_stats.values()))

reporter = ReportHTML(total_stats, RESULTS_FOLDER)
reporter.generate()