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


def display_and_get_add_patient_info() -> tuple:
    """
    Display the add patient menu options

    :return: None
    """
    print("\n")
    print("Add Patient")
    print("<=================================================================>")
    print("Enter patient details:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    date_of_birth = input("Date of Birth (dd-mm-yyyy: ")
    hometown = input("Hometown: ")
    house_number = input("House Number: ")
    phone_number = input("Phone Number (024-400-0000): ")

    return first_name, last_name, date_of_birth, hometown, house_number, phone_number


def add_patient() -> None:
    pass


def display_patients(patient_id: int=None) -> None:
    pass


def update_patient_info(patient_id: int, patient_data: dict) -> None:
    pass


def delete_patient(patient_id: int) -> None:
    pass


def search_patient(patient_id: int) -> dict:
    pass


def validate_patient_date_of_birth(date_of_birth: str) -> bool:
    """
    Validate the date of birth format (dd-mm-yyyy)

    :param: date_of_birth:

    :return: True if the date of birth is valid, otherwise False
    """
    date_of_birth_pattern = re.compile(r"^\d{2}-\d{2}-\d{4}$")

    return bool(date_of_birth_pattern.fullmatch(date_of_birth))


def validate_patient_phone_number(phone_number: str) -> bool:
    """
    Validate the phone number format (024-400-0000)

    :param: phone_number:

    :return: True if the phone number is valid, otherwise False
    """
    phone_number_pattern = re.compile(r"^\d{3}-\d{3}-\d{4}$")

    return bool(phone_number_pattern.fullmatch(phone_number))


def validate_days_of_each_month(day: int, month: int) -> bool:
    """
    Validate the number of days in each month

    :param day: The day of the month:
    :param month: The month of the year:

    :return: True if the day is valid, otherwise False
    """
    if month > 12 or month < 1:
        return False

    if day < 1 or day > 31:
        return False

    if month == 2 and day > 29:
        return False

    if month in (4, 6, 9, 11) and day > 30:
        return False

    return True


def main() -> None:
    """
    Main function to run the application

    :return: None
    """


if __name__ == "__main__":
    main()
