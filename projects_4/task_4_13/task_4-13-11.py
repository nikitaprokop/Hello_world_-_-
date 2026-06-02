import psycopg2

try:
    # Подключение к твоей БД (порт и база могут отличаться)
    connection = psycopg2.connect(
        host="localhost",
        port="5430",          # твой порт из docker-compose
        user="postgres_db",
        password="student",
        database="student_task"
    )

    cursor = connection.cursor()

    # Пример SQL-запроса (можно заменить на любой)
    cursor.execute("SELECT name, price FROM products LIMIT 5;")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()

    print("\n✅ Запрос выполнен успешно")

except Exception as error:
    print(f"❌ Ошибка при подключении или выполнении запроса: {error}")