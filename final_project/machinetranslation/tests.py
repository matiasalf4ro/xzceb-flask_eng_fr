import unittest
from translator import englishToFrench, frenchToEnglish

class testenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(englishToFrench(""),"Error")
        self.assertEqual(frenchToEnglish(""),"Error")

unittest.main()S