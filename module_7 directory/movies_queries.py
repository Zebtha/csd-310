import mysql.connector

# Connect to the database
db = mysql.connector.connect(host='localhost', user='root', password='Limecows02!Lime!', database='movies')

# Create a cursor object
cursor = db.cursor()

# Define the query title
query_title = "-- DISPLAYING Studio RECORDS --"

# Execute the query
cursor.execute('SELECT * FROM studio')

# Fetch the results
studios = cursor.fetchall()

# Print the results, with a title 
print(query_title)
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

# Define the query title
query_title = " -- DISPLAYING Genre RECORDS --"

# Execute the query
cursor.execute('SELECT * FROM genre')

# Fetch the results
genre = cursor.fetchall()

# Print the results, with a title 
print(query_title)
for genre in genre:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

# Define the query title
query_title = " -- DISPLAYING Short Film RECORDS --"

# Execute the query
cursor.execute('SELECT film_name, film_runtime FROM film WHERE film_runtime < 120')

# Fetch the results
film = cursor.fetchall()

# Print the results, with a title 
print(query_title)
for film in film:
    print("Film Name: {}\nRuntime: {} \n".format(film[0],film[1]))

# Define the query title
query_title = " -- DISPLAYING Director RECORDS in Order --"

# Execute the query
cursor.execute('SELECT film_name, film_director FROM film ORDER BY film_director')

# Fetch the results
film = cursor.fetchall()

# Print the results, with a title 
print(query_title)
for film in film:
    print("Film Name: {}\nDirector: {} \n".format(film[0],film[1]))

# Close the cursor and database connection
cursor.close()
db.close()