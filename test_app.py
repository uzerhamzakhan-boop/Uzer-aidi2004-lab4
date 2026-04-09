import unittest
from app import greet, farewell

class TestApp(unittest.TestCase):
    def test_greet(self):
        result = greet("Uzer")
        self.assertIn("Uzer", result)
        self.assertIn("AIDI 2004", result)

    def test_farewell(self):
        result = farewell("Uzer")
        self.assertIn("Uzer", result)

if __name__ == "__main__":
    unittest.main()
