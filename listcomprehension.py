# You are given three integers and  representing the dimensions of a cuboid along with an integer . 
# Print a list of all possible coordinates given by  on a 3D grid where the sum of x,y,z is not equal to n

# Added unit tests and logic.  This is a good example of how to use list comprehension

import unittest

class TestCuboid(unittest.TestCase):
    def test_cuboid_1112(self):
        self.assertEqual(cuboid(1,1,1,2), [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]])
    def test_cuboid_2222(self):
        self.assertEqual(cuboid(2,2,2,2), [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]])

def cuboid(x,y,z,n):
    newlist = [[i,j,k] for i in range(x+1) for j in range(y + 1) for k in range(z + 1)]
    copied = []
    for l in newlist:
         if sum(l) != n:
             copied.append(l)
    return copied

def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(cuboid(x,y,z,n))

if __name__ == '__main__':

# generates the grid points
#   main()
        
# testing the output against standard inputs
    try:        
        unittest.main()
    except:
        print("=)")
 
 