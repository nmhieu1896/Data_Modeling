# Build a simple pipeline for transforming json data from files to table


### Step1: Create tables for storing by running script:
> python create_tables.py

This script Drop all exists tables and create new ones


### Step2: Run pipeline by script:
> python etl.py

This script load data from songs_data and log_data. Then insert these data into created tables


### file "test.ipynb" for checking whether tables and data is imported or not!
### file "etl.ipynb" for running "step 2" step by step


## Project Description

#### Dimension Tables
1. users - users in the app
    - *user_id, first_name, last_name, gender, level*
2. songs - songs in music database
    - *song_id, title, artist_id, year, duration*
3. artists - artist in music database
    - *artist_id, name, location, latitude, longitude*
4. time - timestamps of records in **songplays** broken down into specific units
    - *start_time, hour, day, week, month, year, weekday*
    
#### Fact Table
5. songplays - records in log data associated with song plays i.e. records with page **NextSong**
    - *songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent*
