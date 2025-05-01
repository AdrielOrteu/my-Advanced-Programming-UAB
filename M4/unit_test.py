import unittest
from vector import Vector


class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.empty = Vector([])
        cls.single_element = Vector([1])
        cls.multiple_element = Vector([1, 2, 3])
    
    def test_str_empty(self):
        self.assertEqual("[]", str(self.empty))
    
    def test_str_single_element(self):
        self.assertEqual("[1]", str(self.single_element))
    
    def test_str_multiple_element(self):
        self.assertEqual("[1,2,3]", str(self.multiple_element))
    
    def test_add_empty(self):
        r = self.empty + self.empty
        self.assertEqual("[]", r)
    
    def test_add_single_element(self):
        r = self.single_element + self.single_element
        self.assertEqual([2], r)
    
    def test_add_multiple_element(self):
        r = self.multiple_element + self.multiple_element
        self.assertEqual("[2,4,6]", str(r))
    
    def test_add_not_equal_length(self):
        with self.assertRaises(AssertionError):
            self.single_elemen + self.empty
        with self.assertRaises(AssertionError):
            self.single_element + self.multiple_element
    
    def test_add_different_magnitud(self):
        r = Vector([0, -1, 1, 1, -1]) + Vector([-1, 0, -1, 1, -1])
        self.assertEqual("[-1,-1,0,2,-2]", str(r))
    
    def test_sub_empty(self):
        r = self.empty - self.empty
        self.assertEqual("", str(r))
    
    def test_sub_single_element(self):
        r = self.single_element - self.single_element
        self.assertEqual(0, r)
    
    def test_sub_multiple_element(self):
        r = self.multiple_element - self.multiple_element
        self.assertEqual(0, r)
    
    def test_sub_different_magnitud(self):
        r = Vector([0, -1, 1, 1, -1]) - Vector([-1, 0, -1, 1, -1])
        self.assertEqual(0, r)
    
    def test_sub_not_equal_length(self):
        with self.assertRaises(AssertionError):
            self.single_element - self.empty
        with self.assertRaises(AssertionError):
            self.single_element - self.multiple_element
    
    def test_mult_empty(self):
        r = self.empty * self.empty
        self.assertEqual("", str(r))
    
    def test_mult_single_element(self):
        r = self.single_element * self.single_element
        self.assertEqual(1, str(r))
    
    def test_mul_multiple_element(self):
        r = self.multiple_element * self.multiple_element
        self.assertEqual(0, r)
    
    def test_mul_not_equal_length(self):
        with self.assertRaises(AssertionError):
            self.single_element * self.empty
        with self.assertRaises(AssertionError):
            self.single_element * self.multiple_element
