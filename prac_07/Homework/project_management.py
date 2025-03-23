import csv
from datetime import datetime
from project import Project


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip header
        for row in reader:
            projects.append(Project(*row))
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
    """Display projects, separating incomplete and completed ones."""
    incomplete = sorted([p for p in projects if not p.is_completed()])
    completed = sorted([p for p in projects if p.is_completed()])

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects, date_str):
    """Filter projects that start after a given date."""
    date = datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = sorted([p for p in projects if p.start_date > date], key=lambda p: p.start_date)
    for project in filtered:
        print(project)


def add_new_project(projects):
    """Add a new project based on user input."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: ")
    completion = input("Completion percentage: ")
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    """Update an existing project's completion and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)

    new_completion = input("New Percentage: ")
    if new_completion:
        project.completion_percentage = int(new_completion)

    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)


def main():
    """Main menu loop."""
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    while True:
        choice = input(
            "\n(L)oad projects, (S)ave projects, (D)isplay projects, (F)ilter projects, (A)dd, (U)pdate, (Q)uit: ").lower()
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
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input(f"Would you like to save to {filename}? (y/n): ").lower() == 'y':
                save_projects(filename, projects)
            print("Thank you for using Project Management!")
            break


if __name__ == "__main__":
    main()

