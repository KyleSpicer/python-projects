#!/usr/bin/env python3

import csv
from sys import argv
import argparse

"""
We have been appointed Court Genealogist of the Kingdom of Pylandia. Given a
dataset(tab-deliminated file) of family data, we are to create a command line
utility 'pyfamily' that can accurately search for specific fields. The fields
include: id, details, siblings, descendants, ancestors, intermarriage, all,
living, and search for various fields.
"""

fam_dict = []
# reads in familydata.txt, csv organizes and creates dictionary
try:
    with open("familydata.txt", "r", newline="") as fam_data:
        fam_reader = csv.DictReader(fam_data, delimiter="\t")
        for row in fam_reader:
            fam_dict.append(row)
except (FileNotFoundError, IOError):
    print("File Not Found. Check file location and path.")


#  accepts a person dict and modifies output to resemble exam requirements
def clean_person(person: dict):
    """
    Returns a formatted string to achieve exam formatting requirements.

        Parameters:
            (dict): a dictionary containing one persons information
        Returns:
            formatted string to achieve exam formatting requirements
    """
    values = list(person.values())
    values = values
    for value in values:
        if len(value) == 0:
            values.remove(value)
    join_values = ", ".join(values)
    title = f"{values[0]}: {person['firstname']} {person['middlename']} \
{person['lastname']}"
    end_title = join_values
    clean_person = f"{title} [{end_title}]"
    return clean_person


# accepts a name or any part of a name, returns the id num for that person(s)
def get_id(name_to_search: str):
    """
    Returns a list of formatted strings containing person data.

        Parameters:
            (str): any part of a name(first,middle,last)
        Returns:
            (list): list of formatted strings containing person data
    """

    cleaned_list = []
    name_to_search = ''.join(name_to_search.lower())
    for person in fam_dict:
        search_squish = ''.join(person['firstname'].lower() +
                                person['middlename'].lower() +
                                person['lastname'].lower())
        if name_to_search.lower() in search_squish:
            cleaned = clean_person(person)
            cleaned_list.append(cleaned)
        else:
            continue

    return cleaned_list


# accepts id number, returns all fields for that person(s)
def get_details(id_number: str):
    """
    Returns a list of formatted strings containing person data.

        Parameters:
            (str): id number for person
        Returns:
            (list): Returns a list of formatted strings containing person data.
    """
    clean_person_list = []
    for person in fam_dict:
        if person["idnumber"] == id_number:
            cleaned = clean_person(person)
            clean_person_list.append(cleaned)
    return clean_person_list


# accepts id number, returns list of siblings with id number and name
def get_siblings(id_number: str):
    """
    Returns a list of formatted strings containing siblings for that person

        Parameters:
            (str): id number for person
        Returns:
            (list): returns a list of formatted strings containing siblings
            data for id number
    """

    siblings_list = []
    for person in fam_dict:
        if person["idnumber"] == id_number:
            for sibling in fam_dict:
                if sibling["motherid"] == person["motherid"] and \
                        sibling['motherid'] != '':
                    sibling = clean_person(sibling)
                    siblings_list.append(sibling)
                elif sibling["fatherid"] == person["fatherid"] and \
                        sibling['fatherid'] != '':
                    sibling = clean_person(sibling)
                    siblings_list.append(sibling)
                else:
                    continue

    for person in siblings_list:
        if person[0:2] == id_number:
            siblings_list.remove(person)

    return siblings_list


# accepts id number, returns list of all descendants with id number and name
def get_descendants(idnumber: str):
    """
    Returns list of all descendants for id number entered. Function uses
    recursion to accurately retrieve all descendants for id number.

        Parameters:
            (str): id number
        Returns:
            (list): returns a list of descendants associated with id number
    """

    descendants_list = []
    for person in fam_dict:
        if person["idnumber"] == idnumber:
            for another_person in fam_dict:
                if (
                    person["idnumber"] == another_person["fatherid"]
                    or person["idnumber"] == another_person["motherid"]
                ):
                    descendants_list.append(another_person)
                    des_list = get_descendants(another_person["idnumber"])
                    for des in des_list:
                        descendants_list.append(des)

    return descendants_list


