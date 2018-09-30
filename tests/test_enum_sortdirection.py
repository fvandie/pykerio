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

import pykerio.enums


class TestCase_SortDirection(unittest.TestCase):
    def test_01_SortDirection_Asc(self):
        """
        Test SortDirection with Asc
        """
        value = pykerio.enums.SortDirection(value='Asc')
        self.assertEquals(value.value, 'Asc')
        self.assertEquals(value.dump(), 'Asc')

    def test_02_SortDirection_Desc(self):
        """
        Test SortDirection with Desc
        """
        value = pykerio.enums.SortDirection(value='Desc')
        self.assertEquals(value.value, 'Desc')
        self.assertEquals(value.dump(), 'Desc')

    @unittest.expectedFailure
    def test_99_SortDirection_FAIL(self):
        """
        Test SortDirection with FAIL
        """
        value = pykerio.enums.SortDirection(value='FAIL')
        self.assertEquals(value.value, 'FAIL')
        self.assertEquals(value.dump(), 'FAIL')