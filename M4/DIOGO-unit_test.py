import unittest
from vector import Vector

### THIS CODE IS FROM MY CLASSMATE AND FRIEND DIOGO LA CABRITA TEIXEIRA ###
### it GOT A 100% IN THE TEST EVALUATION, MINE DIDN'T, SO USE HIS FOR GUIDANCE ##

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
        resultat = self.empty + self.empty
        self.assertEqual("[]", str(resultat))
    
    def test_add_single_element(self):
        resultat = self.single_element + self.single_element
        self.assertEqual("[2]", str(resultat))
    
    def test_add_multiple_element(self):
        resultat = self.multiple_element + self.multiple_element
        self.assertEqual("[2,4,6]", str(resultat))
    
    def test_add_not_equal_length(self):
        self.assertRaises(AssertionError, self.empty + self.single_element)
        
        self.assertRaises(AssertionError, self.single_element + self.multiple_element)
    
    def test_add_different_magnitud(self):
        resultat = Vector([0, -1, 1, 1, -1]) + Vector([-1, 0, -1, 1, -1])
        self.assertEqual("[-1,-1,0,2,-2]", str(resultat))
    
    def test_sub_empty(self):
        resultat = self.empty - self.empty
        self.assertEqual("", str(resultat))
    
    def test_sub_single_element(self):
        resultat = self.single_element - self.single_element
        self.assertEqual("0", str(resultat))
    
    def test_sub_multiple_element(self):
        resultat = self.multiple_element - self.multiple_element
        self.assertEqual("0", str(resultat))
    
    def test_sub_different_magnitud(self):
        resultat = Vector([0, -1, 1, 1, -1]) - Vector([-1, 0, -1, 1, -1])
        self.assertEqual("0", str(resultat))
    
    def test_sub_not_equal_length(self):
        with self.assertRaises(AssertionError):
            self.empty - self.single_element
        with self.assertRaises(AssertionError):
            self.single_element - self.multiple_element
    
    def test_mult_empty(self):
        resultat = self.empty * self.empty
        self.assertEqual("", str(resultat))
    
    def test_mult_single_element(self):
        resultat = self.single_element * self.single_element
        self.assertEqual("1", str(resultat))
    
    def test_sub_multiple_element(self):
        resultat = self.multiple_element * self.multiple_element
        self.assertEqual("0", str(resultat))
    
    def test_sub_not_equal_length(self):
        with self.assertRaises(AssertionError):
            self.empty * self.single_element
        with self.assertRaises(AssertionError):
            self.single_element * self.multiple_element
