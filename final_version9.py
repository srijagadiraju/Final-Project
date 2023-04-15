def get_location():
    """
    Prompts patient to input location of their pain (gets the location of the pain from the patient). 
    Returns a string representing the location of the patient's pain.

    Args: 
        None

    Returns:
        str: a string representing the location of the pain.
        If not valid, returns None.
    """
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


def get_pain_type():
    """
    Prompts the patient to input their pain type. Returns a string representing the patient's pain type.
    
    Args:
        None

    Returns:
        str: a string representing the patient's pain type. The string only be "burning", "itching",
        "stabbing", "tingling."
        If not valid, returns None.
    """
    while True:
        # ask for the type of pain
        pain_type = input("What type of pain do you have (burning, itching, stabbing, tingling)? ")
        # check if the entered pain type is valid
        if pain_type.lower() not in ["burning", "itching", "stabbing", "tingling"]:
            # if not valid, print a message and continue prompting
            print("Please choose from the given options: burning, itching, stabbing, tingling.")
        else:
            # if valid, return the lowercase version of the type
            return pain_type.lower()


def check_pain(data, location, pain_type):
    """
    Checks for possible diagnoses based on inputted location and pain type.

    Args:
        data (dict): a dictionary that contains information about diagnoses based on location and pain types
        location (str): the location of the pain entered by the patient
        pain_type (str): the type of pain entered by the patient

    Returns:
        Prints out possible diagnoses for the given location and type of pain
        If no diagnosis available, prints out error message
    """
    # create a tuple of the location and pain type -- key
    pain = (location, pain_type)

    # check if there are any diagnoses for the given pain
    if pain in data:
        print("\nPossible diagnoses are:")
        # print out list of possible diagnoses for the given pain based on location
        for diagnosis in data[pain]:
            print(diagnosis)
    else:
        # if no diagnoses are found
        print(f"No diagnoses found for {pain} pain.")


def body_input(data):
    """
    This function handles the input and processing of pain information for a patient.
    
    Args:
        data (dict): A dictionary containing diagnoses data based on pain type and location.
    
    Returns:
        None
    """
    while True:
        # get the location of the pain 
        location = get_location()

        # check if location is valid
        if location is not None:
            # get pain type  
            pain_type = get_pain_type()

            # check for diagnoses based on the location and pain type
            check_pain(data, location, pain_type)

        # ask patient if they want to ask about another body part
        while True:
            another_part = input("\nWould you like to ask about another body part? (yes or no) ")
            # if they would, break function to restart 
            if another_part.lower() == "yes":
                break
            elif another_part.lower() == "no":
            # print a message to show end of program 
                print("Feel better soon!\n")
                return
            else:
            # continue printing error until correct choices are inputted 
                print("Invalid option. Please enter yes or no.\n")


def main():
     """
    Main function to run the program. Reads in data from a file, prompts the user for input on pain location and type, 
    and outputs any matching diagnoses from the dictionary.

    Returns:
        None
    """
    # initialize an empty dictionary called 'data'
data = {}

    # open the file "diagnoses.txt" and store its contents in 'data' using the 'eval' function
with open("diagnoses.txt", "r") as file:
    data = eval(file.read())

    # call the 'body_input' function with the 'data' dictionary as argument
    body_input(data)


if __name__ == "__main__":
    main()
   
   
  
            
