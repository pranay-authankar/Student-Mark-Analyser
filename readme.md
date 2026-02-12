# Student Marks Analyser

This program takes raw student data from a text file, processes it, and generates a detailed performance report.

## How it Works

1.  **Input**: Reads a raw `.txt` file containing student details (Roll No, Name, and Marks).
2.  **Processing**:
    *   Validates data to ensure correctness (checks for valid marks, unique roll numbers, etc.).
    *   Separates valid entries from invalid ones.
    *   Calculates Total, Average, Grade, and Verdict (Pass/Fail) for each student.
3.  **Output**:
    *   Displays a formatted table of results.
    *   Highlights the Top 3 students.
    *   Lists any invalid entries found in the source file.

## Usage

Simply run the script with the `students.txt` file in the same directory:

```bash
python main.py
```
