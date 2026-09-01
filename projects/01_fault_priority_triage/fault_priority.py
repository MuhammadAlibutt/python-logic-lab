def take_input():
    try:

        while True:
            eq_id = str(input("Enter the equipment ID: ")).strip().upper()
            if eq_id.strip() == "" or not eq_id.startswith("CV-"):
                 print("Equipment ID cannot be empty and must start with 'cv-'. Please enter a valid ID.")
            else:
                break

        while True:
            safety_critical = input("Safety Risk? (yes/no): ").strip().lower()
            if safety_critical not in ["yes", "no", "y", "n"]:
                print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                break 
            
        while True:
            is_working = input("Is the equipment working? (yes/no): ").strip().lower()
            if is_working not in ["yes", "no", "y", "n"]:
                print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                break

        while True:
            downtime = int(input("Enter the downtime/disruption in minutes: ").strip())
            if downtime < 0 :
                print("Downtime cannot be negative or exceed 1440 minutes (24 hours). Please enter a valid value.")
            else:
                break
        result = priority_triage(eq_id, safety_critical, is_working, downtime)
        return result     
    except ValueError:
        return "Invalid input. Please enter a valid value"

def priority_triage(eq_id: str, safety_critical: str, is_working: str, downtime: int)-> str:
    """
    Function to determine the priority of equipment based on user input.
    """
    if safety_critical in ["yes", 'y']:
        return f"{eq_id} | P1 | Escalate immediately"
            
    elif safety_critical in ["no", 'n'] and downtime >= 30 and is_working in ["no", 'n']:
        return f"{eq_id} | P1 | Escalate immediately"
            
    elif downtime < 30 and is_working in ["no", 'n']:
        return f"{eq_id} | P2 | Attend this shift"
            
    elif downtime >= 60 and is_working in ["yes", 'y']:
        return f"{eq_id} | P2 | Need to Attend this shift"
            
    elif 1 <= downtime <=59 and is_working in ["yes", 'y']:
        return f"{eq_id} | P3 | Schedule inspection"
            
    elif 0 <= downtime < 1 and is_working in ["yes", 'y']:
         return f"{eq_id} | P4 | Monitor "
    else:
            return f"{eq_id} | Need more Inspection | Please check the equipment"
    
        

def main():
    try:
        priority = take_input()
        print(priority)
    except Exception as e:
        print(f"An error occurred: {e}")
    except ValueError:
        print("Invalid input. Please enter a valid value.")

if __name__ == "__main__":
    main()