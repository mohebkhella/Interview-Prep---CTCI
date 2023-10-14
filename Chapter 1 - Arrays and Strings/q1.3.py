import unittest

def URLify(url, n):
    if n ==0: 
        return ""

    new_url = ""
    for i in range(n):
        if url[i] == " ":
            new_url += "%20"
        else:
            new_url += url[i]
    return new_url

# TESTING PURPOSES
class TestcheckPermutations(unittest.TestCase):
    def test_book_case(self):
        self.assertEqual(URLify("Mr John Smith", 13), "Mr%20John%20Smith")

    def test_base_vase(self):
        self.assertEqual(URLify("", 0), "")

    def test_one_space(self):
        self.assertEqual(URLify("yo how", 6), "yo%20how")
    
    def test_no_space(self):
        self.assertEqual(URLify("chicken", 7), "chicken")

    def test_double_space(self):
        self.assertEqual(URLify("double  space", 13), "double%20%20space")

if __name__ == '__main__':
    unittest.main()