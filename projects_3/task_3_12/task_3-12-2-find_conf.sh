#!/bin/bash
echo "Поиск .conf файлов в /etc (регистронезависимо)"
ls -l /etc | grep -i "\.conf"
