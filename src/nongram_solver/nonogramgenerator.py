#!/usr/bin/env python3
import numpy as np
import json
import argparse
import sys

# 0-'*': unknown
# 1-'X': black
# 2-'.': white
NCH = ['*', 'X', '.']

class NonogramGenerator(object):
	"""docstring for NonogramGenerator"""
	def __init__(self):
		super(NonogramGenerator, self).__init__()

	@staticmethod
	def _count_rows(ar):
		res = []
		for row in ar:
			row_res = []
			cnt = 0
			for v in row:
				if v == True:
					cnt += 1
				elif cnt != 0:
					row_res.append(cnt)
					cnt = 0
			if cnt != 0:
				row_res.append(cnt)
			res.append(row_res)
		return res

	@staticmethod
	def array_to_nonogram(ar):
		rows = []
		cols = []
		# make sure we get numpy array for shape and all
		ar = np.array(ar)
		# fix for array of strings
		if len(ar.shape) == 1 and type(ar[0]) == np.str_:
			ar = np.array([list(s.lower()) for s in ar])
			if sum(sum(ar == '.') + sum(ar == 'x') + sum(ar == 'X')) != ar.size:
				raise ValueError('Can only contain ., x, and X')
			ar = (ar != '.')
		elif len(ar.shape) == 2:
			ar = np.array(ar, dtype=np.bool)
		else:
			raise ValueError('Must receive an array of 2 dimensions')
		ar = (ar != 0) # convert to a bool array
		res = {
				'r': NonogramGenerator._count_rows(ar),
				'c': NonogramGenerator._count_rows(np.transpose(ar))
			}
		
		return res

	@staticmethod
	def str_to_nonogram(ar):
		if type(ar) is str:
			ar = ar.split('\n')
		return NonogramGenerator.array_to_nonogram(ar)

def array_to_nonogram(ar):
	return NonogramGenerator.array_to_nonogram(ar)

def str_to_nonogram(ar):
	return NonogramGenerator.str_to_nonogram(ar)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-f', '--file', help='nongram file in . and x format')
	group.add_argument('-s', '--str', help='nongram string in . and x format')
	args = parser.parse_args()

	if args.file:
		with open(args.file, 'r') as f:
			ar = [[c for c in line.strip()] for line in f]
			print(json.dumps(NonogramGenerator.array_to_nonogram(ar)))
	else:
		print(json.dumps(NonogramGenerator.str_to_nonogram(args.str)))
