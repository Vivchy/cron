# Запуск скрипта python при помощи cron

#### создание планировщика 

<pre> crontab -e </pre>

Добавить в файл

<pre> * * * * * cd /home/user/cron && /home/user/cron/venv/bin/python3 main.py </pre>

Проверка работы

<pre>tail /var/log/syslog </pre>
