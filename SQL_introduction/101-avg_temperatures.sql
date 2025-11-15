-- 101-avg_temperatures.sql
-- Şəhərlər üzrə orta temperatur (Fahrenheit) hesablanır və azalan sıraya görə göstərilir

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
