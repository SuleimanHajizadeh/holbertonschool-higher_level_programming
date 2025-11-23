-- 102-rating_shows.sql
-- List all shows by rating sum
SELECT tv_shows.title, SUM(tv_shows_rating.rating) AS rating
FROM tv_shows
LEFT JOIN tv_shows_rating ON tv_shows.id = tv_shows_rating.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
