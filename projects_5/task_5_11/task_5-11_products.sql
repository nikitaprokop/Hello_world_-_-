
SELECT *
FROM products
WHERE category = 'Электроника';


SELECT *
FROM products
WHERE category = 'Аксессуары'
  AND name LIKE '%женские%';


SELECT *
FROM products
WHERE category = 'Книги';


SELECT *
FROM products
WHERE category != 'Бытовая техника';


SELECT *
FROM products
WHERE category IN ('Электроника', 'Аксессуары', 'Книги');


SELECT *
FROM products
WHERE (category = 'Электроника' AND name LIKE '%Samsung%')
   OR category = 'Бытовая техника';


SELECT *
FROM products
WHERE (
    category IN ('Электроника', 'Аксессуары', 'Бытовая техника')
    AND product_id BETWEEN 1 AND 15
    AND name NOT LIKE '%Samsung%'
  )
  OR category = 'Книги';