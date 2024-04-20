import jwt
import sqlite3
from datetime import datetime, timedelta

# Function to generate JWT token with SQL payload
def generate_jwt_payload():

    conn = sqlite3.connect("shaw_university.db")
    cursor = conn.cursor()

    # Execute SQL queries to retrieve data from all tables
    cursor.execute("SELECT * FROM staff")
    staff_data = cursor.fetchall()

    cursor.execute("SELECT * FROM internships")
    internships_data = cursor.fetchall()

    cursor.execute("SELECT * FROM students")
    students_data = cursor.fetchall()

    cursor.execute("SELECT * FROM news")
    news_data = cursor.fetchall()

    cursor.execute("SELECT * FROM statistics")
    statistics_data = cursor.fetchall()

    # Close database connection
    conn.close()

    # Payload to be encrypted
    payload = {
        'staff_data': staff_data,
        'internships_data': internships_data,
        'students_data': students_data,
        'news_data': news_data,
        'statistics_data': statistics_data,
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiration time
    }


    secret_key = 'Maurille_Was_Not_Here_teehee'

    # Generate JWT token with payload using PyJWT library
    jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')

    return jwt_token


if __name__ == "__main__":
    jwt_token = generate_jwt_payload()
    print("JWT Token:", jwt_token)
