from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL database
try:
    conn = psycopg2.connect(
        dbname="movie_rating_system",
        user="movie_rating",
        password="root",
        host="localhost",
        port="5432"
    )
    c = conn.cursor()
except psycopg2.OperationalError as e:
    print("Unable to connect to the database:", e)
    exit(1)


# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Email and password are required"}), 400

    email = data['email']
    password = data['password']

    try:
        c.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        user = c.fetchone()
        if user:
            user_data = {
                "id": user[0],
                "name": user[1],
                "phone": user[2],
                "email": user[4]
            }
            return jsonify({"message": "Login successful", "user": user_data}), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401
    except psycopg2.Error as e:
        print("Error fetching user from database:", e)
        return jsonify({"error": "Internal server error"}), 500


# Route to get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        c.execute('SELECT * FROM movies')
        movies = c.fetchall()
        return jsonify({"movies": movies}), 200
    except psycopg2.Error as e:
        print("Error fetching movies from database:", e)
        return jsonify({"error": "Internal server error"}), 500


# Route to add a movie
@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    if not data or 'name' not in data or 'genre' not in data or 'rating' not in data or 'release_date' not in data:
        return jsonify({"error": "Name, genre, rating, and release date are required"}), 400

    name = data['name']
    genre = data['genre']
    rating = data['rating']
    release_date = data['release_date']

    try:
        c.execute('INSERT INTO movies (name, genre, rating, release_date) VALUES (%s, %s, %s, %s)',
                  (name, genre, rating, release_date))
        conn.commit()
        return jsonify({"message": "Movie added successfully"}), 201
    except psycopg2.Error as e:
        print("Error adding movie to database:", e)
        return jsonify({"error": "Internal server error"}), 500


# Route to rate a movie
@app.route('/rate_movie', methods=['POST'])
def rate_movie():
    data = request.json
    if not data or 'user_id' not in data or 'movie_id' not in data or 'rating' not in data:
        return jsonify({"error": "User ID, movie ID, and rating are required"}), 400

    user_id = data['user_id']
    movie_id = data['movie_id']
    rating = data['rating']

    try:
        c.execute('INSERT INTO ratings (user_id, movie_id, rating) VALUES (%s, %s, %s)', (user_id, movie_id, rating))
        conn.commit()
        return jsonify({"message": "Rating added successfully"}), 201
    except psycopg2.Error as e:
        print("Error adding rating to database:", e)
        return jsonify({"error": "Internal server error"}), 500


# Route to search for a movie by name and get its details along with average rating
@app.route('/search_movie', methods=['GET'])
def search_movie():
    name = request.args.get('name')
    try:
        c.execute('SELECT * FROM movies WHERE name = %s', (name,))
        movie = c.fetchone()
        if not movie:
            return jsonify({"error": "Movie not found"}), 404

        movie_id = movie[0]
        c.execute('SELECT AVG(rating) FROM ratings WHERE movie_id = %s', (movie_id,))
        average_rating = c.fetchone()[0] or 0  # If no ratings exist, set average to 0
        return jsonify({"movie": movie, "average_rating": average_rating}), 200
    except psycopg2.Error as e:
        print("Error searching for movie in database:", e)
        return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
