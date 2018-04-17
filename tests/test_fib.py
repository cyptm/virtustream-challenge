#!../virtustream/bin/python

import os
import unittest
import json
from server import app


class FibTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_fib(self):
        test_seq = [0,1,1,2,3]
        response = self.app.get('/fib/5', follow_redirects=True)

        print "Test response %s" % response
        self.assertEqual(response.status_code, 200)
        seq = json.loads(response.data)
        self.assertEqual(seq, test_seq)
            
if __name__ == "__main__":
    unittest.main()
