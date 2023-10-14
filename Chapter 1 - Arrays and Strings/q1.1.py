import unittest

def isUnique(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

def isUniqueOptimized(s):
    if(len(s) == 0):
        return True
    hashtable = [0] * 128
    for i in range(len(s)):
        hashtable[ord(s[i])] += 1
        if hashtable[ord(s[i])] > 1:
            # print(f"The character {s[i]} occurs {hashtable[ord(s[i])]} times")
            return False
    return True

# TESTING PURPOSES
class TestIsUniqueOptimized(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(isUniqueOptimized(""))

    def test_alphabet_in_order(self):
        self.assertTrue(isUniqueOptimized("abcdefghijklmnopqrstuvwyxz"))

    def test_special_characters(self):
        self.assertTrue(isUniqueOptimized("1234567890=!@#$%^&*()+-_"))

    def test_duplicate_characters(self):
        self.assertFalse(isUniqueOptimized("abcbisq"))

    def test_repeated_characters_at_ends(self):
        self.assertFalse(isUniqueOptimized("abcdefa"))

    def test_repeated_character_at_end(self):
        self.assertFalse(isUniqueOptimized("bcadefa"))

if __name__ == '__main__':
    unittest.main()