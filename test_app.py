import unittest
from app import sum, mul


class testing (unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(4,5),9)
        self.assertEqual(sum(5,6),11)
    
    def test_mul(self):
        self.assertEqual(mul(4,5),20)
        self.assertEqual(mul(-1,-2),2)
        
        
if __name__ == "__main__":
    unittest.main()