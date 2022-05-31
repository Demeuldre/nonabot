#!/usr/bin/env python3

import json
import os
from sqlite3 import enable_shared_cache
import sys
import numpy as np
import math
import itertools
import argparse
from nonosolving import *

## TODO: there is a problem where one of cells might switch to next cell
## to reproduce use example 6

# 0-'*': unknown
# 1-'X': black
# 2-'.': white
NCH = ['*', 'X', '.']

class NonogramSolver(object):
	def __init__(self, path):
		self.marks = []
		with open(path, 'r') as f:
			self.marks = json.load(f)
		self._verbose = False
		self.__print(self.marks)

		self.RC = len(self.marks['r'])
		self.CC = len(self.marks['c'])

		self.NONO = np.zeros((self.RC, self.CC), dtype=np.int)

	def __str__(self):
		return '\n'.join([''.join([NCH[c] for c in r]) for r in self.NONO])

	def set_verbose(self, verbose):
		self._verbose = verbose

	'''
	row solving algorithm:
	generate all combinations that doesn't violate previously found cells
	for each possible combination mark common cells
	return result of common cells as new solution row

	@param ar: Array an array of count of consecutive black marks
	@param ref: int current solution for this row
	@return Array yielded possible combination of marks starting starting and ending with num of empty
	'''
	@staticmethod
	def solve_row(ar, ref):
		if np.sum(ref == 0) == 0:
			return ref
		N = len(ref)
		K = N - sum(ar)
		res_ar = False
		for comb in itertools.combinations(range(0, K+1), len(ar)):
			c_ar = [0] + list(comb) + [K] # combination position array
			w_ar = [c_ar[i+1]-c_ar[i] for i in range(len(c_ar)-1)] # zero count array

			w_ar = [[2]*x for x in w_ar] # white int array
			b_ar = [[1]*x for x in ar] # black int array


			for i,v in enumerate(b_ar): # merge two string arrays to generate possible placement
				w_ar.insert(2*i+1, v)
		
			res = [x for r in w_ar for x in r]
			
			match = True
			for i in range(N):
				if ref[i] == 0 or ref[i] == res[i]:
					continue
				match = False
				break
			if not match:
				continue
			if not res_ar:
				res_ar = res
				continue
			for i in range(N):
				if res_ar[i] != res[i]:
					res_ar[i] = 0
		return np.array(res_ar)
		
		


	'''
	@param ar: Array an array of consecutive black marks
	@param N: int total of
	@return int number of possible combination of marks
	'''
	@staticmethod
	def get_probs_count(ar, N):
		N -= sum(ar) - 1
		R = len(ar)
		f = math.factorial
		return f(N)/f(N-R)/f(R)

	def __print(self, *args, **kwargs):
		if self._verbose:
			print(*args, **kwargs)

	'''
	Algorithm is very simple:
	repeat until all cells are solved:
		turn every column and row into rows
		solve for generated row
		update result matrix
	@param self
	'''
	def solve(self):
		pass_cnt = 1
		while np.sum(self.NONO == 0) != 0:
			self.__print('Pass:', pass_cnt)
			# TODO: add check if get any improvements
			# pass rows
			for i, r in enumerate(self.marks['r']):
				self.NONO[i, :] = NonogramSolver.solve_row(r, self.NONO[i])
			# pass cols
			for j, c in enumerate(self.marks['c']):
				self.NONO[:, j] = NonogramSolver.solve_row(c, self.NONO[:, j])
			self.__print(self)
			pass_cnt += 1


def solve(path):
	return NonogramSolver(path).solve()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', required=True, help='nongram file in json format')
	args = parser.parse_args()

	solver = NonogramSolver(args.file)
	solver.solve()
	print('Solution:\n', solver, sep='')
	
	
	f = open("Nonogram.txt", "w")
	print(solver, file=f)
	f.close()
	lines = []
	with open("Nonogram.txt", "r") as f:
		lines = f.readlines()
    
	array_to_nonosolver = []
	count = 0
	rows = 0
	for line in lines:
		for character in line:
			if character == 'X':
				array_to_nonosolver.append(1)
			elif character == '.':
				array_to_nonosolver.append(0)
			else:
				continue
		columns = len(line) - 1
		count += 1
	rows = count
 
	checkParameters(rows, columns, array_to_nonosolver)
	printBoard(rows, columns, array_to_nonosolver)
