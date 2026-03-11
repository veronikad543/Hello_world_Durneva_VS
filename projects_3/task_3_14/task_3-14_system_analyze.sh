#!/bin/bash
df -h | awk 'NR>1 {print $1, $5}'
echo "Предупреждение:"
df -h | awk 'NR>1 && $5+0 > 90 {print $1, $5}'
