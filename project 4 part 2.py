import re
import pandas as pd
import cx_Oracle
import os

# Step 1: Load the Text File
file_path = 'C:/Users/mekhi/Downloads/pg51326.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Step 2: Define regex patterns for the new book
patterns = {
    'Publication Details': r'(?s)(The Project Gutenberg eBook of The Principles of Chemistry, Volume I.*?)(\*{3} START OF THE PROJECT GUTENBERG EBOOK)',
    'Table of Contents': r'(?s)(CONTENTS.*?)(INTRODUCTION)',
    'Preface': r'(?s)(PREFACE.*?)(INTRODUCTION)',
    'Introduction': r'(?s)(INTRODUCTION.*?)(CHAP\.)',
    'Chapter I': r'(?s)(CHAP\.\s*I\..*?)(CHAP\.\s*II\.)',
    'Chapter II': r'(?s)(CHAP\.\s*II\..*?)(CHAP\.\s*III\.)',
    'Chapter III': r'(?s)(CHAP\.\s*III\..*?)(CHAP\.\s*IV\.)',
    'Chapter IV': r'(?s)(CHAP\.\s*IV\..*?)(CHAP\.\s*V\.)',
    'Chapter V': r'(?s)(CHAP\.\s*V\..*?)(CHAP\.\s*VI\.)',
    'Chapter VI': r'(?s)(CHAP\.\s*VI\..*?)(CHAP\.\s*VII\.)',
    'Chapter VII': r'(?s)(CHAP\.\s*VII\..*?)(CHAP\.\s*VIII\.)',
    'Chapter VIII': r'(?s)(CHAP\.\s*VIII\..*?)(CHAP\.\s*IX\.)',
    'Chapter IX': r'(?s)(CHAP\.\s*IX\..*?)(CHAP\.\s*X\.)',
    'Chapter X': r'(?s)(CHAP\.\s*X\..*?)(CHAP\.\s*XI\.)',
    'Chapter XI': r'(?s)(CHAP\.\s*XI\..*?)(CHAP\.\s*XII\.)',
    'Chapter XII': r'(?s)(CHAP\.\s*XII\..*?)(CHAP\.\s*XIII\.)',
    'Chapter XIII': r'(?s)(CHAP\.\s*XIII\..*?)(CHAP\.\s*XIV\.)',
    'Chapter XIV': r'(?s)(CHAP\.\s*XIV\..*?)(CHAP\.\s*XV\.)',
    'Chapter XV': r'(?s)(CHAP\.\s*XV\..*?)(CHAP\.\s*XVI\.)',
    'Chapter XVI': r'(?s)(CHAP\.\s*XVI\..*?)(CHAP\.\s*XVII\.)',
    'Chapter XVII': r'(?s)(CHAP\.\s*XVII\..*?)(END OF VOLUME I)',
}

# Step 3: Extract sections
extracted_data = {}
for key, pattern in patterns.items():
    match = re.search(pattern, text)
    extracted_data[key] = match.group(1).strip() if match else None

# Step 4: Convert extracted data to pandas DataFrame
df = pd.DataFrame([extracted_data])

# Verify DataFrame content
print(df)

# Step 5: Save DataFrame to a CSV file for verification
df.to_csv('extracted_sections_pg51326.csv', index=False)

# Step 6: Set TNS_ADMIN Environment Variable
wallet_location = r"C:\Users\mekhi\Downloads\Wallet_mekhiAveryDb1"
os.environ['TNS_ADMIN'] = wallet_location

# Step 7: Database connection details
user = "Admin"
password = "Mekhiavery2004"
dsn = "mekhiaverydb1_high"

# Step 8: Connect to the Oracle database
connection = cx_Oracle.connect(
    user=user,
    password=password,
    dsn=dsn,
    encoding="UTF-8"
)

cursor = connection.cursor()

# Step 9: Update table schema if necessary
try:
    cursor.execute("ALTER TABLE literature ADD (book_title CLOB)")
    cursor.execute("ALTER TABLE literature ADD (book_author CLOB)")
    cursor.execute("ALTER TABLE literature ADD (release_date DATE)")
    cursor.execute("ALTER TABLE literature ADD (language VARCHAR2(50))")
    connection.commit()
    print("Table 'literature' updated successfully.")
except cx_Oracle.DatabaseError as e:
    error, = e.args
    if error.code == 1430:
        print("Columns already exist in 'literature' table.")
    else:
        print("Error updating table:")
        print(error.message)

# Step 10: Insert data into literature table for the new book
insert_sql = """
INSERT INTO literature (
    publication_details, table_of_contents, preface,
    chapter_1, chapter_2, chapter_3, chapter_4, chapter_5, chapter_6, chapter_7,
    chapter_8, chapter_9, chapter_10, chapter_11, chapter_12, chapter_13,
    chapter_14, chapter_15, chapter_16, chapter_17,
    book_title, book_author, release_date, language
) VALUES (
    :1, :2, :3,
    :4, :5, :6, :7, :8, :9, :10,
    :11, :12, :13, :14, :15, :16,
    :17, :18, :19, :20,
    :21, :22, TO_DATE(:23, 'YYYY-MM-DD'), :24
)
"""

try:
    cursor.execute(insert_sql, (
        df.at[0, 'Publication Details'],
        df.at[0, 'Table of Contents'],
        df.at[0, 'Preface'],
        df.at[0, 'Chapter I'],
        df.at[0, 'Chapter II'],
        df.at[0, 'Chapter III'],
        df.at[0, 'Chapter IV'],
        df.at[0, 'Chapter V'],
        df.at[0, 'Chapter VI'],
        df.at[0, 'Chapter VII'],
        df.at[0, 'Chapter VIII'],
        df.at[0, 'Chapter IX'],
        df.at[0, 'Chapter X'],
        df.at[0, 'Chapter XI'],
        df.at[0, 'Chapter XII'],
        df.at[0, 'Chapter XIII'],
        df.at[0, 'Chapter XIV'],
        df.at[0, 'Chapter XV'],
        df.at[0, 'Chapter XVI'],
        df.at[0, 'Chapter XVII'],
        "The Principles of Chemistry, Volume I",
        "Dmitry Ivanovich Mendeleyev",
        "2016-02-29",
        "English"
    ))
    connection.commit()
    print("Data inserted successfully.")
except cx_Oracle.DatabaseError as e:
    error, = e.args
    print("Error inserting data:")
    print(error.message)
finally:
    cursor.close()
    connection.close()

# Step 11: Retrieve and verify table of contents from the database
connection = cx_Oracle.connect(
    user=user,
    password=password,
    dsn=dsn,
    encoding="UTF-8"
)

cursor = connection.cursor()

query = """
SELECT book_title, table_of_contents FROM literature
"""

try:
    cursor.execute(query)
    rows = cursor.fetchall()
    
    for row in rows:
        if row[0] == 'The Principles of Chemistry, Volume I':
            print(row[1])
except cx_Oracle.DatabaseError as e:
    error, = e.args
    print("Error querying data:")
    print(error.message)
finally:
    cursor.close()
    connection.close()
