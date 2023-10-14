import unittest

def checkPermutations(parent, child):
    if(len(child) == 0 or parent == child):
        return True
    if(len(parent) == 0 and len(child) > 0):
        return False
    
    parent_hashtable = [0] * 128
    for i in range(len(parent)):
        parent_hashtable[ord(parent[i])] += 1

    for i in range(len(child)):
        parent_hashtable[ord(child[i])] -= 1
        if parent_hashtable[ord(child[i])] < 0:
            return False
    return True

# TESTING PURPOSES
class TestcheckPermutations(unittest.TestCase):
    def test_empty_child(self):
        self.assertTrue(checkPermutations("hello",""))

    def test_same_string(self):
        self.assertTrue(checkPermutations("hello", "hello"))

    def test_alphabat(self):
        self.assertTrue(checkPermutations("abcdefghijklmnopqrstuvwyxz", "ftvhge"))

    def test_empty_parent(self):
        self.assertFalse(checkPermutations("", "yes"))

    def test_specials(self):
        self.assertTrue(checkPermutations("1234567890=!@#$%^&*()+-_", "6438!&"))

    def test_same_characters_different_quantaties(self):
        self.assertFalse(checkPermutations("abba", "aaab"))

if __name__ == '__main__':
    unittest.main()