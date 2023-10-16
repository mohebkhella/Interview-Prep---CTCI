import unittest

def palindromPermuatation(s):
    special_chars = "1234567890!@#$%^&*()_+-=[]{}|;:'\",.<>?\\/ "
    for char in special_chars:
        s = s.replace(char, '')
    s = s.lower()

    s_hashtable = [0] * 26
    for i in range(len(s)):
        s_hashtable[ord(s[i]) - ord('a')] += 1

    one_occurence = 0
    for i in range(len(s_hashtable)):
        if s_hashtable[i] % 2 == 1:
            one_occurence += 1
            if one_occurence > 1:
                return False
            
    return True

# TESTING PURPOSES
class TestcheckPermutations(unittest.TestCase):
    def test_book_case(self):
        self.assertTrue(palindromPermuatation("Tact Coa"))

    def test_originally_not_a_palindrome(self):
        self.assertTrue(palindromPermuatation("aAb"))

    def test_originally_not_a_palindrome_2(self):
        self.assertTrue(palindromPermuatation("carerac"))

    def test_not_a_palindrome(self):
        self.assertFalse(palindromPermuatation("yoabsnjan"))

    def test_specials(self):
        self.assertTrue(palindromPermuatation("---yoyo"))

    def test_empty_string(self):
        self.assertTrue(palindromPermuatation(""))

if __name__ == '__main__':
    unittest.main()