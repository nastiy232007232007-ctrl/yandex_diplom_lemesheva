# Работа с базой данных

## Задание 1
### Список курьеров с количеством заказов в доставке


SELECT c.login,
       COUNT(o.id) AS active_deliveries
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login
ORDER BY active_deliveries DESC;


## Задание 2  
### Статусы заказов по трекерам


SELECT track,
       CASE 
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN "inDelivery" = true THEN 1
           ELSE 0
       END AS status
FROM "Orders";
