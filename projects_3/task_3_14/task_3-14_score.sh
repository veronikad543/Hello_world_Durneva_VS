#!/bin/bash

echo "Выше 80:"
awk '$2 > 80' students.txt

echo "Ниже 70:"
awk '$2 < 70' students.txt

echo "Первая строка:"
head -1 students.txt

