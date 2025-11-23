-- 103-rating_genres.sql
-- List all genres by rating sum
SELECT g.name, SUM(r.rating) AS rating
FROM tv_genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
JOIN tv_shows s ON sg.tv_show_id = s.id
JOIN tv_ratings r ON s.id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
