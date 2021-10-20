#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program formats a mailing adress


def address_format(
    full_name,
    street_number,
    sreet_name,
    city_name,
    province_name,
    postal_code,
    apartment=None,
):
    # this function formats mailing addresses
    # process
    if apartment == None:
        mail_address = "{0}\n{1} {2}\n{3} {4}  {5}".format(
            full_name, street_number, sreet_name, city_name, province_name, postal_code
        ).upper()
    else:
        mail_address = "{0}\n{1}-{2} {3}\n{4} {5}  {6}".format(
            full_name,
            apartment,
            street_number,
            sreet_name,
            city_name,
            province_name,
            postal_code,
        ).upper()

    return mail_address


def main():
    # this is the main function
    user_apartment = None

    print("This program formats your address to a mailing address.")
    # input & process
    user_full_name = input("Enter your full name : ")
    question = input("Do you live in an apartment (y/n) : ")
    if question.upper() == "Y" or question.upper() == "YES":
        user_apartment = input("Enter your apartment number : ")
    user_street_number = input("Enter your street number : ")
    user_sreet_name = input("Enter your street AND type (Main St, Express Pkwy) :  ")
    user_city_name = input("Enter your city : ")
    user_province_name = input("Enter your province (as abbreviation, ex: ON, BC…) : ")
    user_postal_code = input("Enter your postal code : ")

    try:
        user_street_number = int(user_street_number)
        # call function
        if user_apartment == None:
            adress = address_format(
                user_full_name,
                user_street_number,
                user_sreet_name,
                user_city_name,
                user_province_name,
                user_postal_code,
            )
        else:
            user_apartment = int(user_apartment)
            adress = address_format(
                user_full_name,
                user_street_number,
                user_sreet_name,
                user_city_name,
                user_province_name,
                user_postal_code,
                user_apartment,
            )
        print("")
        print(adress)

    except (Exception):
        print("\nInvalid input")

    print("\nDone.")


if __name__ == "__main__":
    main()
