-- SCRIPT THAT DISPLAYS THE AVG TEMPERATURE FROM DIFFERENT CITIES
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
