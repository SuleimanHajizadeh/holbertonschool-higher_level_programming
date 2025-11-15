-- 101-avg_temperatures.sql
USE hbtn_0c_0;

SELECT city, ROUND(AVG(temp), 4) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
