import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='Limecows02!Lime!', database='movies')

# Create a cursor object
cursor = db.cursor()


def show_films(cursor, title):
    cursor.execute("SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio "
                   "Name' FROM film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON "
                   "film.studio_id = studio.studio_id")

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2],
                                                                                         film[3]))


# Display all films
show_films(cursor, "DISPLAYING FILMS")

# Insert a new record into the 'film' table
cursor.execute("INSERT INTO film (film_name, film_director, genre_id, studio_id, film_runtime, film_releaseDate) "
               "VALUES ('Mrs. Doubtfire', 'Chris Columbus', 3, 1, 125, 1993)")
# Commit the changes to the database
db.commit()
# Display all films
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Update the genre of the film "Alien" to "Horror"
cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")

# Commit the changes to the database
db.commit()

# Display all films
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

# Delete Gladiator from table
cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'") 

# Commit the changes to the database
db.commit()

# Display all films
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

