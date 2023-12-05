"""Python Script that Creates TravelAgency Database and Tables
"""
import mysql.connector
import random

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword"
    )

# Create a cursor to execute SQL queries
cursor = mydb.cursor()

# SQL query to create the database
create_db_query = "CREATE DATABASE IF NOT EXISTS Milestone2"

try:
    # Execute the create database query
    cursor.execute(create_db_query)
    print("Database 'Milestone2' created successfully.")
except mysql.connector.Error as err:
    print(f"Error creating database: {err}")

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="Milestone2"  # Specify the database to use
)

# Create a new cursor after changing the database
cursor = mydb.cursor()

# Switch to the newly created 'TravelAgency' database
cursor.execute("USE Milestone2")

create_tables_query = [
    """
    CREATE TABLE IF NOT EXISTS Location (
        LocationID INT AUTO_INCREMENT PRIMARY KEY,
        LocationName VARCHAR(100),
        Country VARCHAR(50),
        City VARCHAR(50),
        StateProvidence VARCHAR(50),
        PostalCode VARCHAR(20)
    )""",
    """
    CREATE TABLE IF NOT EXISTS Guide (
        GuideID INT AUTO_INCREMENT PRIMARY KEY,
        LegalFirstName VARCHAR(50),
        LegalMiddleName VARCHAR(50),
        LegalLastName VARCHAR(50),
        PreferredName VARCHAR(50),
        Specialty VARCHAR(100),
        ExperienceLevel VARCHAR(50),
        ContactNumber VARCHAR(20),
        EmailAddress VARCHAR(100)
    )""",
    """
    CREATE TABLE IF NOT EXISTS Trip (
        TripID INT AUTO_INCREMENT PRIMARY KEY,
        LocationID INT,
        GuideID INT,
        StartDate DATE,
        EndDate DATE,
        TripCategory ENUM('Adventure', 'Camping', 'Hiking', 'Biking'),
        TripDescription TEXT,
        FOREIGN KEY (LocationID) REFERENCES Location(LocationID),
        FOREIGN KEY (GuideID) REFERENCES Guide(GuideID)
    )""",
    """
    CREATE TABLE IF NOT EXISTS Customer (
        CustomerID INT AUTO_INCREMENT PRIMARY KEY,
        LegalFirstName VARCHAR(50),
        LegalMiddleName VARCHAR(50),
        LegalLastName VARCHAR(50),
        PreferredName VARCHAR(50),
        Email VARCHAR(100),
        Phone VARCHAR(20),
        Address VARCHAR(100),
        Country VARCHAR(50),
        City VARCHAR(50),
        State VARCHAR(50),
        PostalCode VARCHAR(20)
    )""",
    """
    CREATE TABLE IF NOT EXISTS Payment (
        PaymentID INT AUTO_INCREMENT PRIMARY KEY,
        CustomerID INT,
        PaymentType ENUM('Cash', 'Card', 'Wire', 'EFT'),
        Description TEXT,
        PaymentAmount DECIMAL(10,2),
        PaymentStatus ENUM('Pending', 'Paid', 'Declined'),
        PaymentDate DATE,
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
    )""",    
    """
    CREATE TABLE IF NOT EXISTS Booking (
        BookingID INT AUTO_INCREMENT PRIMARY KEY,
        CustomerID INT,
        TripID INT,
        PaymentID INT,
        BookingDate DATE,
        BookingNotes TEXT,
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
        FOREIGN KEY (TripID) REFERENCES Trip(TripID),
        FOREIGN KEY (PaymentID) REFERENCES Payment(PaymentID)
    )""",
    
    """
    CREATE TABLE IF NOT EXISTS Equipment (
        EquipmentID INT AUTO_INCREMENT PRIMARY KEY,
        EquipmentName VARCHAR(100),
        EquipmentWholeSalePrice DECIMAL(10, 2),
        EquipmentRetailPrice DECIMAL(10,2),
        EquipmentStatus ENUM('Available', 'Rented', 'Out of Order'),
        ConditionDescription VARCHAR(100),
        Quantity INT
    )""",
    
    """
    CREATE TABLE IF NOT EXISTS Review (
        ReviewID INT AUTO_INCREMENT PRIMARY KEY,
        CustomerID INT,
        TripID INT,
        GuideID INT,
        ReviewDate DATE,
        Rating INT,
        ReviewComment TEXT,
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
        FOREIGN KEY (TripID) REFERENCES Trip(TripID),
        FOREIGN KEY (GuideID) REFERENCES Guide(GuideID)
    )""",
    """
    CREATE TABLE IF NOT EXISTS Customer_Order ( 
        OrderID INT AUTO_INCREMENT PRIMARY KEY,
        BookingID INT,
        EquipmentID INT,
        CustomerID INT,
        PaymentID INT,
        FOREIGN KEY (PaymentID) REFERENCES Payment(PaymentID),
        FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID),
        FOREIGN KEY (BookingID) REFERENCES Booking(BookingID),
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
        
    )"""
]

