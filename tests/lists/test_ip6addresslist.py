##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import unittest

import pykerio.lists
import pykerio.shared


class TestCase_Ip6AddressList(unittest.TestCase):
    def test_01_Ip6AddressList(self):
        """
        Test Ip6AddressList
        """
        testlist = pykerio.lists.Ip6AddressList()
        self.assertEquals(len(testlist), 0)

        address = '::1'
        ip6address = pykerio.shared.Ip6Address(address)
        testlist.append(ip6address)
        self.assertEquals(len(testlist), 1)

        self.assertEquals(testlist[-1], ip6address)

        testlist.clear()
        self.assertEquals(len(testlist), 0)