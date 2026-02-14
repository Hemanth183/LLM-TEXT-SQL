import pyodbc
from config import AZURE_SQL_SERVER, AZURE_SQL_DATABASE, AZURE_SQL_USER, AZURE_SQL_PASSWORD, AZURE_SQL_DRIVER

def get_connection():
    conn_str = (
    f"DRIVER={AZURE_SQL_DRIVER};"
    f"SERVER={AZURE_SQL_SERVER};"
    f"DATABASE={AZURE_SQL_DATABASE};"
    f"UID={AZURE_SQL_USER};"
    f"PWD={AZURE_SQL_PASSWORD};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)
    conn = pyodbc.connect(conn_str)
    return conn

def execute_query(sql: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    cursor.close()
    conn.close()
    return result