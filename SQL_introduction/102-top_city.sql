-- 102-top_city.sql
USE hbtn_0c_0;

SELECT city, ROUND(AVG(temp), 4) AS avg_temp
FROM temperatures
WHERE MONTH(CONVERT(date, DATE)) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