try:
    # Execute each table creation query
    for query in create_tables_query:
        cursor.execute(query)
    print("Tables created successfully.")

    # Commit changes to the database
    mydb.commit()
except mysql.connector.Error as err:
    print(f"Error creating tables: {err}")
finally:
    # Close cursor and database connections
    cursor.close()
    mydb.close()

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword"
    )

# Create a cursor to execute SQL queries
cursor = mydb.cursor()

# Switch to the 'TravelAgency' database
cursor.execute("USE Milestone2")

# Insert 10 customers into the 'Customer' table
customers = [
    ("John", "Doe", "Smith", "John Doe", "johndoe@email.com", "123-456-7890", "123 Main St.", "USA", "New York", "NY", "10001"),
    ("Jane", "Joanne", "Smith", "Jane Doe", "janedoe@email.com", "987-654-3210", "456 Elm St.", "USA", "Los Angeles", "CA", "90210"),
    ("Peter", "Jones", "Brown", "Bucky", "peterjones@email.com", "123-456-7890", "789 Oak St.", "USA", "Chicago", "IL", "60601"),
    ("Mary", "Jane", "Brown", "Mary Jane", "maryjones@email.com", "987-654-3210", "1011 Pine St.", "USA", "Houston", "TX", "77001"),
    ("David","Jerry", "Scott", "Candy", "davidwilliams@email.com", "123-456-7890", "1234 Maple St.", "USA", "Phoenix", "AZ", "85001"),
    ("Sarah", "Tammy", "Miller", "Sarah Williams", "sarahwilliams@email.com", "987-654-3210", "5678 Birch St.", "USA", "Philadelphia", "PA", "19101"),
    ("Michael", "Brown", "Davis", "Michael Brown", "michaelbrown@email.com", "123-456-7890", "9012 Ash St.", "USA", "San Antonio", "TX", "78229"),
    ("Jessica", "Gigi", "Davis", "Gigi", "jessicabrown@email.com", "987-654-3210", "1314 Elm St.", "USA", "San Diego", "CA", "92101"),
    ("James", "Miller", "Taylor", "James Miller", "jamesmiller@email.com", "123-456-7890", "1516 Oak St.", "USA", "Dallas", "TX", "75201"),
    ("Jennifer", "Bobby", "Taylor", "Jennifer Miller", "jennifermiller@email.com", "987-654-3210", "1718 Pine St.", "USA", "San Jose", "CA", "95112"),
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

    # Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword"
    )

# Create a cursor to execute SQL queries
cursor = mydb.cursor()

# Switch to the 'TravelAgency' database
cursor.execute("USE Milestone2")

