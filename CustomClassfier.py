class CustomClassifier:
    def __init__(self, text: str):
        self.text = text.lower()
        self.custom_categories = {}

    def add_category(self, category_name: str, keywords: list):
        self.custom_categories[category_name] = keywords

    def build(self):
        print("Создание своих категорий")
        print("Введите пустую строку когда закончите\n")

        while True:
            category_name = input("Название категории (введите Enter для завершения): ").strip()
            if category_name == "":
                break

            keywords_input = input(f"Введите ключевые слова для '{category_name}' через запятую: ").strip()
            keywords = [word.strip().lower() for word in keywords_input.split(",") if word.strip() != ""]

            if len(keywords) == 0:
                print("Нужно ввести хотя бы одно слово")
                continue

            self.add_category(category_name, keywords)
            print(f"Категория '{category_name}' добавлена!\n")

    def classify(self):
        for category, words in self.custom_categories.items():
            for word in words:
                if word in self.text:
                    return category
        return "Прочее"