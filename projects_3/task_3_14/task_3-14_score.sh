#!/bin/bash
if [ ! -f "students.txt" ]; then
echo "Ошибка: students.txt не найден. Сначала запустите task_3-14_students.sh"
exit 1
fi
echo "Студенты с оценкой ВЫШЕ 80"
awk '$2 > 80 {print $1, $2}' students.txt
echo -e "\nСтуденты с оценкой НИЖЕ 70"
awk '$2 < 70 {print $1, $2}' students.txt
echo -e "\nТолько первая строка файла"
awk 'NR == 1 {print $0}' students.txt
