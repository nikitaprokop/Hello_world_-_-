#!/bin/bash
echo "Поиск пользователя $USER в /etc/passwd"
grep "^$USER:" /etc/passwd