# Insert 10 entries into the 'Location' table
locations = [
    ("Europe", "France", "Paris", "Ile-de-France", "75000"),
    ("Europe", "Spain", "Madrid", "Madrid", "28001"),
    ("Europe", "Italy", "Rome", "Lazio", "00118"),
    ("Europe", "Germany", "Berlin", "Berlin", "10115"),
    ("Europe", "United Kingdom", "London", "England", "SW1A 1AA"),
    ("Asia", "China", "Beijing", "Beijing", "100000"),
    ("Asia", "Japan", "Tokyo", "Tokyo", "100-8111"),
    ("Asia", "India", "New Delhi", "Delhi", "110001"),
    ("Asia", "South Korea", "Seoul", "Seoul", "04524"),
    ("Asia", "United Arab Emirates", "Dubai", "Dubai", "12345"),
    ("Africa", "South Africa", "Cape Town", "Western Cape", "8000"),
    ("Africa", "Nigeria", "Lagos", "Lagos", "100001"),
    ("Africa", "Kenya", "Nairobi", "Nairobi", "00100"),
    ("Africa", "Egypt", "Cairo", "Cairo", "11511"),
    ("Africa", "Morocco", "Casablanca", "Casablanca-Settat", "20250"),
]

insert_location_query = """
    INSERT INTO Location (
        LocationName,
        Country,
        City,
        StateProvidence,
        PostalCode
    )
    VALUES (%s, %s, %s, %s, %s)
"""

try:
    # Execute the insert location query for each location
    for location in locations:
        cursor.execute(insert_location_query, location)

    # Commit changes to the database
    mydb.commit()

    print("Locations inserted successfully.")
except mysql.connector.Error as err:
    print(f"Error inserting locations: {err}")
finally:
    # Close cursor and database connections
    cursor.close()
    mydb.close()

    # Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="Milestone2"  # Specify the database to use
)

# Create a new cursor after changing the database
cursor = mydb.cursor()

# Define the data for the two guides
guides_data = [
    ('John', '', 'MacNell', 'Mac', 'Hiking', 'Expert', '+1234567890', 'johnmac@example.com'),
    ('D.B.', '', 'Marland', 'Duke', 'Camping', 'Intermediate', '+1987654321', 'duke@example.com')
]

# SQL query to insert data into the Guide table
insert_query = "INSERT INTO Guide (LegalFirstName, LegalMiddleName, LegalLastName, PreferredName, Specialty, ExperienceLevel, ContactNumber, EmailAddress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

try:
    # Execute the insert query for each guide
    cursor.executemany(insert_query, guides_data)
    print("Guide data inserted successfully.")

    # Commit changes to the database
    mydb.commit()
except mysql.connector.Error as err:
    print(f"Error inserting data into Guide table: {err}")
finally:
    # Close cursor and database connections
    cursor.close()
    mydb.close()

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="Milestone2"
)

# Create a new cursor after changing the database
cursor = mydb.cursor()

# Select all LocationIDs and GuideIDs from their respective tables
cursor.execute("SELECT LocationID FROM Location")
location_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT GuideID FROM Guide")
guide_ids = [row[0] for row in cursor.fetchall()]

# Generate 10 unique trips
trips = []
for _ in range(10):
    location_id = random.choice(location_ids)
    guide_id = random.choice(guide_ids)
    start_date = "2023-01-01"  # Replace this with actual start date
    end_date = "2023-01-07"    # Replace this with actual end date
    trip_category = random.choice(['Adventure', 'Camping', 'Hiking', 'Biking'])
    trip_description = f"Trip to LocationID: {location_id} with GuideID: {guide_id}"

    trips.append((location_id, guide_id, start_date, end_date, trip_category, trip_description))

