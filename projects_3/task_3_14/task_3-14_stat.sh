#!/bin/bash
awk '{sum+=$2} END {print "Сумма:", sum}' students.txt
awk '{sum+=$2} END {print "Среднее:", sum/NR}' students.txt
awk 'NR==1{max=$2} $2>max{max=$2} END {print "Максимум:", max}' students.txt

