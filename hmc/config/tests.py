#!/usr/bin/env python

import unittest2 as unittest

from hmc.config.testing import HMC_CONFIG_INTEGRATION_TESTING


class TestSetup(unittest.TestCase):

    layer = HMC_CONFIG_INTEGRATION_TESTING

    def test_portal_title(self):
        portal = self.layer['portal']
        self.assertEqual("Human Motion and Control Laboratory",
                         portal.getProperty('title'))

    def test_portal_description(self):
        portal = self.layer['portal']
        self.assertEqual("Welcome to the Parker Hannifin Human Motion and Control Laboratory at Cleveland State University.",
                         portal.getProperty('description'))
