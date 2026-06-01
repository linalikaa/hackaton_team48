@echo off
echo Запуск системы классификации писем

if not exist "doc.py" (
    echo Ошибка - файл doc.py не найден
    pause
    exit /b 1
)

if not exist "inbox" (
    echo Ошибка - папка inbox не найдена
    pause
    exit /b 1
)

if not exist "results" mkdir results

python doc.py 2>&1 | tee results\run.log

echo.
echo Письма разложены по папкам
echo Лог сохранён в: results\run.log
echo.
pause