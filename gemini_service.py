import os
import google.genai as genai
from config import GEMINI_API_KEY



# Load environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize client
client = genai.Client(api_key=GEMINI_API_KEY,vertexai=False)

# You can choose a Gemini model that fits best (like "gemini‑2.5‑flash")
MODEL = "gemini-2.5-flash"

SCHEMA = """

Table: receipts
columns: receipt_id, receipt_type, merchant_name, country, street_address, city, state, subtotal, tip, total, transaction_date, transaction_time, currency_code, created_at

Table: receiptitems
columns: receipt_item_id, receipt_id, item, quantity, total_price

Foreign keys:
receiptitems.receipt_id -> receipts.receipt_id
"""

SYSTEM_PROMPT = f"""
You are a SQL generator and you are using azure sql database and folllow the rules that azure sql has.
Use only SELECT queries.
Do NOT generate DELETE, UPDATE, INSERT, DROP.
If the sql query contains limit use top instead of limit
Use only the schema below.
Return ONLY SQL query starting from select only.
Schema:
{SCHEMA}
"""

def generate_sql(user_question: str) -> str:
    prompt = SYSTEM_PROMPT + "\nUser: " + user_question
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    # Gemini returns text in .text
    return response.text.strip()