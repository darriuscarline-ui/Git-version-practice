
"""Module 6: Individual Git and GitHub Practice.

Run this program to demonstrate basic Git and GitHub concepts.
No outside packages are required.
"""


def show_project_info():
    """Display basic information about this version-control exercise."""
    project_name = "Python Version Control Project"
    version = "2.0"

    print(f"Project: {project_name}")
    print(f"Version: {version}")
    print("Git helps track changes in a software project.")


def show_git_workflow():
    """Print the basic sequence used in this exercise."""
    steps = [
        "1. Edit and save your Python file.",
        "2. Stage your changes with git add.",
        "3. Record a local commit with git commit.",
        "4. Upload your commit to GitHub with git push.",
    ]

    for step in steps:
        print(step)


def main():
    """Run the project information and Git workflow examples."""
    show_project_info()
    print()
    show_git_workflow()
    print()

    # Explain why tracking changes with Git is useful.
    print("Git is useful because it saves a history of code changes.")

    # Explain the difference between git commit and git push.
    print("Git commit saves changes locally, while git push uploads them to GitHub.")


if __name__ == "__main__":
    main()
