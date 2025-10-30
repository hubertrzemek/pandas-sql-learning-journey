import pyodbc
import pandas as pd

# Database connection settings
server = r'serverName'   # SQL Server name  
database = 'databaseNAme'#Database name
trusted_connection = 'yes'  # Windows Authentication

# SQL query to execute ----
query = """
SELECT TOP 10 ;
"""

try:
    #  Establish connection to SQL Server 
    conn = pyodbc.connect(
        f"Driver={{ODBC Driver 17 for SQL Server}};"
        f"Server={server};"
        f"Database={database};"
        f"Trusted_Connection={trusted_connection};"
    )

    print(" Connected to database!")

    # Execute query and load into Pandas DataFrame 
    df = pd.read_sql(query, conn)

    print(" Query result:")
    print(df)

except Exception as e:
    print(" Database connection or query error:", e)

finally:
    try:
        conn.close()
        print(" Connection closed.")
    except:
        pass
