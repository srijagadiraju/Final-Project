def body_input(diagnoses):
    body_parts = ["chest"]

    while True:
        location = input("Where is your pain located? ")
        if location.lower() not in body_parts:
            print(f"This program is not equipped to diagnose {location} pain.")
            another_part = input("Would you like to input another body part? (yes or no) ")
            if another_part.lower() == "yes":
                continue
                location = input("Where is your pain located? ")
            else:
                break

        pain_type = input("What type of pain do you have (burning, itching, stabbing, tingling)? ")
        if pain_type.lower() not in ["burning", "itching", "stabbing", "tingling"]:
            print("Invalid pain type.")
            continue

        pain = (location, pain_type)

        if pain in diagnoses:
            print("\nPossible diagnoses are:")
            for diagnosis in diagnoses[pain]:
                print(diagnosis)
        else:
            print("No diagnoses found for the given pain type.")

        another_part = input("\n\nWould you like to input another body part? (yes or no) ")
        if another_part.lower() == "yes":
            continue
            location = input("Where is your pain located? ")
        else:
            break


def main():
    # Import diagnoses from diagnoses.txt
    #with open("diagnoses.txt", "r") as f:
        #data = eval(f.read())
    with open("diagnoses.txt", "r") as f:
        data_2 = eval(f.read())

    body_input(data_2)


if __name__ == "__main__":
    main()
