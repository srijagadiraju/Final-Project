# gets the location of the pain from the user
def get_location():
    # current body parts with diagnoses (chose the most prevalent ones to test)
    body_parts = ["chest", "kidney", "head"]

    while True:
        # ask for the location of patient's pain
        location = input("Where is your pain located? ")
        # check if the entered location is valid
        if location.lower() not in body_parts:
            # if not valid, print a message and return None
            print(f"This program is not equipped to diagnose {location} pain.")
            return None
        else:
            # if valid, return the lowercase version of the location (stored to form tuple -- key in dictionary)
            return location.lower()

# get the type of pain from the user
def get_pain_type():
    while True:
        # ask for the type of pain
        pain_type = input("What type of pain do you have (burning, itching, stabbing, tingling)? ")
        # check if the entered pain type is valid
        if pain_type.lower() not in ["burning", "itching", "stabbing", "tingling"]:
            # if not valid, print a message and continue prompting
            print("Please choose from the given options: burning, itching, stabbing, tingling.")
        else:
            # If valid, return the lowercase version of the type
            return pain_type.lower()

# check for diagnoses based on location and pain type
def check_pain(data, location, pain_type):
    # Create a tuple of the location and pain type
    pain = (location, pain_type)

    # check if there are any diagnoses for the given pain
    if pain in data:
        print("\nPossible diagnoses are:")
        # print out list of possible diagnoses for the given pain based on location
        for diagnosis in data[pain]:
            print(diagnosis)
    else:
        # If no diagnoses found, print a message
        print(f"No diagnoses found for {pain} pain.")

# function to handle input and processing of pain information
def body_input(data):
    while True:
        # get the location of the pain from the user
        location = get_location()
        # if location is not valid, prompt user if they want to ask about another body part
        if location is None:
            while True:
                # ask if they want to get information about another body part 
                another_part = input("Would you like to ask about another body part? (yes or no) ")
                if another_part.lower() == "yes":
                    break
                elif another_part.lower() == "no":
                    print("Feel better soon!\n")
                    return
                else:
                    print("Invalid option. Please enter yes or no.\n")
            continue

        # get pain type from the user
        pain_type = get_pain_type()

        # Check for diagnoses based on the location and type of pain
        check_pain(data, location, pain_type)

        while True:
            # Prompt user if they want to ask about another body part
            another_part = input("\nWould you like to ask about another body part? (yes or no) ")
            if another_part.lower() == "yes":
                break
            elif another_part.lower() == "no":
                print("Feel better soon!\n")
                return
            else:
                print("Invalid option. Please enter yes or no.\n")
            continue


# Main function to read in the data from a file and call the body_input function
def main():
    # Initialize an empty dictionary called 'data'
    data = {}

    # Open the file "diagnoses.txt" in read mode, and store its contents in 'data' using the 'eval' function
    with open("diagnoses.txt", "r") as file:
        data = eval(file.read())

    # Call the 'body_input' function with the 'data' dictionary as argument
    body_input(data)

# Check if this module is being run as the main program
if __name__ == "__main__":
    # If it is, call the 'main' function
    main()
   