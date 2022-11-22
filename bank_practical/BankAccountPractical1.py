#!/usr/bin/env  python3

from string import ascii_letters, digits
'''This class is for creating Bank Account object.'''


def contains_all(string: str, a_set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in string for c in a_set]


class BankAccountPractical1:

    def __init__(self, account_id, acct_holder, date_opened_or_closed,
                 br_id, status, init_balance):

        self._account_id = account_id
        self.acct_holder = acct_holder  # non-empty string, len 1 to 254.
        self.date_opened_or_closed = date_opened_or_closed
        self.br_id = br_id  # a string startswith "BR" endswith digits.
        self._status = status
        self._init_balance = init_balance

    #  region
    #  Getters
    @property
    def account_id(self):
        return self._account_id

    @property
    def acct_holder(self):
        return self._acct_holder

    @property
    def br_id(self):
        return self._br_id

    @property
    def status(self):
        return self._status

    #  Setters
    @acct_holder.setter
    def acct_holder(self, new_acct_holder_name):
        valid_chars = "".join([ascii_letters, digits, '.'])
        if isinstance(new_acct_holder_name, str) and \
            contains_all(valid_chars, new_acct_holder_name) and \
                0 < len(new_acct_holder_name) < 255:
            self._acct_holder = new_acct_holder_name
        else:
            raise ValueError('Invalid account holder value.')

    @br_id.setter
    def br_id(self, br_id):
        if isinstance(br_id, str) and br_id.startswith("BR") and \
                    len(br_id) > 2 and contains_all(digits, br_id[2:]):
            self._br_id = br_id
        else:
            raise ValueError('Invalid Branch ID. Must start with "BR" \
followed by only digits.')

    #  endregion

    def __str__(self):
        '''print Account ID, Account Number, Date Opened, Branch ID, \
        Account Status'''
        output_str = (f"{'Account ID:':<20} {self._account_id:>20}\n\
{'Account Holder:':20} {self._acct_holder:>20}\n{'Date Opened:':<20} \
{self.date_opened_or_closed:>20}\n\
{'BranchID:':<20} {self._br_id:>20} \n{'Acct Status:':<20} \
{self._status:>20}\n")
        return output_str

    def close_account(self):
        if self._status == "Open":
            self._status = "Closed"
        else:
            print(f"Account {self._account_id} already closed.")


def main():
    '''This function has data used to test the class output'''
    try:
        acct1 = BankAccountPractical1("acct1", "accountholder01", "12/04/2019",
                                      "BR01", "Open", "1234123.00")
        print(acct1.br_id)
    except ValueError as err:
        print(err)
        exit()


if __name__ == "__main__":
    main()
