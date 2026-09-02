
def ask_yes_no(user_input: str) -> bool:
    """
    Normalize user input to a standard format.
    """
    while True:
            try:
                input_string = input(f"{user_input}: ").strip().lower()
                if input_string not in ["yes", "no", "y", "n"]:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    continue
                else:
                    if input_string in ['yes', 'y']:
                        input_string = True
                        break
                    else:
                        input_string = False
                        break
            except ValueError:
                print("Invalid input.")
                continue
    return input_string

def Report(eq_id: str, piority_id:str)-> str:
    
    if piority_id == "P1":
        return f"{eq_id} | P1 | Escalate immediately"
    elif piority_id == "P2":
        return f"{eq_id} | P2 | Attend this shift"
    elif piority_id == "P3":
        return f"{eq_id} | P3 | Schedule inspection"
    elif piority_id == "P4":
        return f"{eq_id} | P4 | Monitor"
    else:
        return f"{eq_id} | Unclassified | Please check manually"

def take_input():
    while True:
        try:
            eq_id = input("Enter the equipment ID: ").strip().upper()
            if eq_id == "":
                print("Equipment ID cannot be empty. Please enter a valid ID.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid equipment ID.")
            continue
        break
    
    safety_risk = ask_yes_no("safety risk? (yes/no)")
    
    stop = ask_yes_no("Equipment Stopped? (yes/no)")

    while True:
        try:
            downtime = int(input("Enter the downtime/disruption in minutes: ").strip())
            if downtime < 0:
                print("Downtime cannot be negative. Please enter a valid value.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer for downtime.")
            continue
        break
    return priority_triage(eq_id, safety_risk, stop, downtime)  

def priority_triage(eq_id: str, safety_risk: bool, stop: bool, downtime: int)-> str:
    """
    Function to determine the priority of equipment based on user input.
    """
    if safety_risk:
        return Report(eq_id= eq_id, piority_id="P1")
            
    elif not safety_risk and downtime >= 30 and stop:
        return Report( eq_id=eq_id , piority_id="P1")
            
    elif downtime < 30 and stop:
        return Report(eq_id=eq_id, piority_id="P2")
            
    elif downtime >= 60 and not stop:
        return Report(eq_id=eq_id , piority_id="P2")
    
    elif downtime == 0 and not stop:
             return Report(eq_id=eq_id, piority_id="P4") 
              
    elif downtime < 60  and not stop:
        return Report(eq_id=eq_id , piority_id= "P3")
    else:
        return Report(eq_id=eq_id, piority_id="UNKNOWN")
        

def main():
    priority = take_input()
    print(priority)

if __name__ == "__main__":
    main()