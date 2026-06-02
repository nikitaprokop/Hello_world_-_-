#!/bin/bash
cat > settings.php << 'PHP'
<?php
return [
'db_host' => 'localhost',
'db_name' => 'app_db',
'db_user' => 'app_user',
'db_pass' => 'secret',
// Путь к каталогу данных MySQL
'db_data_path' => '/var/lib/mysql/data',
// Дополнительные настройки
'log_path' => '/var/log/app.log'
];
PHP
echo "Исходный файл settings.php"
cat settings.php
sed -i 's|/var/lib/mysql/data|/mnt/ssd/mysql|g' settings.php
echo -e "\nФайл после замены"
cat settings.php
