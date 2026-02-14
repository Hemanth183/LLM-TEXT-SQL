ALLOWED_KEYWORDS = ["select", "from", "where", "group by", "order by", "limit", "sum", "count", "avg", "max", "min","in","rank","top"]

def is_safe_sql(sql: str) -> bool:
    sql_lower = sql.lower()
    forbidden = ["delete", "update", "insert", "drop", "alter", "create"]
    if any(word in sql_lower for word in forbidden):
        return False
    if not sql_lower.strip().startswith("select"):
        return False
    return True