#!flask/bin/python
#micheal nayebare
#mn@fieldcloud.com cc @fieldcloud 21.08.2020

import os
import unittest

import back

class TestCase(unittest.TestCase):

    def test_arraylist(self):
        expected = back.listDisks()
        assert expected != ""

if __name__ == '__main__':
    unittest.main()
