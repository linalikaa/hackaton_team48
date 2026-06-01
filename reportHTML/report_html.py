import os

class ReportHTML:
    def __init__(self, stats, output_folder):
        self.stats = stats
        self.output_folder = output_folder

    def generate(self):
        total = sum(self.stats.values())

        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Отчёт о сортировке почты</title>
    <style>
        body {{
            font-family: Arial;
            background: #ffe4ec;
            padding: 30px;
        }}
        h1 {{
            color: #d63384;
            text-align: center;
        }}
        h3 {{
            text-align: center;
            color: #c2185b;
        }}
        .total {{
            background: #f8bbd0;
            padding: 15px;
            border-radius: 20px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin: 20px 0;
        }}
        .category {{
            background: white;
            padding: 12px;
            margin: 10px 0;
            border-radius: 15px;
            border-left: 10px solid #ec407a;
        }}
        .category-name {{
            font-weight: bold;
            color: #c2185b;
        }}
        .category-count {{
            float: right;
            font-size: 20px;
            font-weight: bold;
            color: #d63384;
        }}
        .footer {{
            text-align: center;
            font-style: italic;
            margin-top: 30px;
            color: #d63384;
        }}
    </style>
</head>
<body>
    <h1>Отчёт о сортировке почты</h1>
    <h3>Личная страничка с наглядным представлением статистики Вашей почты</h3>

    <div class="total">
        Всего писем: {total}
    </div>
"""

        for category, count in self.stats.items():
            html += f"""
    <div class="category">
        <span class="category-name">{category}</span>
        <span class="category-count">{count}</span>
    </div>
"""

        html += f"""
    <div class="footer">
        Над проектом работали: Погребная Анна, Никулова Анастасия, Сяглова Анна
    </div>
</body>
</html>"""

        output_path = os.path.join(self.output_folder, "report.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"Отчёт создан: {output_path}")