# Given a space separated list of numbers. 
# Task is to print a reversed NumPy array with the element type float.

import unittest, numpy as np

class TestNumpy(unittest.TestCase):
    def test_helloworld(self):
        self.assertEqual(arrays([1, 2, 3, 4, 5]), "[5. 4. 3. 2. 1.]")

def arrays(arr):
    new_arr = np.array(arr,float)
    return np.flip(new_arr)

def main():
#    arr = input().strip().split(' ')
    arr = 1, 2, 3, 4, 5
    result = arrays(arr)
    print(result)

if __name__ == '__main__':
    main()
#    unittest.main()