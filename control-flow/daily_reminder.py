def main():
    
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")
    
    match priority:
        case "high":
            if time_bound.lower() == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Focus on completing it soon.")
        case "medium":
            if time_bound.lower() == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Plan to complete it when possible.")
        case "low":
            if time_bound.lower() == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print(f"Reminder: '{task}' - Please specify a valid priority level (high/medium/low).")

    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print("🚀 Click here to tweet! 🚀")

if __name__ == "__main__":
    main()
