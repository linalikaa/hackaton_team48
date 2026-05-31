
echo "Запуск системы классификации писем"
if ! command -v python3 &> /dev/null; then
    echo "Ошибка - Python3 не найден, установите Python3 и попробуйте снова."
    exit 1
fi
if [ ! -f "doc.py" ]; then
    echo "Ошибка - файл doc.py не найден, проверьте, что вы запускаете скрипт из папки проекта."
    exit 1
fi
if [ ! -d "inbox" ]; then
    echo "Ошибка - папка inbox не найдена, создайте папку inbox и положите туда .txt файлы с письмами"
    exit 1
fi
if [ -z "$(ls -A inbox/)" ]; then
    echo "Ошибка - папка inbox пустая, положите туда .txt файлы с письмами."
    exit 1
fi
if [ ! -d "results" ]; then
    mkdir results
fi
COUNT=$(ls inbox/*.txt 2>/dev/null | wc -l)
echo "Найдено писем для обработки: $COUNT"

echo "Запускаем классификатор"
echo "----------------------------------------"
python3 doc.py 2>&1 | tee results/run.log
echo "----------------------------------------"

if [ $? -eq 0 ]; then
    echo ""
    echo "Письма разложены по папкам"
    echo "Лог сохранён в: results/run.log"
    echo ""
    echo "Результаты:"
    ls results/
else
    echo ""
    echo "Ошибка - что-то пошло не так при запуске doc.py"
    echo "Посмотрите лог: results/run.log"
    exit 1
fi
echo ""
echo "  Работа завершена успешно"

