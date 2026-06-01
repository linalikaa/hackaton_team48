from email_processor import EmailProcessor
from reportHTML.report_html import ReportHTML
import os

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
INBOX_FOLDER = os.path.join(PROJECT_FOLDER, "inbox")
RESULTS_FOLDER = os.path.join(PROJECT_FOLDER, "results")

processor = EmailProcessor(INBOX_FOLDER, RESULTS_FOLDER)
stats = processor.process()

print("Статистика:")
for category, count in stats.items():
    print(f"{category}: {count}")
print("Всего обработано писем:", sum(stats.values()))

reporter = ReportHTML(stats, RESULTS_FOLDER)
reporter.generate()