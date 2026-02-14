from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_SQL_SERVER = os.getenv("AZURE_SQL_SERVER")
AZURE_SQL_DATABASE = os.getenv("AZURE_SQL_DATABASE")
AZURE_SQL_USER = os.getenv("AZURE_SQL_USER")
AZURE_SQL_PASSWORD = os.getenv("AZURE_SQL_PASSWORD")
AZURE_SQL_DRIVER = os.getenv("AZURE_SQL_DRIVER")
