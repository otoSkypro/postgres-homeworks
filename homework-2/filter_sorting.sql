-- Напишите запросы, которые выводят следующую информацию:
-- 1. заказы, доставленные в страны France, Germany, Spain (таблица orders, колонка ship_country)
SELECT ...

-- 2. уникальные страны и города, куда отправлялись заказы, отсортировать по странам и городам (таблица orders, колонки ship_country, ship_city)


-- 3. сколько дней в среднем уходит на доставку товара в Германию (таблица orders, колонки order_date, shipped_date, ship_country)


-- 4. минимальную и максимальную цену среди продуктов, не снятых с продажи (таблица products, колонки unit_price, discontinued не равно 1)


-- 5. минимальную и максимальную цену среди продуктов, не снятых с продажи и которых имеется не меньше 20 (таблица products, колонки unit_price, units_in_stock, discontinued не равно 1)

SELECT * FROM orders
WHERE ship_country IN ('France', 'Germany', 'Spain')

SELECT DISTINCT ship_country, ship_city FROM orders

SELECT AVG(shipped_date-order_date) FROM orders
WHERE ship_country = 'Germany'

SELECT MIN(unit_price), MAX(unit_price) FROM products
WHERE discontinued <> 1

SELECT MIN(unit_price), MAX(unit_price) FROM products
WHERE discontinued <> 1 AND units_in_stock > 20
