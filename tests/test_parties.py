#!/usr/bin/env python

import os
import unittest

#from vlib.odict import odict

from parties import Parties, Party


# fixtures

CUSTOMER_ID = 7
CUSTOMER_LASTNAME = 'Ritell'

class TestParties(unittest.TestCase):

    def testgetList(self):
        parties = Parties()
        table = parties.get()
        self.assertIsInstance(table, tuple)
        self.assertTrue(len(table) > 1)
        self.assertIsInstance(table[0], dict)

class TestParty(unittest.TestCase):

    def testgetRecord(self):
        party = Party(CUSTOMER_ID)
        self.assertEqual(party.last_name, CUSTOMER_LASTNAME)

unittest.main()
