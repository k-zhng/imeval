import argparse
import random

parser = argparse.ArgumentParser(description='Generate random features')
parser.add_argument('count', type=int, help='number of features to generate')
parser.add_argument('--chromosomes', type=int, default=20,
	help='number of chromosomes [%(default)i]')
parser.add_argument('--size', type=float, default=1e7,
	help='size of chromosomes [%(default)f]')
parser.add_argument('--min', type=int, default=1,
	help='minimum feature length [%(default)i]')
parser.add_argument('--max', type=int, default=10000,
	help='maximum feature length [%(default)i]')
arg = parser.parse_args()

for i in range(arg.count):
	chrom = random.randint(1, arg.chromosomes)
	beg = random.randint(1, arg.size)
	end = beg + random.randint(arg.min, arg.max)
	print(f'Chr{chrom}\t{beg}\t{end}')
