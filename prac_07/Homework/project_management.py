import csv
from datetime import datetime
from project import Project

def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)  # Skip header
            for row in reader:
                projects.append(Project(*row))
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with an empty list.")
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'),
                             project.priority, project.cost_estimate, project.completion_percentage])

def display_projects(projects):
    """Display incomplete and completed projects separately, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_completed()])
    complete = sorted([p for p in projects if p.is_completed()])
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("\nCompleted projects:")
    for project in complete:
        print(f"  {project}")

def filter_projects_by_date(projects, date_str):
    """Filter and display projects starting after a given date."""
    filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = sorted([p for p in projects if p.start_date > filter_date], key=lambda p: p.start_date)
    for project in filtered:
        print(project)

def add_project(projects):
    """Add a new project."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Completion percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))

def update_project(projects):
    """Update a project's completion percentage and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    project = projects[index]
    new_percentage = input("New Completion Percentage (leave blank to keep current): ")
    new_priority = input("New Priority (leave blank to keep current): ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)
    if new_priority:
        project.priority = int(new_priority)

def main():
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")
    while True:
        choice = input("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit\n>>> ").lower()
        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input(f"Would you like to save to {filename}? (y/n): ").lower()
            if save_choice == 'y':
                save_projects(filename, projects)
            print("Thank you for using Pythonic Project Management!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
