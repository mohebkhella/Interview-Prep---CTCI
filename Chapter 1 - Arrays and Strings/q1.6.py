import unittest

# bad attempt at this problem - you over complicated it
def stringCompression(s):
    s_hashmap = [0] * 56
    for i in range(len(s)):
        if s[i].isupper():
            s_hashmap[ord(s[i]) - ord('A')] += 1
        else:
            s_hashmap[26 + ord(s[i]) - ord('a')] += 1
    
    used_chars = ""
    compressed_string = ""
    for i in range(len(s)):
        if s[i].isupper():
            if s_hashmap[ord(s[i]) - ord('A')] != 0 and s[i] not in used_chars:
                compressed_string += s[i] +  s_hashmap(ord(s[i]) - ord('A'))
                used_chars += s[i]
        else:
            if s_hashmap[ord(s[i]) - ord('a')] != 0:
                print("yo")
                compressed_string += s[i] +  s_hashmap(ord(s[i]) - ord('a'))
                used_chars += s[i]

    print(compressed_string)
    if len(compressed_string) >= len(s):
        return s    
    
    return compressed_string

# caching system to solve problem easily
def stringCompressionTwo(s):
    if len(s) == 0:
        return ""
    last_char = s[0]
    count_char = 0
    compressed_string = ""
    for i in range(len(s)):
        if s[i] != last_char or i == len(s) - 1:
            if i == len(s) - 1:
                count_char+=1
            compressed_string += last_char
            compressed_string += str(count_char)
            last_char = s[i]
            count_char = 1
        else:
            last_char = s[i]
            count_char += 1

    if len(compressed_string) >= len(s):
        return s     
    return compressed_string

# TESTING PURPOSES
class TestcheckPermutations(unittest.TestCase):
    def test_book_case(self):
        self.assertEqual(stringCompressionTwo("aabcccccaaa"), "a2b1c5a3")
    
    def test_s_is_better(self):
        self.assertEqual(stringCompressionTwo("abcde"), "abcde")

    def test_with_upper_case(self):
        self.assertEqual(stringCompressionTwo("AAAABBBDDEEff"), "A4B3D2E2f2")

    def test_base_case(self):
        self.assertEqual(stringCompressionTwo(""), "")

    def test_not_in_order(self):
        self.assertEqual(stringCompressionTwo("ccccAaaabbbb"), "c4A1a3b4")


if __name__ == '__main__':
    unittest.main()