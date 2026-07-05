# Help Desk Ticket Analyzer

A Python-based reporting tool that analyzes help desk ticket data from a CSV file and generates summary reports, filtered ticket views, and visual charts.

## Features

- Loads help desk ticket data from a CSV file
- Calculates total, open, and closed tickets
- Identifies the most common issue type
- Finds the department with the most tickets
- Calculates average ticket resolution time
- Detects high-priority unresolved tickets
- Generates a text summary report
- Creates charts for tickets by issue type, department, and status
- Supports filtering by status, priority, and department

## Technologies Used

- Python
- pandas
- matplotlib
- CSV file processing

## Project Structure

```text
help-desk-ticket-analyzer/
├── data/
│   └── tickets.csv
├── reports/
│   ├── ticket_summary_report.txt
│   ├── tickets_by_issue_type.png
│   ├── tickets_by_department.png
│   └── tickets_by_status.png
├── src/
│   └── ticket_analyzer.py
├── README.md
├── requirements.txt
└── .gitignore 