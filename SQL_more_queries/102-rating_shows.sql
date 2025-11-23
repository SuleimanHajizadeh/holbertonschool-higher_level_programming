-- 102-rating_shows.sql
-- List all shows by rating sum
SELECT tv_shows.title, SUM(tv_ratings.rating) AS rating
FROM tv_shows
LEFT JOIN tv_ratings ON tv_shows.id = tv_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
