#!/bin/bash
echo "Имена:"
cut -d' ' -f1 students.txt

echo "Оценки:"
cut -d' ' -f2 students.txt

echo "Номер и имя:"
nl students.txt | cut -f1,2
