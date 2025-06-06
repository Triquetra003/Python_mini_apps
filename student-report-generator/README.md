# Student Marks Report Generator

## Overview

This Python project reads student information and marks from two CSV files, merges the data, calculates each student’s percentage, determines pass/fail status, assigns ranks based on percentages, and generates a consolidated report as a CSV file.

---

## Features

- Reads student details (`students.csv`) and marks (`marks.csv`)
- Merges data based on student IDs
- Calculates percentage scores for each student
- Determines pass/fail status based on percentage threshold
- Assigns ranks to students sorted by percentage
- Error Handling for failed students' ranking system 
- Error Handling for students with same percentage/rank
- Outputs a final report CSV file (`reports.csv`)

---

## Files

- `students.csv` — Contains student IDs and names  
- `marks.csv` — Contains student IDs and marks in subjects  
- `report-generator.py` — Python script that processes data and generates the report  
- `reports.csv` — Output file with consolidated student info, percentages, pass/fail, and ranks

---

## How to Run

1. Make sure you have Python 3 installed.  
2. Place the `students.csv` and `marks.csv` files in the same folder as `report-generator.py`.  
3. Replace `<path-of-file>` with the actual path of file without replacing name of the csv files.
4. Run the script from the command line or your IDE:

   ```bash
   python report-generator.py
   ```