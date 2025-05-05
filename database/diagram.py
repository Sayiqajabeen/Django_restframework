# import sqlite3

# # Path to the uploaded SQLite file
# db_path = '/mnt/data/credit_reports.db'

# # Connect to the SQLite database and fetch its schema
# def get_db_schema(db_path):
#     with sqlite3.connect(db_path) as conn:
#         cursor = conn.cursor()
#         # Fetch all table names
#         cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#         tables = cursor.fetchall()
        
#         schema = {}
#         for table in tables:
#             table_name = table[0]
#             # Fetch schema details for each table
#             cursor.execute(f"PRAGMA table_info({table_name});")
#             schema[table_name] = cursor.fetchall()
            
#     return schema

# # Extract the schema
# db_schema = get_db_schema(db_path)
# db_schema


# import sqlite3
# import os
# from pathlib import Path

# # Setup paths
# BASE_DIR = Path(__file__).parent.parent.parent
# DB_PATH = BASE_DIR / "credit_reports.db"

# def get_db_schema():
#     """Get database schema with error handling"""
#     try:
#         if not DB_PATH.exists():
#             raise FileNotFoundError(f"Database not found at: {DB_PATH}")
            
#         with sqlite3.connect(DB_PATH) as conn:
#             cursor = conn.cursor()
            
#             # Fetch all table names
#             cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#             tables = cursor.fetchall()
            
#             schema = {}
#             for table in tables:
#                 table_name = table[0]
#                 # Fetch schema details for each table
#                 cursor.execute(f"PRAGMA table_info({table_name});")
#                 columns = cursor.fetchall()
                
#                 # Fetch foreign keys
#                 cursor.execute(f"PRAGMA foreign_key_list({table_name});")
#                 foreign_keys = cursor.fetchall()
                
#                 schema[table_name] = {
#                     'columns': columns,
#                     'foreign_keys': foreign_keys
#                 }
                
#             return schema
            
#     except sqlite3.Error as e:
#         print(f"Database error: {e}")
#         return None
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# if __name__ == "__main__":
#     schema = get_db_schema()
#     if schema:
#         print("Database Schema:")
#         for table, details in schema.items():
#             print(f"\nTable: {table}")
#             print("Columns:")
#             for col in details['columns']:
#                 print(f"  {col}")
#             print("Foreign Keys:")
#             for fk in details['foreign_keys']:
#                 print(f"  {fk}")


# import sqlite3
# from pathlib import Path

# class DatabaseManager:
#     def __init__(self):
#         self.base_dir = Path(__file__).parent.parent.parent
#         self.db_path = self.base_dir / "data" / "credit_reports.db"
#         self.init_database()
#         self.verify_database()

#     def init_database(self):
#         try:
#             # Create data directory
#             self.db_path.parent.mkdir(parents=True, exist_ok=True)
            
#             with sqlite3.connect(self.db_path) as conn:
#                 cursor = conn.cursor()
#                 cursor.executescript('''
#                     CREATE TABLE IF NOT EXISTS credit_scores (
#                         id INTEGER PRIMARY KEY,
#                         status_id INTEGER,
#                         user_id INTEGER,
#                         credit_score TEXT,
#                         report_date TEXT
#                     );

#                     CREATE TABLE IF NOT EXISTS credit_history (
#                         id INTEGER PRIMARY KEY,
#                         user_id INTEGER,
#                         account_type TEXT,
#                         balance REAL,
#                         payment_status TEXT,
#                         FOREIGN KEY (user_id) REFERENCES credit_scores(user_id)
#                     );
#                 ''')
#                 print(f"Database initialized at: {self.db_path}")
#         except Exception as e:
#             print(f"Database initialization error: {e}")

#     def verify_database(self):
#         try:
#             with sqlite3.connect(self.db_path) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#                 tables = cursor.fetchall()
                
#                 print("\nDatabase Schema:")
#                 for table in tables:
#                     table_name = table[0]
#                     print(f"\nTable: {table_name}")
                    
#                     # Get columns
#                     cursor.execute(f"PRAGMA table_info({table_name});")
#                     columns = cursor.fetchall()
#                     print("Columns:")
#                     for col in columns:
#                         print(f"  {col[1]} ({col[2]})")
                    
#                     # Get foreign keys
#                     cursor.execute(f"PRAGMA foreign_key_list({table_name});")
#                     fks = cursor.fetchall()
#                     if fks:
#                         print("Foreign Keys:")
#                         for fk in fks:
#                             print(f"  References {fk[2]}({fk[3]})")
        
#         except Exception as e:
#             print(f"Database verification error: {e}")

# if __name__ == "__main__":
#     db = DatabaseManager()


import sqlite3
from pathlib import Path
# Setup paths
BASE_DIR = Path(__file__).parent.parent.parent
db_path = BASE_DIR / "credit_reports.db"

# Connect to the SQLite database
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Function to retrieve table names
def get_table_names(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [row[0] for row in cursor.fetchall()]

# Function to retrieve table schema
def get_table_schema(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    return [{"column_id": col[0], "name": col[1], "type": col[2], "not_null": bool(col[3]), 
             "default_value": col[4], "primary_key": bool(col[5])} for col in columns]

# Function to retrieve foreign key relationships
def get_foreign_keys(cursor, table_name):
    cursor.execute(f"PRAGMA foreign_key_list({table_name});")
    return cursor.fetchall()

# Extracting database structure
db_structure = {}
table_names = get_table_names(cursor)

for table in table_names:
    db_structure[table] = {
        "columns": get_table_schema(cursor, table),
        "foreign_keys": get_foreign_keys(cursor, table)
    }

# Close the connection
connection.close()

db_structure



# import sqlite3
# from pathlib import Path

# # Setup paths
# BASE_DIR = Path(__file__).parent.parent.parent
# db_path = BASE_DIR / "credit_reports.db"

# # Connect to the SQLite database
# connection = sqlite3.connect(db_path)
# cursor = connection.cursor()

# # Function to retrieve table names
# def get_table_names(cursor):
#     cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     return [row[0] for row in cursor.fetchall()]

# # Function to retrieve table schema
# def get_table_schema(cursor, table_name):
#     cursor.execute(f"PRAGMA table_info({table_name});")
#     columns = cursor.fetchall()
#     return [{"column_id": col[0], "name": col[1], "type": col[2], "not_null": bool(col[3]), 
#              "default_value": col[4], "primary_key": bool(col[5])} for col in columns]

# # Function to retrieve foreign key relationships
# def get_foreign_keys(cursor, table_name):
#     cursor.execute(f"PRAGMA foreign_key_list({table_name});")
#     return cursor.fetchall()

# # Function to fetch all rows from a table
# def get_all_rows(cursor, table_name):
#     cursor.execute(f"SELECT * FROM {table_name};")
#     columns = [description[0] for description in cursor.description]
#     rows = cursor.fetchall()
#     return [{"columns": dict(zip(columns, row))} for row in rows]

# # Extracting database structure
# db_structure = {}
# table_names = get_table_names(cursor)

# for table in table_names:
#     db_structure[table] = {
#         "columns": get_table_schema(cursor, table),
#         "foreign_keys": get_foreign_keys(cursor, table),
#         "data": get_all_rows(cursor, table)  # Fetch all rows from the table
#     }

# # Close the connection
# connection.close()
# db_structure