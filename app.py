import streamlit as st
import os
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv
from groq import Groq
load_dotenv() 

client = Groq(
    api_key=os.getenv("QROQ_API")
)

def get_groq_response(question, prompt):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content

## retrieve query from sql database
def read_sql_query(sql,db):
  conn = sqlite3.connect(db)
  cur=conn.cursor()
  cur.execute(sql)
  rows=cur.fetchall()
  conn.commit()
  conn.close()
  for row in rows :
    print(row)
  return rows

prompt = """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION and MARKS.

    For example,

    Example 1 - How many entries of records are present?
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;

    Example 2 - Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT
    where CLASS="Data Science";

    also the sql code should not have ``` in beginning or end and sql word in output
    """

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_groq_response(question, prompt)
    print(response)

    data = read_sql_query(response, "student.db")

    st.subheader("The Response is")

    for row in data:
        print(row)
        st.write(row)