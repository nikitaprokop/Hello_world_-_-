import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams['font.family'] = 'DejaVu Sans'


conn = psycopg2.connect(
    host="localhost",
    port="5435",
    user="postgres",
    password="student",
    database="student_task"
)


df_category = pd.read_sql("""
    SELECT
        p.category,
        COUNT(DISTINCT p.id) AS product_count,
        ROUND(AVG(pr.price)::numeric, 2) AS avg_price,
        ROUND(MIN(pr.price)::numeric, 2) AS min_price,
        ROUND(MAX(pr.price)::numeric, 2) AS max_price
    FROM products p
    JOIN prices pr ON p.id = pr.product_id
    GROUP BY p.category
    ORDER BY avg_price DESC
""", conn)


df_products = pd.read_sql("""
    SELECT
        p.name AS product_name,
        p.category,
        COUNT(pr.price) AS price_count,
        ROUND(AVG(pr.price)::numeric, 2) AS avg_price,
        ROUND(MIN(pr.price)::numeric, 2) AS min_price,
        ROUND(MAX(pr.price)::numeric, 2) AS max_price,
        ROUND(STDDEV(pr.price)::numeric, 2) AS price_std
    FROM products p
    JOIN prices pr ON p.id = pr.product_id
    GROUP BY p.id, p.name, p.category
    ORDER BY avg_price DESC
    LIMIT 10
""", conn)


df_all_prices = pd.read_sql("""
    SELECT pr.price, p.category
    FROM prices pr
    JOIN products p ON p.id = pr.product_id
""", conn)

conn.close()


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Анализ цен товаров", fontsize=16, fontweight="bold")


categories = df_category["category"]
avg_prices = df_category["avg_price"]

bars1 = ax1.bar(categories, avg_prices, color="#4a90d9", edgecolor="white", width=0.6)
for bar, val in zip(bars1, avg_prices):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f"{val:.2f}", ha="center", fontsize=9)
ax1.set_ylabel("Средняя цена (руб.)")
ax1.set_title("Средняя цена по категориям", fontweight="bold")
ax1.set_xticklabels(categories, rotation=15, ha="right", fontsize=9)


product_names = df_products["product_name"]
avg_prices_prod = df_products["avg_price"]

bars2 = ax2.barh(product_names, avg_prices_prod, color="#2ecc71", edgecolor="white")
for bar, val in zip(bars2, avg_prices_prod):
    ax2.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
             f"{val:.2f} руб.", va="center", fontsize=8)
ax2.set_xlabel("Средняя цена (руб.)")
ax2.set_title("Топ-10 товаров по средней цене", fontweight="bold")
ax2.tick_params(axis='y', labelsize=8)


# График 3: Распределение цен (гистограмма)
all_prices = df_all_prices["price"]
ax3.hist(all_prices, bins=15, color="#7b68ee", edgecolor="white", alpha=0.7)
ax3.axvline(all_prices.mean(), color="crimson", linestyle="--",
            linewidth=1.5, label=f"Среднее: {all_prices.mean():.2f}")
ax3.axvline(all_prices.median(), color="orange", linestyle="--",
            linewidth=1.5, label=f"Медиана: {all_prices.median():.2f}")
ax3.set_xlabel("Цена (руб.)")
ax3.set_ylabel("Количество товаров")
ax3.set_title("Распределение цен", fontweight="bold")
ax3.legend(fontsize=8)


category_stats = df_category[["category", "product_count", "avg_price", "min_price", "max_price"]]
category_stats.columns = ["Категория", "Товаров", "Ср. цена", "Мин.", "Макс."]

ax4.axis("tight")
ax4.axis("off")
table = ax4.table(cellText=category_stats.values,
                  colLabels=category_stats.columns,
                  cellLoc="center",
                  loc="center",
                  colWidths=[0.2, 0.15, 0.15, 0.12, 0.12])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.5)
ax4.set_title("Сводная статистика по категориям", fontweight="bold", y=0.98)

plt.tight_layout()
plt.savefig("price_analysis_report.png", dpi=150, bbox_inches="tight")
plt.show()


print("\n=== ДОПОЛНИТЕЛЬНАЯ СТАТИСТИКА ===\n")
print(f"Всего товаров: {df_products['product_name'].nunique()}")
print(f"Всего категорий: {df_category['category'].nunique()}")
print(f"Всего ценовых записей: {len(df_all_prices)}")
print(f"\nОбщая статистика по ценам:")
print(f"  Среднее: {all_prices.mean():.2f} руб.")
print(f"  Медиана: {all_prices.median():.2f} руб.")
print(f"  Стандартное отклонение: {all_prices.std():.2f} руб.")
print(f"  Минимум: {all_prices.min():.2f} руб.")
print(f"  Максимум: {all_prices.max():.2f} руб.")