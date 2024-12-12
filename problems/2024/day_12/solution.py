import argparse
from collections import deque

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = self.file.splitlines()

  def create_grid(self):
    #initialize a dictionary, and then traverse the lines adding the value at each grid point.
    grid = {}
    for i, row in enumerate(self.lines):
      for j, val in enumerate(row):
        grid[(i,j)] = val
    return grid

  def island(grid, start):
    visited = set()
    Q = deque([start])

    while Q:





  def part1(self):
    pass
  
  def part2(self):
    pass
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
