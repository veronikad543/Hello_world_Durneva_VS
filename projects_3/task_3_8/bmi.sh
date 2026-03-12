#!/bin/bash

echo "Введите вашу массу (кг):"
read weight

echo "Введите ваш рост (в метрах, например 1.75):"
read height

bmi=$(echo "$weight / ($height * $height)")

bmi_int=$(printf "%.0f" $bmi)

echo "Ваш индекс массы тела (BMI): $bmi_int"
