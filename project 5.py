import re
import pandas as pd

# Load the text file
file_path = 'C:/Users/mekhi/Downloads/pg30155.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Define regex patterns
patterns = {
    'Publication Details': r'(?s)(The Project Gutenberg eBook of Relativity: The Special and General Theory.*?)(\*{3} START OF THE PROJECT GUTENBERG EBOOK)',
    'Table of Contents': r'(?s)(Contents.*?)(PREFACE)',
    'Preface': r'(?s)(PREFACE.*?)(PART I: THE SPECIAL THEORY OF RELATIVITY)',
    'Chapter I': r'(?s)(I\. PHYSICAL MEANING OF GEOMETRICAL PROPOSITIONS.*?)(II\. THE SYSTEM OF CO-ORDINATES)',
    'Chapter II': r'(?s)(II\. THE SYSTEM OF CO-ORDINATES.*?)(III\. SPACE AND TIME IN CLASSICAL MECHANICS)',
    'Chapter III': r'(?s)(III\. SPACE AND TIME IN CLASSICAL MECHANICS.*?)(IV\. THE GALILEIAN SYSTEM OF CO-ORDINATES)',
    'Chapter IV': r'(?s)(IV\. THE GALILEIAN SYSTEM OF CO-ORDINATES.*?)(V\. THE PRINCIPLE OF RELATIVITY \(IN THE RESTRICTED SENSE\))',
    'Chapter V': r'(?s)(V\. THE PRINCIPLE OF RELATIVITY \(IN THE RESTRICTED SENSE\).*?)(VI\. THE THEOREM OF THE ADDITION OF VELOCITIES EMPLOYED IN CLASSICAL MECHANICS)',
    'Chapter VI': r'(?s)(VI\. THE THEOREM OF THE ADDITION OF VELOCITIES EMPLOYED IN CLASSICAL MECHANICS.*?)(VII\. THE APPARENT INCOMPATIBILITY OF THE LAW OF PROPAGATION OF LIGHT WITH THE PRINCIPLE OF RELATIVITY)',
    'Chapter VII': r'(?s)(VII\. THE APPARENT INCOMPATIBILITY OF THE LAW OF PROPAGATION OF LIGHT WITH THE PRINCIPLE OF RELATIVITY.*?)(VIII\. ON THE IDEA OF TIME IN PHYSICS)',
    'Chapter VIII': r'(?s)(VIII\. ON THE IDEA OF TIME IN PHYSICS.*?)(IX\. THE RELATIVITY OF SIMULTANEITY)',
    'Chapter IX': r'(?s)(IX\. THE RELATIVITY OF SIMULTANEITY.*?)(X\. ON THE RELATIVITY OF THE CONCEPTION OF DISTANCE)',
    'Chapter X': r'(?s)(X\. ON THE RELATIVITY OF THE CONCEPTION OF DISTANCE.*?)(XI\. THE LORENTZ TRANSFORMATION)',
    'Chapter XI': r'(?s)(XI\. THE LORENTZ TRANSFORMATION.*?)(XII\. THE BEHAVIOUR OF MEASURING-RODS AND CLOCKS IN MOTION)',
    'Chapter XII': r'(?s)(XII\. THE BEHAVIOUR OF MEASURING-RODS AND CLOCKS IN MOTION.*?)(XIII\. THEOREM OF THE ADDITION OF VELOCITIES. THE EXPERIMENT OF FIZEAU)',
    'Chapter XIII': r'(?s)(XIII\. THEOREM OF THE ADDITION OF VELOCITIES. THE EXPERIMENT OF FIZEAU.*?)(XIV\. THE HEURISTIC VALUE OF THE THEORY OF RELATIVITY)',
    'Chapter XIV': r'(?s)(XIV\. THE HEURISTIC VALUE OF THE THEORY OF RELATIVITY.*?)(XV\. GENERAL RESULTS OF THE THEORY)',
    'Chapter XV': r'(?s)(XV\. GENERAL RESULTS OF THE THEORY.*?)(XVI\. EXPERIENCE AND THE SPECIAL THEORY OF RELATIVITY)',
    'Chapter XVI': r'(?s)(XVI\. EXPERIENCE AND THE SPECIAL THEORY OF RELATIVITY.*?)(XVII\. MINKOWSKI’S FOUR-DIMENSIONAL SPACE)',
    'Chapter XVII': r'(?s)(XVII\. MINKOWSKI’S FOUR-DIMENSIONAL SPACE.*?)(PART II: THE GENERAL THEORY OF RELATIVITY)'
}

# Extract sections
extracted_data = {}
for key, pattern in patterns.items():
    match = re.search(pattern, text)
    extracted_data[key] = match.group(1).strip() if match else None

# Convert extracted data to pandas DataFrame
df = pd.DataFrame([extracted_data])

# Print DataFrame content to verify
print(df)

# Save DataFrame to a CSV file for verification
df.to_csv('extracted_sections.csv', index=False)
