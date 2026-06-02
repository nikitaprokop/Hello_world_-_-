#!/bin/bash
cat > data.csv << 'DATA'
1,Mouse,23
2,Keyboard,15
3,Monitor,120
4,USB,5
DATA
echo "Содержимое data.csv"
cat data.csv
echo -e "\nНазвания товаров"
awk -F ',' '{print $2}' data.csv
echo -e "\nТовары дороже 20"
awk -F ',' '$3 > 20 {print $2, $3}' data.csv
echo -e "\nОбщая стоимость всех товаров"
total=$(awk -F ',' '{sum += $3} END {print sum}' data.csv)
echo "Общая стоимость: $total"
