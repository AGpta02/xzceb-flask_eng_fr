import unittest

from translator import frenchToEnglish, englishToFrench

class translator_tests(unittest.TestCase):
    def test_englishToFrench_null(self):
        self.assertEquals(englishToFrench(''),'entrée invalide')

    def test_englishToFrench_hello(self):
        self.assertEquals(englishToFrench('Hello'),'Bonjour')

    def test_frenchToEnglish_null(self):
        self.assertEquals(frenchToEnglish(''),'invalid entry')

    def test_frenchToEnglish_hello(self):
        self.assertEquals(frenchToEnglish('Bonjour'),'Hello')

if __name__ == '__main__':
    unittest.main()