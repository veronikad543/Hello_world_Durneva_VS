#!/bin/bash

USER=$USER

echo "Ищем пользователя: $USER в файле /etc/passwd"
grep "^$USER:" /etc/passwd

if [ $? -eq 0 ]; then
    echo "Пользователь $USER найден!"
else
    echo "Пользователь $USER не найден в системе"
fi