# SQL query to insert data into the Trip table
insert_trip_query = """
    INSERT INTO Trip (LocationID, GuideID, StartDate, EndDate, TripCategory, TripDescription)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

try:
    # Execute the insert query for each trip
    cursor.executemany(insert_trip_query, trips)
    print("Trips inserted successfully.")

    # Commit changes to the database
    mydb.commit()
except mysql.connector.Error as err:
    print(f"Error inserting data into Trip table: {err}")
finally:
    # Close cursor and database connections
    cursor.close()
    mydb.close()

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="Milestone2"
)

# Create a new cursor after changing the database
cursor = mydb.cursor()

# Fetching all CustomerIDs from the Customer table
cursor.execute("SELECT CustomerID FROM Customer")
customer_ids = [row[0] for row in cursor.fetchall()]

# Generating 10 unique payments
payments = []
for _ in range(10):
    customer_id = random.choice(customer_ids)  # Assuming customer_ids exist (IDs from Customer table)
    payment_type = random.choice(['Cash', 'Card', 'Wire', 'EFT'])
    description = f"Payment for CustomerID: {customer_id}"
    payment_amount = random.uniform(50, 500)  # Assuming payment amount range

    # Random date generation for payment date (change date range as needed)
    payment_date = "2023-01-07"    # Replace this with actual end date

    payment_status = random.choice(['Pending', 'Paid', 'Declined'])

    payments.append((customer_id, payment_type, description, payment_amount, payment_status, payment_date))

# SQL query to insert data into the Payment table
insert_payment_query = """
    INSERT INTO Payment (CustomerID, PaymentType, Description, PaymentAmount, PaymentStatus, PaymentDate)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

try:
    # Execute the insert query for each payment
    cursor.executemany(insert_payment_query, payments)
    print("Payments inserted successfully.")

    # Commit changes to the database
    mydb.commit()
except mysql.connector.Error as err:
    print(f"Error inserting data into Payment table: {err}")
finally:
    # Close cursor and database connections
    cursor.close()
    mydb.close()

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="Milestone2"
)

# Create a new cursor after changing the database
cursor = mydb.cursor()

# Fetching all BookingIDs from the Booking table
cursor.execute("SELECT BookingID FROM Booking")
booking_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT TripID FROM Trip")
trip_ids = [row[0] for row in cursor.fetchall()]

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="Milestone2"
)

# Create a new cursor after changing the database
cursor = mydb.cursor()

# Fetching all BookingIDs from the Booking table
cursor.execute("SELECT BookingID FROM Booking")
booking_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT TripID FROM Trip")
trip_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("Select PaymentID FROM Payment")
payment_ids = [row[0] for row in cursor.fetchall()]

bookings = []
for _ in range(10):
    trip_id = random.choice(trip_ids)
    customer_id = random.choice(customer_ids)  # Assuming customer_ids exist (IDs from Customer table)
    payment_id = random.choice(payment_ids)    # Assuming payment_ids exist (IDs from Payment table)
    booking_date = "2023-01-07"    # Replace this with actual booking date
    booking_notes = "Some notes about the booking..."

    bookings.append((customer_id, trip_id, payment_id, booking_date, booking_notes))

# SQL query to insert data into the Booking table
insert_booking_query = """
    INSERT INTO Booking (CustomerID, TripID, PaymentID, BookingDate, BookingNotes)
    VALUES (%s, %s, %s, %s, %s)
"""

try:
    # Execute the insert query for each booking
    cursor.executemany(insert_booking_query, bookings)
    print("Bookings inserted successfully.")

    # Commit changes to the database
    mydb.commit()
except mysql.connector.Error as err:
    print(f"Error inserting data into Booking table: {err}")
finally:
    # Close cursor and database connections
    cursor.close()
    mydb.close()

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="Milestone2"
)

# Create a new cursor after changing the database
cursor = mydb.cursor()

