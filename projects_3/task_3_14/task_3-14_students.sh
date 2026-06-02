#!/bin/bash
cat > students.txt << 'DATA'
Ivan 78
Maria 92
Oleg 67
Anna 85
DATA
echo "Содержимое students.txt"
cat students.txt
echo -e "\nТолько имена"
awk '{print $1}' students.txt
echo -e "\nТолько оценки"
awk '{print $2}' students.txt
echo -e "\nНомер строки и имя"
awk '{print NR, $1}' students.txt
