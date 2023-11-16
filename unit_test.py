import unittest
from hello import greeting

class TestHello(unittest.TestCase):
    def test_pass_1(self):
        self.assertEqual(greeting(),"Hello Nhat Quan Bui")
    
    def test_pass_2(self):
        self.assertTrue(isinstance(greeting(),str))
    
    def test_pass_3(self):
        self.assertTrue(len(greeting()) > 0)
    
    def test_fail_1(self):
        self.assertEqual(greeting(),"Hello my name")
        
    def test_fail_2(self):
        self.assertIsNone(greeting())
        