# accepts id number, returns list of all ancestors with id number and name
def get_ancestors(id_number: str):
    """
    Returns list of all descendants for id number entered. Function uses
    recursion to accurately retrieve all ancestors for id number.

        Parameters:
            (str): id number
        Returns:
            (list): returns a list of ancestors associated with id number
    """

    ancestors_list = []
    for person in fam_dict:
        if person["idnumber"] == id_number:
            for another_person in fam_dict:
                if (
                    another_person["idnumber"] == person["motherid"]
                    or another_person["idnumber"] == person["fatherid"]
                ):
                    ancestors_list.append(another_person)
                    anc_list = get_ancestors(another_person["idnumber"])
                    for anc in anc_list:
                        ancestors_list.append(anc)

    return ancestors_list


# accepts lastname1 lastname2, returns list of pairs with matching last names
def get_intermarriage(names: str):
    """
    Returns list of pairs with matching spouseid's

        Parameters:
            (str): two last names for matches you'd like to search for
        Returns:
            (list): returns a list of pairs with matching spouseid's
    """

    couples = []
    for name in names:
        name1 = names[0]
        name2 = names[1]

    for person in fam_dict:
        for another_person in fam_dict:
            if (
                person["lastname"].lower() == name1.lower()
                and another_person["lastname"].lower() == name2.lower()
            ):
                if person["idnumber"] == another_person["spouseid"]:
                    couples.append(person)
                    couples.append(another_person)

    return couples


# takes no arguments, list all names with IDs
def get_all():
    """
    Returns a full list of formatted strings from the database.

        Parameters:
            (none): no parameters are required
        Returns:
            (list): returns a list of formatted strings from database
    """
    big_list = []
    for person in fam_dict:
        showered = clean_person(person)
        big_list.append(showered)
    return big_list


# accepts one or more name=value pairs,
def get_search(name_value_pair: list):
    """
    Return a list of person dictionaries from the search entered.

        Parameters:
            (str): key=value pair to search for
        Returns:
            (list): returns a list of dictionaries associated with search
    """
    first_list = []
    search_dict = {}

    for item in name_value_pair:
        search_key, search_value = parse_search(item)
        search_dict[search_key] = search_value

    for person in fam_dict:
        valid = True
        for key, value in search_dict.items():
            if value.lower() not in person[key].lower():
                valid = False

        if valid is True:
            first_list.append(person)

    return first_list


def parse_search(search_item: str):
    """
    Returns a string after separating key=value pair

        Parameters:
            (str): key=value pair
        Returns:
            (str): return key and value as a string
    """
    valid_keys = ['firstname', 'middlename', 'lastname', 'hobby', 'idnumber',
                  'fatherid', 'motherid', 'spouseid', 'honorific', 'suffix',
                  'gender', 'dateofbirth', 'dateofdeath']

    if '=' not in search_item:
        print(f'{search_item} is an invalid search.\n\
Must be a key=value pair.\n\
If multiple words follow ( = ), wrap words in quotations.\n\
example: hobby="zeppelin repair"')
        exit()

    key, value = search_item.split("=")

    if key not in valid_keys:
        print(f'invalid key search. \nvalid keys = {valid_keys}')
        exit()

    return key, value


# if any argument is living, then only living persons will be output
def get_living(living: list) -> list:
    """
    Returns a list of only living persons in the database

        Parameters:
            (list): accepts a list of dictionaries to be used
        Returns:
            (list): returns a list of dictionaries with only living persons
    """
    living_list = []
    for person in living:
        if person[-7:-1] == "LIVING":
            living_list.append(person)

    return living_list


