import streamlit as st
from gemini_service import generate_sql
from sql_validator import is_safe_sql
from db import execute_query

st.title("💬 Receipt Analytics with Gemini")

user_id = st.number_input("Enter your User ID", min_value=1, step=1)
question = st.text_input("Your Question")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question!")
    else:
        with st.spinner("Generating answer..."):
            # Step 1: Generate SQL using Gemini
            sql_query = generate_sql(f"user_id={user_id}, question={question}")
            sql = sql_query.replace("`","")
            sql1 = sql.replace("sql","")
            

            # Step 2: Validate SQL
            if not is_safe_sql(sql1):
                st.error("Generated SQL is not safe. Cannot execute.")
            else:
                # Step 3: Execute SQL
                results = execute_query(sql1)

                # Step 4: Display SQL and results
                st.subheader("Generated SQL")
                st.code(sql1)

                st.subheader("Results")
                if not results:
                    st.info("No data found.")
                else:
                    import pandas as pd
                    df = pd.DataFrame(results)
                    st.dataframe(df)