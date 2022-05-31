import pytest
import glob
import json
from nonogramsolver import NonogramSolver
import nonogramgenerator

'''
send all json files
'''
def test_solver():
	for path in sorted(glob.glob('examples/*.json')):
		print(path)
		solver = NonogramSolver(path)
		solver.set_verbose(True)
		solver.solve()
		test_res = solver.__str__().replace('\n', '')
		res_path = path.replace('.json', '.res')
		with open(res_path, 'r') as f:
			res = ''.join(f.readlines()).replace('\n', '')
		assert(test_res == res)
		print('....checked')

'''
send all nonograms request in array format
'''
def test_generator_array():
	for path in sorted(glob.glob('examples/*.res')):
		print(path)
		with open(path) as f:
			ar = [line.strip() for line in f.readlines()]
			test_res = nonogramgenerator.array_to_nonogram(ar)
		res_path = path.replace('.res', '.json')
		with open(res_path, 'r') as f:
			res = json.load(f)
		assert(json.dumps(test_res) == json.dumps(res))
		print('....checked')

'''
send all nonograms request in string format
'''
def test_generator_str():
	for path in sorted(glob.glob('examples/*.res')):
		print(path)
		with open(path) as f:
			ar = '\n'.join([line.strip() for line in f.readlines()])
			test_res = nonogramgenerator.str_to_nonogram(ar)
		res_path = path.replace('.res', '.json')
		with open(res_path, 'r') as f:
			res = json.load(f)
		assert(json.dumps(test_res) == json.dumps(res))
		print('....checked')

'''
solve all nonogram jsons then send result to nonogramgenerator to generate initial nonogram jsons
'''
def test_cross_check():
	for path in sorted(glob.glob('examples/*.json')):
		print(path)
		solver = NonogramSolver(path)
		solver.solve()
		solver_res = solver.NONO < 2
		with open(path) as f:
			solver_inp = json.load(f)
		assert(solver_inp == nonogramgenerator.array_to_nonogram(solver_res))
		print('....checked')
