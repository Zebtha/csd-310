import mysql.connector

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Limecows02!Lime!"
    )

# Switch to the 'TravelAgency' database
cursor.execute("USE Milestone2")

# Insert 10 customers into the 'Customer' table
customers = [
    ("John", "Doe", "Smith", "John Doe", "johndoe@email.com", "123-456-7890", "123 Main St.", "USA", "New York", "NY", "10001"),
    ("Jane", "Doe", "Smith", "Jane Doe", "janedoe@email.com", "987-654-3210", "456 Elm St.", "USA", "Los Angeles", "CA", "90210"),
    ("Peter", "Jones", "Brown", "Peter Jones", "peterjones@email.com", "123-456-7890", "789 Oak St.", "USA", "Chicago", "IL", "60601"),
    ("Mary", "Jones", "Brown", "Mary Jones", "maryjones@email.com", "987-654-3210", "1011 Pine St.", "USA", "Houston", "TX", "77001"),
    ("David", "Williams", "Miller", "David Williams", "davidwilliams@email.com", "123-456-7890", "1234 Maple St.", "USA", "Phoenix", "AZ", "85001"),
    ("Sarah", "Williams", "Miller", "Sarah Williams", "sarahwilliams@email.com", "987-654-3210", "5678 Birch St.", "USA", "Philadelphia", "PA", "19101"),
    ("Michael", "Brown", "Davis", "Michael Brown", "michaelbrown@email.com", "123-456-7890", "9012 Ash St.", "USA", "San Antonio", "TX", "78229"),
    ("Jessica", "Brown", "Davis", "Jessica Brown", "jessicabrown@email.com", "987-654-3210", "1314 Elm St.", "USA", "San Diego", "CA", "92101"),
    ("James", "Miller", "Taylor", "James Miller", "jamesmiller@email.com", "123-456-7890", "1516 Oak St.", "USA", "Dallas", "TX", "75201"),
    ("Jennifer", "Miller", "Taylor", "Jennifer Miller", "jennifermiller@email.com", "987-654-3210", "1718 Pine St.", "USA", "San Jose", "CA", "95112"),
]

insert_customer_query = """
    INSERT INTO Customer (
        LegalFirstName,
        LegalMiddleName,
        LegalLastName,
        PreferredName,
        Email,
        Phone,
        Address,
        Country,
        City,
        State,
        PostalCode
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

try:
    # Execute the insert customer query for each customer
    for customer in customers:
        cursor.execute(insert_customer_query, customer)

    # Commit changes to the database
    mydb.commit()

    print("Customers inserted successfully.")
except mysql.connector.Error as err:
    print(f"Error inserting customers: {err}")
finally:
    # Close cursor and database connections
    cursor.close()
    mydb.close()