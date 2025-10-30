import pyodbc
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    filename= "app.log",
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Starting database connection script.")

# Database connection settings
server = r'serverName'   # SQL Server name
database = 'databaseNAme'#Database name
trusted_connection = 'yes'  # Windows Authentication

# SQL query to execute ----
query = " SELECT TOP 10 FROM TABLE_NAME ; "

try:
    #  Connect to SQL Server 
    conn = pyodbc.connect(
        f"Driver={{ODBC Driver 17 for SQL Server}};"
        f"Server={server};"
        f"Database={database};"
        f"Trusted_Connection={trusted_connection};"
    )

    logging.info("Connected to database.")

    # Execute query and load into Pandas DataFrame 
    df = pd.read_sql(query, conn)

    logging.info("Query executed successfully.")
    logging.info(f"Query result:\n{df}")

except Exception as e:
    logging.error("Database connection or query error:", exc_info=True) 
finally:
    try:
        conn.close()
        logging.info("Connection closed.")
    except:
        logging.warning("Could not close the connection")
        pass