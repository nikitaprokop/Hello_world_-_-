#!/bin/bash
read -p "Введите вашу массу (кг): " weight
read -p "Введите ваш рост (метры, например 1.75): " height
bmi=$(echo "scale=0; $weight / ($height * $height)" | bc)
echo "Ваш индекс массы тела (ИМТ): $bmi"
