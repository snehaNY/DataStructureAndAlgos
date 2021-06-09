import unittest

from collections import Counter
def isSubstring(string,sub_string):
    if string == sub_string:
        return True
    if sub_string.strip() == "":
        return True
    c = Counter()
    for s in string:
        c[s] +=1
    for sub in sub_string:
        if sub in c and c[sub]>0:
            c[sub] -=1
        else:
            return False
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = isSubstring(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
            


