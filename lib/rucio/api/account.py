# Copyright European Organization for Nuclear Research (CERN)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Authors:
# - Vincent Garonne, <vincent.garonne@cern.ch>, 2011
# - Angelos Molfetas, <angelos.molfetas@cern.ch>, 2011
# - Thomas Beermann, <thomas.beermann@cern.ch>, 2012

from rucio.core import account


def add_account(accountName, accountType):
        """
        Creates an account with the provided account name, contact information, etc.

        :param accountName: The account name.
        :param accountType: The account type
        """
        account.add_account(accountName, accountType)


def del_account(accountName):
        """
        Disables an account with the provided account name.

        :param accountName: The account name.
        """
        account.del_account(accountName)


def get_account_info(accountName):
        """
        Returns the info like the statistics information associated to an account.

        :param accountName: The account name.
                          timestamp will be removed.
        :returns: A list with all account information.
        """
        return account.get_account(accountName)


def set_account_limits(accountName, limitationName, limitationValue):
        """
        Set's account's quota limit of account.

        :param accountName:     The account name.
        :param limitationName:  The limitation name.
        :param limitationValue: The limitation value.

        :returns: A Response code is returned and if successful is a "0". If an error occurs, the error message text is also returned.
        """
        pass


def get_account_limits(accountName):
        """
        Lists the limitation names/values for the specified account name.

        REST API: http://<host>:<port>/rucio/account/<accountName>/limits

        :param accountName:     The account name.

        :returns: A Response code is returned and if successful is a "0". If an error occurs, the error message text is also returned.
        """
        pass


def list_accounts():
        """
        Lists all the Rucio account names.

        REST API: http://<host>:<port>/rucio/accounts

        :returns: List of all accounts.
        """
        return account.list_accounts()
