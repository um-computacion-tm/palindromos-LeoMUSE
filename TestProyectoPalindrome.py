import unittest

from Palindrome import palindrome
from PalindromeRecursiva import palindromeRecursiva

class Testpalindrome(unittest.TestCase):

#Test iterativos

    def test_1(self):
        Resultado = palindrome('neuquen')
        self.assertEqual(Resultado, True)

    def test_2(self):
        Resultado = palindrome('casa')
        self.assertEqual(Resultado, False)

    def test_3(self):
        Resultado = palindrome('satas')
        self.assertEqual(Resultado, True)

    def test_4(self):
        Resultado = palindrome('perro')
        self.assertEqual(Resultado, False)

# Test Recursivos

    def testrecursivo_1(self):
        Resultado = palindromeRecursiva("sometemos")
        self.assertEqual(Resultado, True)

if __name__ == '__main__':
    unittest.main()