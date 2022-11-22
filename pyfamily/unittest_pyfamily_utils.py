#!/usr/bin/env python3

import unittest
import pyfamily as pf
import ast

"""
Purpose: This program tests the pyfamily.py functions and their
ability to handle valid and invalid input.
"""


class TestPyfamily(unittest.TestCase):
    def setUp(self):

        self.invalid_person = {
            "idnumber": "(#Q*($U",
            "honorific": "Jester",
            "firstname": "#$%",
            "middlename": "  --\\-",
            "lastname": "01234",
            "suffix": "--",
            "motherid": "  ))",
            "fatherid": "12PLSD",
            "gender": "nonebinary",
            "spouseid": "will never marry",
            "hobby": "-555-",
            "dateofbirth": "1 B.C.",
            "dateofdeath": "VAMPIRE",
        }

        self.valid_person = {
            "idnumber": "41",
            "honorific": "",
            "firstname": "Mitzi",
            "middlename": "Sue",
            "lastname": "Hamworth",
            "suffix": "",
            "motherid": "29",
            "fatherid": "32",
            "gender": "f",
            "spouseid": "39",
            "hobby": "zeppelin repair",
            "dateofbirth": "19411206",
            "dateofdeath": "LIVING",
        }
        print()
        pass

    def tearDown(self):
        pass

    # tests formatting person DICTIONARY object for exam requirement output
    def test_format_person_information_valid(self):
        print("Testing: test_format_person_information_valid")
        try:
            pf.clean_person(self.valid_person)
        except Exception as e:
            self.fail("Raised Exception while formatting valid person")

    # tests formatting person LIST object for exam requirement output
    def test_format_person_information_invalid(self):
        print("Testing: test_format_person_information_invalid")
        with self.assertRaises(Exception):
            pf.clean_person(list(self.invalid_person))

    # tests functions ability to search for any part of persons name and return
    # than persons object
    def test_get_id_valid(self):
        print(f"Testing: test_get_id_valid")
        try:
            pf.get_id(self.valid_person["firstname"])
        except Exception as e:
            self.fail("Raised Exception while searching name for valid person")

    # tests functions ability to handle invalid input
    def test_get_id_invalid(self):
        print(f"Testing: test_get_id_invalid")
        # if user inputs invalid input, an empty list is returned
        self.assertEqual(pf.get_id(self.invalid_person["firstname"]), [])

    # tests functions ability to retrieve person information from idnumber
    def test_get_details_valid(self):
        print(f"Testing: test_get_details_valid")
        try:
            pf.get_details(self.valid_person["idnumber"])
        except Exception as e:
            self.fail("Raised Exception while getting details - valid person")

    # tests functions ability to accept invalid input and return empty list
    def test_get_details_invalid(self):
        print(f"Testing: test_get_details_invalid")
        # if user inputs invalid input, an empty list is returned
        self.assertEqual(pf.get_details(self.invalid_person["idnumber"]), [])

    # tests functions ability to accept idnumber and return person's siblings
    def test_get_siblings_valid(self):
        print(f"Testing: test_get_siblings_valid")
        valid_sibling_id = "30"
        try:
            sibling = pf.get_siblings(valid_sibling_id)
        except Exception as e:
            self.fail("Raised Exception while getting siblings - valid person")

    # tests functions ability to receive invalid idnumber and return empty list
    def test_get_siblings_invalid(self):
        print(f"Testing: test_get_siblings_invalid")
        self.assertEqual(pf.get_siblings(self.invalid_person["idnumber"]), [])

    # tests functions ability to receive valid idnumber and return all
    # descendants matching that idnumber
    def test_get_descendants_valid(self):
        print(f"Testing: test_get_descendants_valid")
        valid_descendant = "15"
        try:
            descendant = pf.get_descendants(valid_descendant)
        except Exception as e:
            self.fail("Raised Exception for getting descendant - valid person")

    # tests functions ability to receive invalid idnumber and return nothing.
    def test_get_descendants_invalid(self):
        print(f"Testing: test_get_descendants_invalid")
        self.assertEqual(pf.get_descendants(self.invalid_person["idnumber"]),
                         [])

    # tests functions ability to retrieve ancestors from valid idnumber
    def test_get_ancestors_valid(self):
        print(f"Testing: test_get_ancestors_valid")
        try:
            pf.get_ancestors(self.valid_person["idnumber"])
        except Exception as e:
            self.fail("Raised Exception for getting ancestor - valid person")

    # tests functions ability to receive invalid idnumber and return nothing
    def test_get_ancestors_invalid(self):
        print(f"Testing: test_get_ancestors_invalid")
        self.assertEqual(pf.get_ancestors(self.invalid_person["idnumber"]), [])

    # tests functions ability to receive valid last names and return a combo
    # list of people who are married
    def test_get_intermarriage_valid(self):
        print(f"Testing: test_get_intermarriage_valid")
        lastnames = "spamford", "hamworth"
        test = pf.get_intermarriage(lastnames)
        self.assertEqual(type(test), list)

    # tests functions ability to receive two invalid last names and return
    # an empty list because they're not present in the database
    def test_get_intermarriage_invalid(self):
        print(f"Testing: test_get_intermarriage_invalid")
        invalidnames = "spicer", "deberry"
        self.assertEqual(pf.get_intermarriage(invalidnames), [])

    # tests functions ability to properly run without positional arguments
    def test_get_all_valid(self):
        print("Testing: test_get_all_valid")
        try:
            pf.get_all()
        except Exception as e:
            self.fail("Raised Exception while trying get_all")

    # tests functions ability to raise a TypeError when arguments are used
    def test_get_all_invalid(self):
        print("Testing: test_get_all_invalid")
        # TypeError should be raised because no arguments are allowed
        with self.assertRaises(TypeError):
            pf.get_all("all")

    # tests functions ability to properly search persons key=values pair
    def test_get_search_valid(self):
        print("Testing: test_get_search_valid")
        try:
            pf.get_search(["hobby=ze"])
            pf.get_search(["idnumber=30"])
            pf.get_search(["motherid=29"])
        except Exception as e:
            self.fail("Raised Exception while getting valid search")

    # tests functions ability to raise KeyError exception with invalid search
    def test_get_search_invalid(self):
        print("Testing: test_get_search_invalid")
        with self.assertRaises(KeyError):
            pf.get_search(["unknown=unknown"])

    # tests functions ability to accept key, value pair and create two strings
    def test_parse_search_valid(self):
        print("Testing: test_parse_search_valid")
        try:
            pf.parse_search("hobby=ze")
        except Exception as e:
            self.fail("Raised Exception while getting invalid search")

    # tests functions ability to raise ValueError when invalid input is entered
    def test_parse_search_invalid(self):
        print("Testing: test_parse_search_invalid")
        # raises a ValueError because it has a proper input, but an
        # inappropriate value
        with self.assertRaises(ValueError):
            pf.parse_search("thats---anerror")

    # tests function ability to accept a list of formatted strings and
    # return those with 'LIVING' as the last six characters.
    def test_get_living_valid(self):
        print("Testing: test_get_living_valid")
        try:
            test_list = [self.invalid_person, self.valid_person]
            clean_list = []
            for person in test_list:
                clean_one = pf.clean_person(person)
                clean_list.append(clean_one)
            test = pf.get_living(clean_list)
        except Exception as e:
            self.fail("Raised Exception while getting valid living")

    # tests functions ability to raise TypeError when a list of dictionaries is
    # passed in. This function requires a list of formatted strings.
    def test_get_living_invalid(self):
        print("Testing: test_get_living_invalid")
        test_list = [self.invalid_person, self.valid_person]
        with self.assertRaises(TypeError):
            pf.get_living(test_list)


if __name__ == "__main__":
    unittest.main()
