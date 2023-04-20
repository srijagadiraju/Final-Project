"""
FINAL PROJECT TEST CODE
===========================
Course:   CS 5001
Semester: Spring 2023
Student:  Srija Gadiraju

The test code for my 5001 Final Project.

"""

from final_version9 import get_location, get_pain_type, check_pain, body_input

def test_get_location():
    # test a valid location
    print("Testing get_location")
    fail_count = 0
    if (get_location("     cHeSt     ") != 'chest'):
        fail_count += 1
        print("...Failed get_location('chest')")
    if (get_location("     hEad     ") != 'head'):
        fail_count += 1
        print("...Failed get_location('head')")
    if (get_location("     kidNey     ") != 'kidney'):
        fail_count += 1
        print("...Failed get_location('kidney')")
    # test for invalid function
    if (get_location("     nEcK     ") != 'This program is not equipped to diagnose neck pain.'):
        fail_count += 1
        print("...Failed get_location('neck')")
    if (fail_count < 1):
        print("....all tests passed for get_location()")
    return fail_count


def test_get_pain_type():
    # test a valid pain type
    print("Testing get_pain_type")
    fail_count = 0
    if (get_pain_type("     BURnIng     ") != 'burning'):
        fail_count += 1
        print("...Failed get_pain_type('burning')")
    if (get_pain_type("     iTChing     ") != 'itching'):
        fail_count += 1
        print("...Failed get_pain_type('itching')")
    if (get_pain_type("     sTABBing     ") != 'stabbing'):
        fail_count += 1
        print("...Failed get_pain_type('stabbing')")
    if (get_pain_type("     TINgLIng     ") != 'tingling'):
        fail_count += 1
        print("...Failed get_pain_type('tingling')")
    # test for invalid function
    if (get_pain_type("     STinGInG     ") != 'Please choose from the given options: burning, itching, stabbing, tingling.'):
        fail_count += 1
        print("...Failed get_pain_type('stinging')")
    if (fail_count < 1):
        print("....all tests passed for get_pain_type()")
    return fail_count
    
def main():
    print("Running all tests")
    fail_count = test_get_location()
    fail_count += test_get_pain_type()
    print(f"Failed {fail_count} tests")

    
if __name__ == "__main__":
    main()