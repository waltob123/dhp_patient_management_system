#!/usr/bin/env python3
"""
@Author: Desmond Asiedu Asamoah
@Date: 04/Jan/2025
@Version: 1.0

This script is the entry of the application Patient Management System (PMS).
It includes the main function to run the application and also other helper functions.
"""

import re

PATIENTS_DATA = []


def generate_patient_id() -> int:
    """
    Generate a unique patient ID for each new patient

    :return: int: The patient unique identifier
    """
    return len(PATIENTS_DATA) + 1 if PATIENTS_DATA else 1


def calculate_age(date_of_birth: str) -> int:
    """
    Calculate the age of a patient from their date of birth

    :date_of_birth: str: The date of birth of the patient

    :return: int: The age of the patient
    """


def display_main_menu() -> None:
    """
    Display the main menu options

    :return: None
    """
    print("\n")
    print("Patient Management System (PMS)")
    print("<=================================================================>")
    print("Select an option from the menu below (1-6):")
    print("1. Add Patient")
    print("2. Display Patients")
    print("3. Update Patient Info")
    print("4. Delete Patient")
    print("5. Search Patient")
    print("6. Exit")


def display_patient_id_menu() -> None:
    """
    Display the patient ID menu options

    :return: None
    """
    print("\n")
    print("Enter patient ID:")
    print("<=================================================================>")


def display_and_get_patient_info() -> tuple:
    """
    Display the add patient menu options

    :return: None
    """
    print("\n")
    print("Add Patient")
    print("<=================================================================>")
    print("Enter patient details:")
    try:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        date_of_birth = input("Date of Birth (dd-mm-yyyy): ")
        hometown = input("Hometown: ")
        house_number = input("House Number: ")
        phone_number = input("Phone Number (024-400-0000): ")
    except KeyboardInterrupt:
        print("\nExiting application...")
        exit(0)

    try:
        validate_patient_date_of_birth(date_of_birth)
        validate_patient_phone_number(phone_number)
    except ValueError as e:
        print(f"\nError: {e}")
        display_and_get_patient_info()

    return first_name, last_name, date_of_birth, hometown, house_number, phone_number


def get_user_choice() -> str:
    """
    Get the user choice from the main menu

    :return: str: The user choice
    """
    try:
        user_input = input("Enter choice: ")
    except KeyboardInterrupt:
        print("\nExiting application...")
        exit(0)
    return user_input


def add_patient(**kwargs) -> None:
    """
    Add a new patient to the system

    :param kwargs: The patient details

    :return:
    """
    patient_data = {
        "patient_id": generate_patient_id(),
        "first_name": kwargs.get("first_name"),
        "last_name": kwargs.get("last_name"),
        "date_of_birth": kwargs.get("date_of_birth"),
        "hometown": kwargs.get("hometown"),
        "house_number": kwargs.get("house_number"),
        "phone_number": kwargs.get("phone_number")
    }

    PATIENTS_DATA.append(patient_data)

    print(f"\nPatient with ID {patient_data.get("patient_id")} added successfully\n")


def display_patients() -> None:
    """
    Display all patients in the system

    :return: None
    """
    print("\n")
    print("Patients")
    print("<=================================================================>")
    if PATIENTS_DATA:
        for patient in PATIENTS_DATA:
            print(patient, end="\n")
    else:
        print("No patients found")


def display_patient(patient_id: int) -> None:
    """
    Display a patient in the system

    :param patient_id: The id of the patient to display

    :return: None
    """
    patient = search_patient(patient_id)

    if patient:
        print(patient)
    else:
        print("\nPatient not found\n")


def update_patient_info(patient: dict, **kwargs) -> None:
    """
    Update patient information

    :param patient: The patient to update
    :param kwargs: The new patient data

    :return: The updated patient information
    """
    patient.update(kwargs)
    print(f"\nPatient with ID {patient.get('patient_id')} updated successfully\n")


def delete_patient(patient_id: int) -> None:
    """
    Delete a patient from the system

    :param patient_id: The id of the patient to delete

    :return: None
    """
    patient = search_patient(patient_id)

    if patient:
        PATIENTS_DATA.remove(patient)
        print(f"\nPatient with ID {patient_id} deleted successfully\n")
    else:
        print("\nPatient not found\n")


