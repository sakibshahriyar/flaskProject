Movie Rating System

Overview:
The Movie Rating System is a Flask-based web application that allows users to log in, view, add, rate movies, and search for movies by name. The application uses a PostgreSQL database to store user information, movie details, and ratings.

Setup and Installation:
1. Clone the repository:
   git clone <repository_url>
   cd movie-rating-system

2. Install dependencies:
   pip install -r requirements.txt

3. Database setup:
   - Make sure you have PostgreSQL installed and running on your machine.
   - Create a database named 'movie_rating_system' with a user 'movie_rating' and password 'root'. You can modify these credentials in the 'app.py' file if needed.
   - Run the provided SQL script ('sample_data.sql') to create the necessary tables in your PostgreSQL database.

4. Run the application:
   python app.py

5. Access the application:
   Once the application is running, you can access it at 'http://localhost:5000' in your web browser.

Endpoints:

User Login
- URL: /login
- Method: POST
- Parameters:
  - email: User's email address
  - password: User's password
- Response: Returns user information upon successful login.

Get All Movies
- URL: /movies
- Method: GET
- Response: Returns a list of all movies stored in the database.

Add a Movie
- URL: /movies
- Method: POST
- Parameters:
  - name: Movie name
  - genre: Movie genre
  - rating: Movie rating
  - release_date: Movie release date
- Response: Adds the movie to the database upon successful addition.

Rate a Movie
- URL: /rate_movie
- Method: POST
- Parameters:
  - user_id: User ID
  - movie_id: Movie ID
  - rating: User's rating for the movie
- Response: Adds the user's rating for the movie to the database.

Search for a Movie
- URL: /search_movie
- Method: GET
- Parameters:
  - name: Movie name to search for
- Response: Returns movie details along with the average rating.

Sample Data:
Sample data is provided to populate the database with initial user information, movie details, and ratings. Run the provided script ('insert_sample_data') to insert this data into your database.

Dependencies:
- Flask
- psycopg2