# Equipment data
equipment_data = [
    ("Tent", 80.00, 120.00, "Available", "Good condition", 50),
    ("Backpack", 40.00, 60.00, "Available", "Slight wear", 100),
    ("Sleeping Bag", 50.00, 80.00, "Available", "Excellent condition", 75),
    ("Hiking Boots", 60.00, 100.00, "Available", "New", 30),
    ("Camping Stove", 70.00, 110.00, "Available", "Used, functional", 25),
    ("Headlamp", 25.00, 45.00, "Available", "Lightly used", 80),
    ("Water Filter", 45.00, 70.00, "Available", "Like new", 40),
    ("Trekking Poles", 35.00, 55.00, "Available", "Good condition", 60),
    ("Cookware Set", 55.00, 90.00, "Available", "Slight scratches", 45),
    ("First Aid Kit", 20.00, 35.00, "Available", "Sealed, unopened", 90),
    ("Portable Chair", 30.00, 50.00, "Available", "Used but sturdy", 70),
    ("Navigation Compass", 15.00, 25.00, "Available", "Excellent condition", 100),
    ("Tarpaulin", 20.00, 40.00, "Available", "Minor tears, usable", 55),
    ("Camp Pillow", 10.00, 20.00, "Available", "Washed, clean", 120),
    ("Fire Starter Kit", 18.00, 30.00, "Available", "Unused", 85),
    ("Dry Bags", 22.00, 38.00, "Available", "Waterproof, intact", 65),
    ("Mosquito Net", 28.00, 48.00, "Available", "Like new", 75),
    ("Camp Shower", 32.00, 55.00, "Available", "Gently used", 50),
    ("Multi-tool", 40.00, 65.00, "Available", "Functional, good shape", 70),
    ("Camping Hammock", 50.00, 85.00, "Available", "Slight stains", 40),
    ("Emergency Whistle", 8.00, 15.00, "Available", "Compact, loud", 95),
    ("Solar Charger", 60.00, 100.00, "Available", "Efficient, reliable", 30),
    ("Handheld GPS", 70.00, 120.00, "Available", "Used for navigation", 25),
    ("Bear Canister", 40.00, 70.00, "Available", "Scratched, functional", 60),
    ("Camp Axe", 55.00, 95.00, "Available", "Sharp, used", 35),
]

# SQL query to insert data into the Equipment table
insert_equipment_query = """
    INSERT INTO Equipment (
        EquipmentName,
        EquipmentWholeSalePrice,
        EquipmentRetailPrice,
        EquipmentStatus,
        ConditionDescription,
        Quantity
    )
    VALUES (%s, %s, %s, %s, %s, %s)
"""

try:
    # Execute the insert query for each equipment entry
    cursor.executemany(insert_equipment_query, equipment_data)
    print("Equipment entries inserted successfully.")

    # Commit changes to the database
    mydb.commit()
except mysql.connector.Error as err:
    print(f"Error inserting data into Equipment table: {err}")
finally:
    # Close cursor and database connections
    cursor.close()
    mydb.close()

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="Milestone2"
)

# Create a new cursor after changing the database
cursor = mydb.cursor()

reviews = [
    "My experience with this travel agency was exceptional! From booking to the actual trip, everything was seamless. The staff was incredibly helpful and made sure every detail was taken care of. Highly recommended!",
    "I've used many travel agencies before, but this one stands out. Their attention to customer preferences and personalized recommendations made my vacation unforgettable. I'll definitely be using their services again.",
    "The team at this travel agency went above and beyond to accommodate our last-minute changes. Their flexibility and professionalism were commendable. Our trip was fantastic, thanks to their efforts.",
    "I cannot thank this travel agency enough for organizing such a fantastic tour. Every aspect was well-planned, and the tour guides were knowledgeable. It was a worry-free experience, and I enjoyed every moment.",
    "Booking through this travel agency was a breeze. They offered competitive prices and a wide range of options. The communication was excellent, and they were quick to respond to any queries. Impressive service!",
    "My family and I had a wonderful vacation, all thanks to this travel agency. They suggested the perfect destinations based on our preferences, and the itinerary was well thought out. It was a truly memorable experience.",
    "I had a fantastic solo trip organized by this agency. They catered to my specific requests and made sure I felt safe and comfortable throughout the journey. I'm grateful for their expertise and attention to detail.",
    "The cruise package arranged by this travel agency exceeded my expectations. The onboard activities and excursions were well-organized. It was a luxurious experience, and I couldn't have asked for more.",
    "The professionalism of this travel agency was impressive. They guided us through the entire process, providing valuable insights and recommendations. Our trip was flawless, and we're already planning our next one with them.",
    "I had an amazing adventure trip, all thanks to the impeccable planning by this travel agency. The guides were knowledgeable, accommodations were top-notch, and the overall experience was simply incredible. Highly recommended for adventure seekers!"
]

