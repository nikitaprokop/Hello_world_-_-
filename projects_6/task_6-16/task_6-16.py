import psycopg2
import pandas as pd


try:
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres",
        password="student",
        database="student_task"
    )
    print("✓ Подключение установлено\n")
except Exception as error:
    print(f"Ошибка подключения: {error}")
    raise SystemExit


# ИСПРАВЛЕНО: p.product_id -> p.id
query = """
SELECT
    p.name AS product_name,
    p.category,
    pr.price
FROM prices pr
JOIN products p ON pr.product_id = p.id
"""

df = pd.read_sql(query, connection)
connection.close()

print("✓ Данные загружены\n")
print(df.head())


mean_price = df['price'].mean()
median_price = df['price'].median()
std_price = df['price'].std()
min_price = df['price'].min()
max_price = df['price'].max()

print("\n=== Статистика по ценам ===")
print(f"Среднее:      {mean_price:,.2f} руб.")
print(f"Медиана:      {median_price:,.2f} руб.")
print(f"Ст. отклонение:{std_price:,.2f} руб.")
print(f"Минимум:      {min_price:,.2f} руб.")
print(f"Максимум:     {max_price:,.2f} руб.")


Q1 = df['price'].quantile(0.25)
Q2 = df['price'].quantile(0.50)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1

print(f"\n=== Квартили ===")
print(f"Q1 (25%): {Q1:,.2f} руб.")
print(f"Q2 (50%): {Q2:,.2f} руб.")
print(f"Q3 (75%): {Q3:,.2f} руб.")
print(f"IQR:      {IQR:,.2f} руб.")


above_q3 = df[df['price'] > Q3][['product_name', 'category', 'price']]
print("\n=== Товары дороже Q3 ===")
print(above_q3.to_string(index=False))


category_stats = df.groupby('category')['price'].agg(
    count='count',
    mean='mean',
    median='median',
    std='std'
).round(2).sort_values('mean', ascending=False)

print("\n=== Статистика по категориям ===")
print(category_stats.to_string())


price_range = df.groupby('product_name')['price'].agg(
    min_price='min',
    max_price='max'
)
price_range['range'] = price_range['max_price'] - price_range['min_price']
top5_range = price_range.sort_values('range', ascending=False).head(5)

print("\n=== Топ-5 товаров с наибольшим разбросом цен ===")
print(top5_range.to_string())