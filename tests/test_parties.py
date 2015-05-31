#!/usr/bin/env python

import os
import unittest

#from vlib.odict import odict

from parties import Parties


# fixtures

CUSTOMER_ID = 7
CUSTOMER_LASTNAME = 'Ritell'

class TestParties(unittest.TestCase):

    def testgetList(self):
        p = Parties()
        table = p.get()
        self.assertIsInstance(table, tuple)
        self.assertTrue(len(table) > 1)
        self.assertIsInstance(table[0], dict)

unittest.main()