# SQL query to insert data into the Review table
insert_review_query = """
    INSERT INTO Review (
        CustomerID,
        TripID,
        GuideID,
        ReviewDate,
        Rating,
        ReviewComment
    )
    VALUES (%s, %s, %s, %s, %s, %s)
"""

try:
    for review_text in reviews:
        # For each review, generate mock data for CustomerID, TripID, GuideID, ReviewDate, and Rating
        customer_id = random.choice(customer_ids)  # Assuming customer_ids exist (IDs from Customer table)
        trip_id = random.choice(trip_ids)          # Assuming trip_ids exist (IDs from Trip table)
        guide_id = random.choice(guide_ids)        # Assuming guide_ids exist (IDs from Guide table)
        review_date = "2023-12-04"                # Replace this with the actual review date
        rating = random.randint(1, 5)             # Assuming the rating is between 1 and 5

        # Execute the insert query for each review
        cursor.execute(insert_review_query, (customer_id, trip_id, guide_id, review_date, rating, review_text))

    # Commit changes to the database
    mydb.commit()
    print("Reviews inserted successfully.")
except mysql.connector.Error as err:
    print(f"Error inserting data into Review table: {err}")
finally:
    # Close cursor and database connections
    cursor.close()
    mydb.close()

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="Milestone2"
)

# Create a cursor to execute SQL queries
cursor = mydb.cursor()

# Fetching all BookingIDs, TripIDs, PaymentIDs, and CustomerIDs from their respective tables
cursor.execute("SELECT BookingID FROM Booking")
booking_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT EquipmentID FROM Equipment")
equipment_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT CustomerID FROM Customer")
customer_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT PaymentID FROM Payment")
payment_ids = [row[0] for row in cursor.fetchall()]

customer_order_data = []
for _ in range(6):
    # Generate mock data for BookingID, EquipmentID, PaymentID, CustomerID, BookingDate, and BookingNotes
    booking_id = random.choice(booking_ids)       # Assuming booking_ids exist (IDs from Booking table)
    equipment_id = random.choice(equipment_ids)   # Assuming equipmentID exist (IDs from Equipment table)
    customer_id = random.choice(customer_ids)     # Assuming customer_ids exist (IDs from Customer table)
    payment_id = random.choice(payment_ids)       # Assuming payment_ids exist (IDs from Payment table)
    
    customer_order_data.append((booking_id, equipment_id, customer_id, payment_id))

# SQL query to insert data into the Customer_Order table
insert_customer_order_query = """
    INSERT INTO Customer_Order (
        BookingID,
        EquipmentID,
        CustomerID,
        PaymentID
    )
    VALUES (%s, %s, %s, %s)
"""

try:
    # Execute the insert query for each customer order entry
    cursor.executemany(insert_customer_order_query, customer_order_data)
    print("Customer Order entries inserted successfully.")

    # Commit changes to the database
    mydb.commit()
except mysql.connector.Error as err:
    print(f"Error inserting data into Customer_Order table: {err}")
finally:
    # Close cursor and database connection
    cursor.close()
    mydb.close()

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="Milestone2"
)

# Create a cursor
cursor = mydb.cursor()

# Function to display data from a table
def display_table_data(table_name):
    print(f"Displaying data from table: {table_name}")
    select_query = f"SELECT * FROM {table_name}"

    try:
        cursor.execute(select_query)
        table_data = cursor.fetchall()

        # Print column names
        column_names = [i[0] for i in cursor.description]
        print(column_names)

        # Print table data
        for row in table_data:
            print(row)
        
        print("\n")
    except mysql.connector.Error as err:
        print(f"Error retrieving data from {table_name} table: {err}")

# List of table names
tables = [
    "Location",
    "Guide",
    "Trip",
    "Customer",
    "Payment",
    "Booking",
    "Equipment",
    "Review",
    "Customer_Order"
]

# Display data from each table
for table in tables:
    display_table_data(table)

# Close cursor and database connection
cursor.close()
mydb.close()
