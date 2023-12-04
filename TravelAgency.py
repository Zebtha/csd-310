import mysql.connector

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Limecows02!Lime!"
    )

# Create a cursor to execute SQL queries
cursor = mydb.cursor()


# SQL query to create the database
create_db_query = "CREATE DATABASE IF NOT EXISTS TravelAgency"

try:
    # Execute the create database query
    cursor.execute(create_db_query)
    print("Database 'TravelAgency' created successfully.")
except mysql.connector.Error as err:
    print(f"Error creating database: {err}")

# Establish a connection to your MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Limecows02!Lime!",
    database="TravelAgency"  # Specify the database to use
)

# Create a new cursor after changing the database
cursor = mydb.cursor()

# Switch to the newly created 'TravelAgency' database
cursor.execute("USE TravelAgency")

create_tables_query = [
    """
    CREATE TABLE IF NOT EXISTS Equipment (
        EquipmentID INT AUTO_INCREMENT PRIMARY KEY,
        ItemName VARCHAR(100),
        PurchaseDate DATE,
        Price DECIMAL(10, 2),
        Status ENUM('Available', 'Rented', 'Out of Order'),
        ConditionDescription VARCHAR(100),
        Quantity INT
    )""",
    """
    CREATE TABLE IF NOT EXISTS Location (
        LocationID INT AUTO_INCREMENT PRIMARY KEY,
        LocationName VARCHAR(100),
        Country VARCHAR(50),
        City VARCHAR(50),
        State VARCHAR(50),
        PostalCode VARCHAR(20)
    )""",
    """
    CREATE TABLE IF NOT EXISTS Inventory (
        InventoryID INT AUTO_INCREMENT PRIMARY KEY,
        EquipmentID INT,
        Quantity INT,
        ConditionDescription VARCHAR(100),
        LocationID INT,
        FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID),
        FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
    )""",
    """
    CREATE TABLE IF NOT EXISTS PaymentMethod (
        PaymentMethodID INT AUTO_INCREMENT PRIMARY KEY,
        PaymentMethodName VARCHAR(50),
        Description TEXT
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
    CREATE TABLE IF NOT EXISTS Customers (
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
    CREATE TABLE IF NOT EXISTS Trip (
        TripID INT AUTO_INCREMENT PRIMARY KEY,
        LocationID INT,
        StartDate DATE,
        EndDate DATE,
        GuideID INT,
        TripCategory ENUM('Adventure', 'Camping', 'Hiking', 'Biking'),
        TripDescription TEXT,
        FOREIGN KEY (LocationID) REFERENCES Location(LocationID),
        FOREIGN KEY (GuideID) REFERENCES Guide(GuideID)
    )""",
    """
    CREATE TABLE IF NOT EXISTS Booking (
        BookingID INT AUTO_INCREMENT PRIMARY KEY,
        CustomerID INT,
        TripID INT,
        BookingDate DATE,
        PaymentStatus ENUM('Pending', 'Paid'),
        PaymentMethodID INT,
        BookingNotes TEXT,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
        FOREIGN KEY (TripID) REFERENCES Trip(TripID),
        FOREIGN KEY (PaymentMethodID) REFERENCES PaymentMethod(PaymentMethodID)
    )""",
    """
    CREATE TABLE IF NOT EXISTS Income (
        IncomeID INT AUTO_INCREMENT PRIMARY KEY,
        BookingID INT,
        Amount DECIMAL(10, 2),
        Date DATE,
        IncomeSource VARCHAR(100),
        FOREIGN KEY (BookingID) REFERENCES Booking(BookingID)
    )""",
    """
    CREATE TABLE IF NOT EXISTS Expenses (
        ExpenseID INT AUTO_INCREMENT PRIMARY KEY,
        TripID INT,
        ExpenseType ENUM('Accommodation', 'Transportation', 'Food', 'Activities'),
        ExpenseDescription TEXT,
        Amount DECIMAL(10, 2),
        Date DATE,
        FOREIGN KEY (TripID) REFERENCES Trip(TripID)
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
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
        FOREIGN KEY (TripID) REFERENCES Trip(TripID),
        FOREIGN KEY (GuideID) REFERENCES Guide(GuideID)
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