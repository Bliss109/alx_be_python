# daily_reminder.py

# Prompt for task description
task = input("Enter your task: ")

# Prompt for priority with validation
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Please enter a valid priority: high, medium, or low.")

# Prompt for time-bound status with validation
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    print("Please answer with yes or no.")

# Output based on priority and time sensitivity
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
