import os
import shutil
from classifier import EmailClassifier


class EmailReader:
    def __init__(self, inbox_folder):
        self.inbox_folder = inbox_folder

    def get_emails(self):
        return [f for f in os.listdir(self.inbox_folder) if f.endswith(".txt")]


class EmailMover:
    def __init__(self, results_folder):
        self.results_folder = results_folder

    def move(self, file_path, category):
        category_folder = os.path.join(self.results_folder, category)
        os.makedirs(category_folder, exist_ok=True)
        shutil.copy2(file_path, os.path.join(category_folder, os.path.basename(file_path)))


class StatsCollector:
    def __init__(self, categories):
        self.stats = {cat: 0 for cat in categories}

    def increment(self, category):
        self.stats[category] = self.stats.get(category, 0) + 1

    def get_stats(self):
        return self.stats


class EmailProcessor:
    def __init__(self, inbox_folder, results_folder):
        self.reader = EmailReader(inbox_folder)
        self.mover = EmailMover(results_folder)
        self.stats = StatsCollector([
            "Запросы на предоставление доступа",
            "Сообщения о внештатных ситуациях",
            "Вопросы по поводу оборудования",
            "Спам",
            "Кадровые вопросы",
            "Информационные сообщения",
            "Черновик",
            "Прочее"
        ])
        self.classifier = EmailClassifier

    def process(self):
        for filename in self.reader.get_emails():
            file_path = os.path.join(self.reader.inbox_folder, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            category = self.classifier(text).classify()
            self.stats.increment(category)
            self.mover.move(file_path, category)
            print(f"{filename} -> {category}")
        return self.stats.get_stats()