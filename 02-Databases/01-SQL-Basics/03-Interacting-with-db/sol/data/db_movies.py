import sqlite3

conn = sqlite3.connect('movies.sqlite')
conn.row_factory = sqlite3.Row
c = conn.cursor()
# rename director_id column into directors
rename = '''
ALTER TABLE movies
RENAME COLUMN director_id TO directors;
'''
c.execute(rename)

# create a director_id column as INTEGER
add = '''
ALTER TABLE movies
ADD COLUMN director_id INTEGER;
'''
c.execute(add)
# copy the directors to director_id
fetch = '''
SELECT directors
FROM movies
ORDER BY 1 ASC;
'''
c.execute(fetch)
ids = c.fetchall()
paste = '''
UPDATE movies
SET director_id = ?
WHERE
    directors = ?
'''
for id in ids:
    id = id['directors']
    print(id)
    c.execute(paste, (int(id), id))
    conn.commit()
# delete the directors column
c.execute('''PRAGMA foreign_keys=off;''')
c.execute('''BEGIN TRANSACTION;''')
c.execute("""
CREATE TABLE IF NOT EXISTS films (
    title TEXT,
    rating TEXT,
    vote_count INTEGER,
    start_year INTEGER,
    minutes INTEGER,
    genres TEXT,
    imdb_id TEXT,
    id INTEGER PRIMARY KEY,
    director_id INTEGER
);
""")
c.execute("""
INSERT INTO films(title, rating, vote_count, start_year, minutes, genres, imdb_id, id, director_id)
SELECT title, rating, vote_count, start_year, minutes, genres, imdb_id, id, director_id
FROM movies;
""")
c.execute('DROP TABLE movies;')
c.execute('ALTER TABLE films RENAME TO movies;')
c.execute('COMMIT;')
c.execute('PRAGMA foreign_keys=on;')
conn.commit()
c.close()
