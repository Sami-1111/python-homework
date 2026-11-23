import sqlite3

connect = sqlite3.connect("online_cinema.db")

cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
)
""")

connect.commit()


def create_user(name):
    cursor.execute(
        "INSERT INTO users (name) VALUES (?)",
        (name,)
    )
    connect.commit()


def create_movie(title, genre):
    cursor.execute(
        "INSERT INTO movies (title, genre) VALUES (?, ?)",
        (title, genre)
    )
    connect.commit()


def create_review(user_id, movie_id, rating):
    cursor.execute(
        "INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)",
        (user_id, movie_id, rating)
    )
    connect.commit()


def read_reviews():
    cursor.execute("""
    SELECT users.name, movies.title, reviews.rating
    FROM reviews
    JOIN users ON reviews.user_id = users.id
    JOIN movies ON reviews.movie_id = movies.id
    """)

    reviews = cursor.fetchall()

    for review in reviews:
        print(review)


def read_all_movies():
    cursor.execute("""
    SELECT movies.title, movies.genre, reviews.rating
    FROM movies
    LEFT JOIN reviews ON movies.id = reviews.movie_id
    """)

    movies = cursor.fetchall()

    for movie in movies:
        print(movie)


def get_average_rating():
    cursor.execute("SELECT AVG(rating) FROM reviews")
    print("Средняя оценка:", cursor.fetchone()[0])


def get_max_rating():
    cursor.execute("SELECT MAX(rating) FROM reviews")
    print("Максимальная оценка:", cursor.fetchone()[0])


def get_min_rating():
    cursor.execute("SELECT MIN(rating) FROM reviews")
    print("Минимальная оценка:", cursor.fetchone()[0])


create_user("Алия")
create_user("Бек")
create_user("Самира")
create_user("Данияр")
create_user("Айжан")

create_movie("Интерстеллар", "Фантастика")
create_movie("Титаник", "Драма")
create_movie("Матрица", "Фантастика")
create_movie("Гарри Поттер", "Фэнтези")
create_movie("Начало", "Триллер")

create_review(1, 1, 10)
create_review(2, 1, 9)
create_review(3, 2, 8)
create_review(4, 2, 10)
create_review(5, 3, 9)
create_review(1, 3, 8)
create_review(2, 4, 10)
create_review(3, 4, 9)
create_review(4, 5, 8)
create_review(5, 5, 10)
create_review(1, 2, 7)
create_review(2, 3, 9)

print("Имя пользователя, фильм, оценка:")
read_reviews()

print("\nВсе фильмы:")
read_all_movies()

get_average_rating()
get_max_rating()
get_min_rating()

connect.close()