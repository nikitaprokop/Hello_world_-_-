#!/bin/bash
echo "Создание файлов"
for i in {1..10}; do
touch "test$i.txt"
echo "Создан файл: test$i.txt"
done
echo -e "\nСписок созданных файлов"
ls test*.txt 2>/dev/null
echo -e "\nУдаление файлов в обратном порядке"
counter=10
while [ $counter -ge 1 ]; do
 rm "test$counter.txt"
echo "Удалён файл: test$counter.txt"
 counter=$((counter - 1))
done
echo -e "\nПроверка: файлы удалены"
ls test*.txt 2>/dev/null || echo "Файлов test*.txt не найдено."
echo -e "\nЦикл завершён."
