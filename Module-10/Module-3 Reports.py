import mysql.connector
from datetime import datetime

# Establish a database connection
def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Limecows02!Lime!",
            database="TravelAgencyFinal"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None

# Function to execute a query and fetch results
def execute_query(cursor, query, params=None):
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return []
    
# Execute a query and fetch results
def evaluate_sales():
    mydb = connect_to_database()
    if mydb:
        cursor = mydb.cursor()

        try:
            # Define date ranges for the first and second quarters
            start_date_1 = datetime(2022, 7, 1).date()
            end_date_1 = datetime(2022, 9, 30).date()
            start_date_2 = datetime(2022, 10, 1).date()
            end_date_2 = datetime(2022, 12, 31).date()

            total_payments_query = """
                SELECT SUM(PaymentAmount) AS TotalPayments
                FROM Payment
                WHERE PaymentDate BETWEEN %s AND %s
            """

            cursor.execute(total_payments_query, (start_date_1, end_date_2))
            total_payments = cursor.fetchone()[0]  # Fetch the total payments

            if total_payments:
                print(f"Total payments collected: ${total_payments:.2f}")
            else:
                print("No payment data available.")

            equipment_sales_query_1 = """
                SELECT SUM(e.EquipmentRetailPrice) AS TotalEquipmentRetailPrice
                FROM Customer_Order co
                JOIN Equipment e ON co.EquipmentID = e.EquipmentID
                JOIN Payment p ON co.PaymentID = p.PaymentID
                WHERE p.PaymentDate BETWEEN %s AND %s
            """

            equipment_result_1 = execute_query(cursor, equipment_sales_query_1, (start_date_1, end_date_1))
            total_equipment_sales_1 = equipment_result_1[0][0] if equipment_result_1[0][0] is not None else 0

            equipment_sales_query_2 = """
                SELECT SUM(e.EquipmentRetailPrice) AS TotalEquipmentRetailPrice
                FROM Customer_Order co
                JOIN Equipment e ON co.EquipmentID = e.EquipmentID
                JOIN Payment p ON co.PaymentID = p.PaymentID
                WHERE p.PaymentDate BETWEEN %s AND %s
            """
            equipment_result_2 = execute_query(cursor, equipment_sales_query_2, (start_date_2, end_date_2))
            total_equipment_sales_2 = equipment_result_2[0][0] if equipment_result_2[0][0] is not None else 0

            sales_percentage_1 = (total_equipment_sales_1 / total_payments) * 100 if total_payments != 0 else 0
            sales_percentage_2 = (total_equipment_sales_2 / total_payments) * 100 if total_payments != 0 else 0

            print(f"First Quarter Equipment Sales Percentage: {sales_percentage_1:.2f}%")
            print(f"Second Quarter Equipment Sales Percentage: {sales_percentage_2:.2f}%")

            if sales_percentage_1 < 40 and sales_percentage_2 < 40:
                print("Equipment sales contribute less than 40% for two consecutive quarters.")
                print("Reevaluate marketing strategy, consider e-commerce expansion, or adjust inventory levels.")
            else:
                print("Equipment sales meet criteria.")

        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
        finally:
            cursor.close()
            mydb.close()

# Evaluate equipment sales
if __name__ == "__main__":
    evaluate_sales()