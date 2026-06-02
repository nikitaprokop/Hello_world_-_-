#!/bin/bash
 read -p "Введите имя файла отчёта: " report_file
 if [ -f "$report_file" ]; then
 echo "Файл '$report_file' найден."
 if [ -s "$report_file" ]; then
echo "   Файл содержит данные."
if grep -qi "error" "$report_file"; then
echo "ВНИМАНИЕ: В файле ошибки!"
error_count=$(grep -ci "error" "$report_file")
 echo "   Количество строк с ошибками: $error_count"
else
 echo "Ошибок не обнаружено."
fi
 else
echo "Файл '$report_file' пуст."
 fi
 else
 echo "Ошибка: Файл '$report_file' не существует."
exit 1
fi
echo "Анализ завершён."
