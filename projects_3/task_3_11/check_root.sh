#!/bin/bash
check_root() {
if [ "$EUID" -eq 0 ]; then
echo "Скрипт запущен от суперпользователя (root)."
return 0
 else
echo "ПРЕДУПРЕЖДЕНИЕ: Скрипт НЕ запущен от root"
 echo "   Текущий EUID = $EUID (требуется 0)"
echo "   Запустите скрипт с помощью: sudo ./check_root.sh"
exit 1
fi
}
echo "Проверка прав доступа"
check_root
echo "Продолжение выполнения скрипта"
