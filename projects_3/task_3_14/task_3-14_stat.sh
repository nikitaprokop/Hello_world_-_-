#!/bin/bash
if [ ! -f "students.txt" ]; then
echo "Ошибка: students.txt не найден. Сначала запустите task_3-14_students.sh"
exit 1
fi
echo "Анализ оценок студентов"
sum=$(awk '{sum += $2} END {print sum}' students.txt)
echo "Сумма оценок: $sum"
count=$(wc -l < students.txt)
echo "Количество студентов: $count"
avg=$(awk '{sum += $2} END {printf "%.2f", sum/NR}' students.txt)
echo "Средняя оценка: $avg"
max=$(awk 'NR==1 {max=$2} $2>max {max=$2} END {print max}' students.txt)
echo "Максимальная оценка: $max"
