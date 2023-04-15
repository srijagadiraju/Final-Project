def body_input(data):
    data = data
    body_parts = ["chest", "kidney", "head"]

    while True:
        location = input("Where is your pain located? ")
        if location.lower() not in body_parts:
            print(f"This program is not equipped to diagnose {location} pain.")
            while True:
                another_part = input("Would you like to ask about another body part? (yes or no) ")
                if another_part.lower() == "yes":
                    break
                elif another_part.lower() == "no":
                    print("Feel better soon!\n")
                    return
                else:
                    print("Invalid option. Please enter yes or no.\n")
            
            continue

        pain_type = input("What type of pain do you have (burning, itching, stabbing, tingling)? ")
        if pain_type.lower() not in ["burning", "itching", "stabbing", "tingling"]:
            print("Please choose from the given options: burning, itching, stabbing, tingling.")
            continue

        pain = (location, pain_type)

        if pain in data:
            print("\nPossible diagnoses are:")
            for diagnosis in data[pain]:
                print(diagnosis)
        else:
            print(f"No diagnoses found for {pain} pain.")
        
        while True:
            another_part = input("\nWould you like to ask about another body part? (yes or no) ")
            if another_part.lower() == "yes":
                    break
            elif another_part.lower() == "no":
                print("We hope you feel better soon!\n")
                return
            else:
                print("Invalid option. Please enter yes or no.\n")
            continue


def main():
    data = {}
    with open("diagnoses.txt", "r") as file:
        data = eval(file.read())
    body_input(data)
    

if __name__ == "__main__":
    main()