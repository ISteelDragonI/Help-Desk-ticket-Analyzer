import pandas as pd

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
    total_tickets = len(tickets)

    open_tickets = len(tickets[tickets["status"].str.lower() == "open"])
    closed_tickets = len(tickets[tickets["status"].str.lower() == "closed"])

    most_common_issue = tickets["issue_type"].mode()[0]
    department_with_most_tickets = tickets["department"].mode()[0]

    average_resolution_time = tickets["resolution_time_hours"].mean()

    high_priority_open = tickets[
        (tickets["priority"].str.lower() == "high") &
        (tickets["status"].str.lower() == "open")
    ]

    print("\n==== Help Desk Ticket Summary ====")
    print(f"Total tickets: {total_tickets}")
    print(f"Open tickets: {open_tickets}")
    print(f"Closed tickets: {closed_tickets}")
    print(f"Most common issue type: {most_common_issue}")
    print(f"Department with most tickets: {department_with_most_tickets}")
    print(f"Average resolution time: {average_resolution_time:.2f} hours")
    print(f"High priority unresolved tickets: {len(high_priority_open)}")

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

def main():
    file_path = "data/tickets.csv"

    tickets = load_ticket_data(file_path)

    if tickets is None:
        return
    
    display_basic_summary(tickets)
    display_tickets_by_issue_type(tickets)
    display_tickets_by_department(tickets)

if __name__ == "__main__":
    main()