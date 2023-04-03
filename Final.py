def body_input():
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

        if pain == ("chest", "burning"):
            print("\nPossible diagnoses are:\nHeartburn\nGastrointestinal (GI) issues\nSymptom of a panic attack\nAnxiety\nHeart attack\nAortic dissection\nIf symptoms persist for longer than 3 days or if they worsen, please seek medical attention from a licensed professional. For more details, please visit https://www.mayoclinic.org/diseases-conditions/heartburn/in-depth/heartburn-gerd/art-20046483")
        elif pain == ("chest", "itching"):
            print("\nPossible diagnoses are:\nContact dermatitis (contact allergies)\nAcne vulgaris – when hair follicles are clogged with sebum and dead skin cells\nPsoriasis\nPruritis\nShingles\nIf symptoms persist for longer than 3 days or if they worsen, please seek medical attention from a licensed professional. For more details, please visit https://www.healthline.com/health/itchy-chest#The-takeaway")
        elif pain == ("chest", "stabbing"):
            print("\nPossible diagnoses are:\nHeart attack\nPericarditis – inflammation of the membranes surrounding the heart\nAngina – due to reduced blood flow to the heart\nPrecordial catch syndrome – can cause pain when shifting positions\nPanic attack\nFractures or strains\nPleuritis – inflammation of the lining around the chest and lungs\nCoronary artery disease\nIf symptoms persist for longer than 3 days or if they worsen, please seek medical attention from a licensed professional. For more details, please visit https://my.clevelandclinic.org/health/symptoms/21209-chest-pain")
        elif pain == ("chest", "tingling"):
            print("\nPossible diagnoses are:\nAngina – when heart does not get enough blood and oxygen, leading to ischemia\nPanic attack\nParasthesia\nStroke\nThoracic outlet syndrome\nIf symptoms persist for longer than 3 days or if they worsen, please seek medical attention from a licensed professional. For more details, please visit https://www.healthline.com/health/numbness-in-chest#when-to-see-your-doctor")
        another_part = input("\n\nWould you like to input another body part? (yes or no) ")
        if another_part.lower() == "yes":
            continue
            location = input("Where is your pain located? ")
        else:
            break


def main():
    body_input()


if __name__ == "__main__":
    main()

        
