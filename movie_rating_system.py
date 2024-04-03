import psycopg2


# Function to insert sample data into the database
def insert_sample_data(conn):
    c = conn.cursor()

    # Sample data
    users = [
        {"name": "John Doe", "phone": "11111111111", "password": "pass1", "email": "john_doe@gmail.com"},
        {"name": "Jane Doe", "phone": "22222222222", "password": "pass2", "email": "jane_doe@gmail.com"},
        {"name": "Mark Doe", "phone": "3333333333", "password": "pass3", "email": "mark_doe@gmail.com"},
        {"name": "Macy Doe", "phone": "4444444444", "password": "pass4", "email": "macy_doe@gmail.com"}
    ]

    movies = [
        {"name": "Home Alone", "genre": "Comedy", "rating": "PG", "release_date": "01-04-1996"},
        {"name": "The Godfather", "genre": "Crime", "rating": "R", "release_date": "01-04-1972"},
        {"name": "Avengers: Endgame", "genre": "Action", "rating": "PG", "release_date": "01-04-2019"}
    ]

    ratings = [
        {"user_id": 1, "movie_id": 1, "rating": 5.0},
        {"user_id": 1, "movie_id": 2, "rating": 4.0},
        {"user_id": 1, "movie_id": 3, "rating": 3.3},
        {"user_id": 2, "movie_id": 1, "rating": 5.0},
        {"user_id": 2, "movie_id": 3, "rating": 4.5},
        {"user_id": 3, "movie_id": 1, "rating": 1.6},
        {"user_id": 3, "movie_id": 2, "rating": 0.0},
        {"user_id": 3, "movie_id": 3, "rating": 3.4},
        {"user_id": 4, "movie_id": 2, "rating": 4.5}
    ]

    try:
        for user in users:
            c.execute('INSERT INTO users (name, phone, password, email) VALUES (%s, %s, %s, %s)',
                      (user['name'], user['phone'], user['password'], user['email']))

        for movie in movies:
            c.execute('INSERT INTO movies (name, genre, rating, release_date) VALUES (%s, %s, %s, %s)',
                      (movie['name'], movie['genre'], movie['rating'], movie['release_date']))

        for rating in ratings:
            c.execute('INSERT INTO ratings (user_id, movie_id, rating) VALUES (%s, %s, %s)',
                      (rating['user_id'], rating['movie_id'], rating['rating']))

        conn.commit()
        print("Sample data inserted successfully.")
    except psycopg2.Error as e:
        print("Error inserting sample data:", e)


# Connect to PostgreSQL database
try:
    conn = psycopg2.connect(
        dbname="movie_rating_system",
        user="movie_rating",
        password="root",
        host="localhost",
        port="5432"
    )
    insert_sample_data(conn)
    conn.close()
except psycopg2.OperationalError as e:
    print("Unable to connect to the database:", e)
