import mysql.connector

# Constants for database connection
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'TravelAgency'
}

# Constants for SQL queries
CREATE_DB_QUERY = "CREATE DATABASE IF NOT EXISTS TravelAgency"

CREATE_TABLES_QUERIES = [
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
)
"""
    ,
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
)
"""
    ,
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
)
"""
    ,
"""
CREATE TABLE IF NOT EXISTS Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY,
    ItemName VARCHAR(100),
    PurchaseDate DATE,
    Price DECIMAL(10, 2),
    Status ENUM('Available', 'Rented', 'Out of Order'),
    Condition VARCHAR(100),
    Quantity INT
)
"""
    ,
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
)
"""
    ,
"""
CREATE TABLE IF NOT EXISTS Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY,
    EquipmentID INT,
    Quantity INT,
    Condition VARCHAR(100),
    LocationID INT,
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID),
    FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
)
"""
    ,
"""
CREATE TABLE IF NOT EXISTS PaymentMethod (
    PaymentMethodID INT AUTO_INCREMENT PRIMARY KEY,
    PaymentMethodName VARCHAR(50),
    Description TEXT
)
"""
    ,
"""
CREATE TABLE IF NOT EXISTS Location (
    LocationID INT AUTO_INCREMENT PRIMARY KEY,
    LocationName VARCHAR(100),
    Country VARCHAR(50),
    City VARCHAR(50),
    State VARCHAR(50),
    PostalCode VARCHAR(20)
)
"""
    ,
"""
CREATE TABLE IF NOT EXISTS Income (
    IncomeID INT AUTO_INCREMENT PRIMARY KEY,
    BookingID INT,
    Amount DECIMAL(10, 2),
    Date DATE,
    IncomeSource VARCHAR(100),
    FOREIGN KEY (BookingID) REFERENCES Booking(BookingID)
)
"""
    ,
"""
CREATE TABLE IF NOT EXISTS Expenses (
    ExpenseID INT AUTO_INCREMENT PRIMARY KEY,
    TripID INT,
    ExpenseType ENUM('Accommodation', 'Transportation', 'Food', 'Activities'),
    ExpenseDescription TEXT,
    Amount DECIMAL(10, 2),
    Date DATE,
    FOREIGN KEY (TripID) REFERENCES Trip(TripID)
)
"""
    ,
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
)
"""
    ,

]

def create_database_connection():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def create_database(cursor):
    try:
        # Execute the create database query
        cursor.execute(CREATE_DB_QUERY)
        print("Database 'TravelAgency' created successfully.")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

def create_tables(cursor):
    try:
        for query in CREATE_TABLES_QUERIES:
            cursor.execute(query)
        print("Tables created successfully.")
    except mysql.connector.Error as err:
        print(f"Error creating tables: {err}")

def main():
    # Establish connection to MySQL server
    mydb = create_database_connection()
    if mydb:
        # Create a cursor to execute SQL queries
        with mydb.cursor() as cursor:
            # Create the database
            create_database(cursor)

            # Reconnect to the server and switch to the TravelAgency database
            mydb.database = DB_CONFIG['database']

            # Create tables
            create_tables(cursor)

    # Close the database connection
    if mydb:
        mydb.close()