def main():
    """
    Completes logic for entire program.

        Parameters:
            utilizes argparse to accept command line arguments and complete
            functions as needed.

        Returns:
            formatted output according to exam guidelines.
    """

    # using argparse to add arguments for command line argument parsing
    parser = argparse.ArgumentParser(
        description="Welcome to the pyfamily \
command line utility program!"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Enter all to preview every person in database.",
        dest="all",
    )

    parser.add_argument("--details",
                        type=str,
                        help="Enter id number",
                        dest="details")

    parser.add_argument(
        "--id", type=str, help="Enter name or any part of a name", dest="id"
    )

    parser.add_argument("--siblings",
                        type=str,
                        help="Enter id number",
                        dest="siblings")

    parser.add_argument(
        "--ancestors", type=str, help="Enter id number", dest="ancestors"
    )

    parser.add_argument(
        "--descendants", type=str, help="Enter id number", dest="descendants"
    )

    parser.add_argument(
        "--living",
        action="store_true",
        help="Enter 'living' if you want to see living souls",
        dest="living",
    )

    parser.add_argument(
        "--intermarriage",
        nargs=2,
        type=str,
        help="Enter two last names separated by a space.",
        dest="intermarriage",
    )

    parser.add_argument(
        "--search",
        metavar="KEY=VALUE",
        nargs="*",
        type=str,
        help='Enter key=value pair. keys include: idnumber, honorific, \
        firstname, middlename, lastname, suffix, gender, spouseid, hobby, \
        dateofbirth, dateofdeath. If you enter two words after the equals \
        sign the pair must be wrapped in quotation marks.',
        dest="search",
    )

    args = parser.parse_args()

    # SEARCH ##################################################################
    if args.search:
        completed_list = []
        search_list = get_search(args.search)
        for person in search_list:
            cleansed = clean_person(person)
            completed_list.append(cleansed)
        if args.living:
            living_list = get_living(completed_list)
            for person in living_list:
                print(person)
        else:
            for person in completed_list:
                print(person)

    # ALL #####################################################################
    if args.all:
        big_list = get_all()
        if args.living:
            living_list = get_living(big_list)
            for person in living_list:
                print(person)
        else:
            for person in big_list:
                print(person)

    # DETAILS #################################################################
    elif args.details:
        clean_list = get_details(args.details)
        if args.living:
            living_list = get_living(clean_list)
            for person in living_list:
                print(person)
        else:
            for person in clean_list:
                print(person)

    # ID ######################################################################
    elif args.id:
        clean_people_list = get_id(args.id)

        if args.living:
            living_people = get_living(clean_people_list)
            for person in living_people:
                print(person)
        else:
            for person in clean_people_list:
                print(person)

    # SIBLINGS ################################################################
    elif args.siblings:
        sib_list = get_siblings(args.siblings)
        if args.living:
            living_list = get_living(sib_list)
            for person in living_list:
                print(person)
        else:
            for sibling in sib_list:
                print(sibling)

    # ANCESTORS ###############################################################
    elif args.ancestors:
        anc_list = get_ancestors(args.ancestors)
        actual_list = []
        output_ancestors = []

        for anc in anc_list:
            if anc not in actual_list:
                actual_list.append(anc)

        for person in actual_list:
            person["idnumber"] = int(person["idnumber"])

        actual_list =\
            sorted(actual_list, key=lambda person: person["idnumber"])
        for person in actual_list:
            person["idnumber"] = str(person["idnumber"])
            happy_person = clean_person(person)
            output_ancestors.append(happy_person)

        if args.living:
            living_list = get_living(output_ancestors)
            for person in living_list:
                print(person)
        else:
            for anc in output_ancestors:
                print(anc)

    # DESCENDANTS #############################################################
    elif args.descendants:
        anc_list = get_descendants(args.descendants)
        actual_list = []
        output_desc = []
        for anc in anc_list:
            if anc not in actual_list:
                actual_list.append(anc)

        for person in actual_list:
            person["idnumber"] = int(person["idnumber"])

        actual_list =\
            sorted(actual_list, key=lambda person: person["idnumber"])
        for person in actual_list:
            person["idnumber"] = str(person["idnumber"])
            happy_person = clean_person(person)
            output_desc.append(happy_person)

        if args.living:
            living_list = get_living(output_desc)
            for person in living_list:
                print(person)
        else:
            for desc in output_desc:
                print(desc)

    # INTERMARRIAGE ###########################################################
    elif args.intermarriage:
        # get_intermarriage(args.intermarriage[0], args.intermarriage[1])
        married_list = get_intermarriage(args.intermarriage)
        living_list = []

        if args.living:
            for person in married_list:
                if person["dateofdeath"] == "LIVING":
                    living_list.append(person)
            for person in living_list:
                for another_person in living_list:
                    if person["spouseid"] == another_person["idnumber"]:

                        output = f"{person['firstname']} \
{person['middlename']} {person['lastname']} [{person['spouseid']}] <=> \
{another_person['firstname']} {another_person['middlename']} \
{another_person['lastname']} [{another_person['spouseid']}]"

                        print(output)
        else:
            for person in married_list:
                for another_person in married_list:
                    if person["spouseid"] == another_person["idnumber"]:
                        output = f"{person['firstname']} \
{person['middlename']} {person['lastname']} [{person['spouseid']}] <=> \
{another_person['firstname']} {another_person['middlename']} \
{another_person['lastname']} [{another_person['spouseid']}]"
                        print(output)


if __name__ == "__main__":
    main()
