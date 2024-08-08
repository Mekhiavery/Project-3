import re
import pandas as pd

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
