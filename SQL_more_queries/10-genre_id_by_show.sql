-- Script that list all shows contained in a database.
SELECT DISTINCT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
