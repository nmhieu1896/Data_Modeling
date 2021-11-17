# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id INT,
        start_time BIGINT,
        user_id VARCHAR,
        level VARCHAR,
        song_id VARCHAR,
        artist_id VARCHAR,
        session_id INT,
        location TEXT,
        user_agent VARCHAR
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id VARCHAR,
        first_name VARCHAR(127),
        last_name VARCHAR(127),
        gender CHAR(1),
        level VARCHAR
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR,
        title VARCHAR(255),
        artist_id VARCHAR,
        year INT,
        duration FLOAT8
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR,
        name VARCHAR(255),
        location TEXT,
        latitude FLOAT8,
        longitude FLOAT8
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time BIGINT,
        hour INT CHECK (hour >= 0 AND hour <= 24),
        day INT CHECK (day >= 1 AND day <= 31),
        week INT CHECK (week >= 1 AND week <= 52),
        month INT CHECK (month >= 1 and month <= 12),
        year INT CHECK (year >= 1000 and year <= 10000),
        weekday INT CHECK (weekday >= 0 and weekday < 7)
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (
        songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users (
        user_id, first_name, last_name, gender, level
    )
    VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
    INSERT INTO songs (
        song_id, title, artist_id, year, duration
    )
    VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
    INSERT INTO artists (
        artist_id, name, location, latitude, longitude
    )
    VALUES (%s, %s, %s, %s, %s)
""")

time_table_insert = ("""
    INSERT INTO time (
        start_time, hour, day, week, month, year, weekday
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, a.artist_id FROM songs as s
    JOIN artists as a USING(artist_id)
    WHERE s.title = %s OR a.name = %s OR s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
