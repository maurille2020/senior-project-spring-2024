import sqlite3
import json
import os

# Function to create tables
def create_tables(cursor, json_data):
    for table_name, columns in json_data.items():
        column_definitions = ', '.join([f"{column['id']} {column['type']}" for column in columns])
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})')

# Function to insert data from JSON files
def insert_data_from_json(cursor, conn, filename, table_name):
    with open(filename, 'r') as file:
        data = json.load(file)
        for entry in data:
            values = [entry[column['id']] for column in table_columns[table_name]]
            cursor.execute(f'INSERT INTO {table_name} VALUES ({",".join(["?"] * len(values))})', values)
    conn.commit()

# Function to generate password
def generate_password(name):
    return name.lower().replace(" ", "") + "123"

# Main function
def main():
    # Connect to SQLite database
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    # Define table columns from JSON files
    table_columns = {}
    for json_file in ['staff_info.json', 'student_info.json', 'news_info.json', 'internship_info.json']:
        table_name = os.path.splitext(json_file)[0]  # Extract table name from JSON file name
        with open(json_file, 'r') as file:
            table_columns[table_name] = json.load(file)

    # Create tables
    create_tables(cursor, table_columns)

    # Prompt user for each JSON file and insert data into corresponding tables
    for table_name in table_columns.keys():
        filename = input(f"Enter the path to the JSON file for the '{table_name}' table: ")
        if os.path.exists(filename):
            insert_data_from_json(cursor, conn, filename, table_name)
        else:
            print(f"File '{filename}' not found.")

    # Close connection
    conn.close()

if __name__ == "__main__":
    main()
