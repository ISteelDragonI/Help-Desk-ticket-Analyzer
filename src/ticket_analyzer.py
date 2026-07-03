import pandas as pd
import matplotlib.pyplot as plt

def load_ticket_data(file_path):
    """
    Loads help desk ticket data from a CSV file.
    
    Parameters: file_path: The path to the CSV file.
    
    Returns: A pandas Datframe containing the ticket data.
    """

    try:
        tickets = pd.read_csv(file_path)
        return tickets
    except FileNotFoundError:
        print("Error: Ticket data file was not found.")
        return None
    

def display_basic_summary(tickets):
    """
    Displays basic summary information about the ticket data
    """
    report_lines = generate_summary_report(tickets)

    print()

    for line in report_lines:
        print(line)

def display_tickets_by_issue_type(tickets):
    """
    Displays the number of tickets for each issue type.
    """
    print("\n==== Tickets by Issue Type ====")

    issue_counts = tickets["issue_type"].value_counts()
    for issue_type, count in issue_counts.items():
        print(f"{issue_type}: {count}")

def display_tickets_by_department(tickets):
    """
    Displays the number of tickets for each department.
    """
    print("\n==== Tickets by Department ====")

    department_counts = tickets["department"].value_counts()
    for department, count in department_counts.items():
        print(f"{department}: {count}")

def generate_summary_report(tickets):
    """
    Creates a list of summary report lins from the ticket data.
    
    Returning the report as a list makes it reusable:
    - We can print it to the terminal.
    - We can save it to a file.
    """
    total_tickets = len(tickets)

    open_tickets = len(tickets[tickets["status"].str.lower() == "open"])
    closed_tickets = len(tickets[tickets["status"].str.lower() == "closed"])

    most_common_issue = tickets["issue_type"].mode()[0]
    department_with_most_tickets = tickets["department"].mode()[0]

    average_resolution_time = tickets["resolution_time_hours"].mean()

    high_priority_open = tickets [
        (tickets["priority"].str.lower() == "high") &
        (tickets["status"].str.lower() == "open")
    ]

    report_lines = [
        "==== Help Desk Ticket Summary ====",
        f"Total tickets: {total_tickets}",
        f"Open tickets: {open_tickets}",
        f"Closed tickets: {closed_tickets}",
        f"Most common issue type: {most_common_issue}",
        f"Department with most tickets: {department_with_most_tickets}",
        f"Average resolution time: {average_resolution_time:.2f} hours",
        f"High priority unresolved tickets {len(high_priority_open)}"
    ]

    return report_lines

def save_report_to_file(tickets, output_path):
    """
    Saves the ticket summaryt report to a text file.
    
    Parameters:
        tickets: The pandas DataFrame containing ticket data.
        output_path: The path where the report should be saved.
    """
    report_lines = generate_summary_report(tickets)

    try:
        with open(output_path, "w") as report_file:
            for line in report_lines:
                report_file.write(line + "\n")

        print(f"\nReport saved to {output_path}")

    except FileNotFoundError:
        print("Error: Reports folder was not found.")

def create_issue_type_chart(tickets, output_path):
    """
    Creates and saves a bar chart showing number of tickets by issue type.
    """
    issue_counts = tickets["issue_type"].value_counts()

    plt.figure(figsize=(8, 5))
    issue_counts.plot(kind="bar")

    plt.title("Tickets by Issue Type")
    plt.xlabel("Issue type")
    plt.ylabel("Number of Tickets")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()

    print(f"Issue type chart saved to {output_path}")

def create_department_chart(tickets, output_path):
    """
    Creates and saves a bar chart showing the number of tickets by department.
    """
    department_counts = tickets["department"].value_counts()

    plt.figure(figsize=(8, 5))
    department_counts.plot(kind="bar")

    plt.title("Tickets by Department")
    plt.xlabel("Department")
    plt.ylabel("Number of Tickets")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()

    print(f"Department chart saved to {output_path}")

def create_status_chart(tickets, output_path):
    """
    Creates and saves a bar chart showing the number of tickets by status.
    """
    status_counts = tickets["status"].value_counts()

    plt.figure(figsize=(6, 4))
    status_counts.plot(kind="bar")

    plt.title("Tickets by Status")
    plt.xlabel("Status")
    plt.ylabel("Number of Tickets")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()

    print(f"Status chart saved to {output_path}")

def create_all_charts(tickets):
    """
    Creates all chart reports and saves them to the reports folder.
    """
    create_issue_type_chart(tickets, "reports/tickets_by_issue_type.png")
    create_department_chart(tickets, "reports/tickets_by_department.png")
    create_status_chart(tickets, "reports/tickets_by_status.png")

def main():
    file_path = "data/tickets.csv"
    output_path = "reports/ticket_summary_report.txt"

    tickets = load_ticket_data(file_path)

    if tickets is None:
        return
    
    display_basic_summary(tickets)
    display_tickets_by_issue_type(tickets)
    display_tickets_by_department(tickets)

    save_report_to_file(tickets, output_path)

    create_all_charts(tickets)

if __name__ == "__main__":
    main()