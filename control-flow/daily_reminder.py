# daily_reminder.py

# Function to prompt the user for task details and provide a customized reminder
def main():
    # Prompt for task description
    task = input("Enter your task: ")

    # Prompt for task priority
    priority = input("Priority (high/medium/low): ").lower()

    # Prompt for time-bound status
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Customized reminder message based on priority and time sensitivity
    reminder = f"Reminder: '{task}' is a {priority} priority task"

    match priority:
        case "high":
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += " that should be completed as soon as possible."
        case "medium":
            if time_bound == "yes":
                reminder += " that should be completed by the end of the day."
            else:
                reminder += " that can be completed within the next few days."
        case "low":
            if time_bound == "yes":
                reminder += " that should be completed when you have the time."
            else:
                reminder += " that can be done at your leisure."
        case _:
            reminder = "Invalid priority level entered."

    # Print the reminder
    print(reminder)

# Run the main function
if __name__ == "__main__":
    main()
