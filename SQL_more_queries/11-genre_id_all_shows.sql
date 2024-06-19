-- Script that list all shows contained in a databse.
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.shows_id
ORDER BY tv_shows.title, tv_shows_genres.genre_id;
