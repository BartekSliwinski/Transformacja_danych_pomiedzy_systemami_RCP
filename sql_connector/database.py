from sqlalchemy import create_engine, text
import urllib

SERVER = 'THINKPAD-BARTEK\\SQLEXPRESS'
DATABASE = "rcp_system"
DRIVER = "ODBC Driver 18 for SQL Server"

params = urllib.parse.quote_plus(
    f"DRIVER={{{DRIVER}}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

connection_string = f"mssql+pyodbc:///?odbc_connect={params}"
engine = create_engine(connection_string)

try:
    engine.connect()
    print("Yay!")
except Exception as e:
    print("Couldn't connect to the database. Error:")
    print(e)