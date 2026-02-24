import pdfplumber
import pandas as pd
import re

pdf_path = r"C:\Users\sanjay\downloads\III YEAR.pdf"

subjects = [
    "20AD501",
    "20AD502",
    "20AD503",
    "20AD504",
    "20MC002",
    "20AD505L",
    "20AD506L",
    "20EEC501L",
]

records = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages[:4]:  # pages with student data
        text = page.extract_text()
        if not text:
            continue

        for line in text.split("\n"):
            tokens = line.split()

            # Must start with S.No and Register No
            if len(tokens) < 20:
                continue
            if not tokens[0].isdigit():
                continue
            if not re.fullmatch(r"\d{12}", tokens[1]):
                continue

            reg_no = tokens[1]

            # --- Work from the RIGHT ---
            # Last tokens look like: PASS 0 8.316 0
            sgpa = tokens[-2]

            # Before that: 8 × (GRD GPA)
            # So total GRD/GPA tokens = 16
            grade_block = tokens[-(16 + 4):-4]

            grades = grade_block[::2]  # take GRD only

            record = {"Register No": reg_no}
            for sub, grd in zip(subjects, grades):
                record[sub] = grd

            record["SGPA"] = sgpa
            records.append(record)

df = pd.DataFrame(records)

df = df[
    ["Register No"]
    + subjects
    + ["SGPA"]
]

df.to_excel("Final_Grades_Correct.xlsx", index=False)

print("✅ Correctly extracted students:", len(df))
