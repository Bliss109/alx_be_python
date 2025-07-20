# daily_reminder.py

# Get task description
task = input("Enter your task: ")

# Get priority level with input validation
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Please enter a valid priority (high/medium/low).")

# Get time-bound status with input validation
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    print("Please answer with yes or no.")

# Match-case for priority and if for time-sensitivity
match priority:
    case "high" | "medium" | "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Unexpected error occurred.")
