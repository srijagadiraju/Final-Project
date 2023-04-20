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
    # test valid locations
    print("Testing get_location")
    fail_count = 0
    locations = ['chest', 'head', 'kidney']
    if get_location() != locations:
        fail_count += 1
        print(f"...Failed get_location('{locations}')")
    else:
        return fail_count

    # test for invalid function
    if get_location() is not None:
        fail_count += 1
        print("...Failed get_location()")

    if fail_count < 1:
        print("....all tests passed for get_location()")

    return fail_count

def test_get_pain_type():
    # test valid pain types
    print("Testing get_pain_type")
    fail_count = 0
    pain_types = ['burning', 'itching', 'stabbing', 'tingling']
    if get_pain_type() != pain_types:
        fail_count += 1
        print(f"...Failed get_pain_type('{pain_types}')")

    # test for invalid function
    if get_pain_type() is not None:
        fail_count += 1
        print("...Failed get_pain_type()")

    if fail_count < 1:
        print("....all tests passed for get_pain_type()")

    return fail_count

def test_check_pain():
    # create a test dictionary with example diagnoses
    test_data = {('chest', 'tingling'): ['Diagnosis A', 'Diagnosis B'],
                 ('head', 'stabbing'): ['Diagnosis C', 'Diagnosis D'],
                 ('kidney', 'burning'): ['Diagnosis E']}

    # test for valid location and pain type
    print("Testing check_pain with valid inputs")
    check_pain(test_data, 'chest', 'tingling')
    check_pain(test_data, 'head', 'stabbing')
    check_pain(test_data, 'kidney', 'burning')

    # test for invalid location and/or pain type
    print("Testing check_pain with invalid inputs")
    check_pain(test_data, 'neck', 'burning')
    check_pain(test_data, 'kidney', 'tingling')


def test_body_input():
    # create a test dictionary with example diagnoses
    print("/nTesting body_input with valid inputs")
    test_data = {('chest', 'tingling'): ['Diagnosis A', 'Diagnosis B'],
                 ('head', 'stabbing'): ['Diagnosis C', 'Diagnosis D'],
                 ('kidney', 'burning'): ['Diagnosis E']}


def main():
    print("Running all tests")
    fail_count = test_get_location() + test_get_pain_type()
    print(f"Failed {fail_count} tests")
    test_check_pain()
    test_body_input()

if __name__ == "__main__":
    main()
