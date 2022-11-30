-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_genres.name AS genre,
	COUNT(*) AS number_shows
FROM tv_show_genres
	INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_shows DESC;