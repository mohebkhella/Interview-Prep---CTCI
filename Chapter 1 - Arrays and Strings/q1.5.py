import unittest

def oneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    s1_hashtable = [0] * 128
    s2_hashtable = [0] * 128
    ite = len(s1)
    if len(s2) < len(s1):
        ite = len(s2)    
    
    for i in range(ite):
        s1_hashtable[ord(s1[i])] += 1
        s2_hashtable[ord(s2[i])] += 1
    
    if ite == len(s2) and len(s1) != len(s2):
        s1_hashtable[ord(s1[len(s1) - 1])] += 1
    elif ite == len(s1) and len(s1) != len(s2):
        s2_hashtable[ord(s2[len(s2) - 1])] += 1
    
    if s1_hashtable == s2_hashtable:
        return True
    
    sus_count = 0
    for i in range(len(s1_hashtable)):
        if abs(s1_hashtable[i] - s2_hashtable[i]) != 0:
            # print(f"at {chr(i)} s1 table says {s1_hashtable[i]} and s2 table says {s2_hashtable[i]}")
            sus_count += 1
        if sus_count > 2:
            return False
            
    return True

# TESTING PURPOSES
class TestcheckPermutations(unittest.TestCase):
    def test_book_case_1(self):
        self.assertTrue(oneAway("pale", "ple"))

    def test_book_case_2(self):
        self.assertTrue(oneAway("pales", "pale"))

    def test_book_case_3(self):
        self.assertTrue(oneAway("pale", "bale"))

    def test_book_case_4(self):
        self.assertFalse(oneAway("pale", "bake"))

    def test_basic_remove(self):
        self.assertTrue(oneAway("abcde", "abde"))

    def test_basic_add(self):
        self.assertTrue(oneAway("abde", "abxde"))

    def test_basic_change(self):
        self.assertTrue(oneAway("abcde", "abxde"))

    def test_mismatching_lengths(self):
        self.assertFalse(oneAway("hi", "hiii"))

    def test_two_changes(self):
        self.assertFalse(oneAway("pale", "pqke"))

if __name__ == '__main__':
    unittest.main()