def search_patient(patient_id: int) -> dict | None:
    """
    Search for a patient in the system using binary search

    :param patient_id: The id of the patient to search for

    :return: The patient information if found, otherwise None
    """
    left = 0
    right = len(PATIENTS_DATA) - 1

    while left <= right:
        mid = (left + right) // 2

        if PATIENTS_DATA[mid].get("patient_id") == patient_id:
            return PATIENTS_DATA[mid]

        if PATIENTS_DATA[mid].get("patient_id") < patient_id:
            left = mid + 1
        else:
            right = mid - 1

    return None


def validate_patient_date_of_birth(date_of_birth: str) -> bool:
    """
    Validate the date of birth format (dd-mm-yyyy)

    :param: date_of_birth:

    :return: True if the date of birth is valid, otherwise False
    """
    date_of_birth_pattern = re.compile(r"^\d{2}-\d{2}-\d{4}$")

    if bool(date_of_birth_pattern.fullmatch(date_of_birth)):
        day, month, year = date_of_birth.split("-")
        return validate_days_of_each_month(int(day), int(month))

    raise ValueError("Invalid date of birth format, date must be in the format dd-mm-yyyy")


def validate_patient_phone_number(phone_number: str) -> bool:
    """
    Validate the phone number format (024-400-0000)

    :param: phone_number:

    :return: True if the phone number is valid, otherwise False
    """
    phone_number_pattern = re.compile(r"^\d{3}-\d{3}-\d{4}$")

    if bool(phone_number_pattern.fullmatch(phone_number)):
        return True
    raise ValueError("Invalid phone number format, phone number must be in the format 024-400-0000")


def validate_days_of_each_month(day: int, month: int) -> bool:
    """
    Validate the number of days in each month

    :param day: The day of the month:
    :param month: The month of the year:

    :return: True if the day is valid, otherwise False
    """
    if month > 12 or month < 1:
        raise ValueError("Invalid month, month must be between 01 and 12 inclusive")

    if day < 1 or day > 31:
        raise ValueError("Invalid day, day must be between 01 and 31 inclusive")

    if month == 2 and day > 29:
        raise ValueError("Invalid day for February, day must be between 01 and 29 inclusive")

    if month in (4, 6, 9, 11) and day > 30:
        raise ValueError("Invalid day for the month, day must be between 01 and 30 inclusive")

    return True


def main() -> None:
    """
    Main function to run the application

    :return: None
    """
    running = True

    while running:
        display_main_menu()

        user_choice = get_user_choice()

        if user_choice == "1":
            first_name, last_name, date_of_birth, hometown, house_number, phone_number = display_and_get_patient_info()

            add_patient(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                hometown=hometown,
                house_number=house_number,
                phone_number=phone_number
            )

        elif user_choice == "2":
            display_patients()
        elif user_choice == "3":
            display_patient_id_menu()

            try:
                patient_id = int(get_user_choice())
            except ValueError:
                print("\nInvalid patient ID\n")
                patient_id = int(get_user_choice())

            patient = search_patient(patient_id)

            if patient:
                first_name, last_name, date_of_birth, hometown, house_number, phone_number = display_and_get_patient_info()

                update_patient_info(
                    patient,
                    first_name=first_name,
                    last_name=last_name,
                    date_of_birth=date_of_birth,
                    hometown=hometown,
                    house_number=house_number,
                    phone_number=phone_number
                )
            else:
                print("\nPatient not found\n")
        elif user_choice == "4":
            display_patient_id_menu()

            try:
                patient_id = int(get_user_choice())
            except ValueError:
                print("\nInvalid patient ID\n")
                patient_id = int(get_user_choice())

            delete_patient(patient_id)
        elif user_choice == "5":
            display_patient_id_menu()

            try:
                patient_id = int(get_user_choice())
            except ValueError:
                print("\nInvalid patient ID\n")
                patient_id = int(get_user_choice())

            display_patient(patient_id)
        elif user_choice == "6":
            running = False
            print("Exiting application...")
            exit(0)
        else:
            print("Invalid choice, please select a valid option")
            continue


if __name__ == "__main__":
    main()
