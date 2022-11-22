#!/usr/bin/env python3

from typing import IO
from BankAccountPractical1 import BankAccountPractical1
import os


def load_bank_accounts_from_file():
    '''function will read text file bankinfo1A.txt: populate and reutrn a
list of bank account objects.'''
    ba_list = []
    try:
        with open("bankinfo1A.txt", "r") as bank_db:
            for account in bank_db.readlines():
                account = account.replace('\n', '').split(" ")
                ba_list.append(BankAccountPractical1(account[0], account[3],
                               account[2], account[1], account[5], account[4]))
            return ba_list
    except FileNotFoundError as e:
        print(f"File not found.\n {e}")
        return -1

    except Exception as e:
        print(e)


def return_closed_acct_IDs(ba_list):
    '''funtion returns a list of account IDs corresponding to accounts with
    a status of "Closed"'''
    closed_accounts = []
    for account in ba_list:
        if account._status == "Closed":
            closed_accounts.append(account)
    return closed_accounts


def accts_with_this_branch_id(br_id_search, ba_list):
    '''Return a list of BankAccount objects with the branch_id property of the
    object of the passed branch_id.'''
    branch_id_list = []
    for branch_id in ba_list:
        if branch_id.br_id == br_id_search:
            if branch_id_list != 0:
                branch_id_list.append(branch_id)
    return(branch_id_list)


def account_for_this_ID(acct_id, ba_list):
    '''Access every account looking for the One to return. If not found,
    return None.'''
    for account in ba_list:
        if account.account_id == acct_id:
            return account
    return None


def print_first_elem_if_not_empty(user_search, ba_list):
    count = 0
    print(f'Using funtion to print element of list')
    num_BR1_accounts = len(accts_with_this_branch_id(user_search, ba_list))
    print(f'Number of accounts for branch {user_search}: {num_BR1_accounts}')
    for account in ba_list:
        if account.br_id == user_search:
            count += 1
            if count == 1:
                print(f'First account for branch {user_search}:\n{account}')
    br1_closed = return_closed_acct_IDs(ba_list)
    br1_closed_len = len(return_closed_acct_IDs(ba_list))
    print(f'Number of closed account: {br1_closed_len}')
    br1_first_closed = br1_closed[0]
    print(f'First closed account is:\n{br1_first_closed}')


def main():
    '''validates the load_bank_accounts_from_file function and proper Class
    implementation'''

    ba_list = load_bank_accounts_from_file()
    if -1 == ba_list:
        print(f'Bad return. Exiting')
        exit()
    #  Number of accounts created
    num_of_accounts = len(ba_list)

    print(f'Number of accounts created = {num_of_accounts}')

    #  Number of accounts for BR1
    br1_count = len(accts_with_this_branch_id("BR1", ba_list))
    print(f'Number of accounts for BR1 is: {br1_count}')

    #  First two accounts for BR1
    br1_list = accts_with_this_branch_id("BR1", ba_list)
    print(f'First two accounts for BR1:\n\n{br1_list[0]}\n{br1_list[1]}')

    #  Details for account ID Acct10000
    Acct10000_info = account_for_this_ID("Acct10000", ba_list)
    print(f'Details for account ID Acct10000 is:\n{Acct10000_info}')

    #  Number of closed accounts
    closed_account_count = len(return_closed_acct_IDs(ba_list))
    print(f'Number of closed accounts: {closed_account_count}\n')

    #  First closed account found
    closed_account_list = return_closed_acct_IDs(ba_list)
    print(f'First closed account found:\n{closed_account_list[0]}')

    #  Using function to print element of list
    print_first_elem_if_not_empty("BR1", ba_list)


if __name__ == "__main__":
    main()
