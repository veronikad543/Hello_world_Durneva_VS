#!/bin/bash
cut -d',' -f2 data.csv
awk -F',' '$3 > 20' data.csv
awk -F',' '{sum+=$3} END {print sum}' data.csv

