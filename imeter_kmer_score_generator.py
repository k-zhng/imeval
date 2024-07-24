import argparse
import gzip
import math


def make_kmer(k, init=0, alph='ACGT'):
    def generate_kmers(prefix, length):
        if length == 0:
            yield prefix
        else:
            for char in alph:
                yield from generate_kmers(prefix + char, length - 1)

    make_kmer = {}
    for kmer in generate_kmers('', k):
        make_kmer[kmer] = init

    return make_kmer

def count2freq(count):
	freq = {}
	total = 0
	for k in count: total += count[k]
	for k in count: freq[k] = count[k] / total
	return freq

def training(filename, k=5, d=5, a=10, t=400):

	# counts
	prox = make_kmer(k, init=1)
	dist = make_kmer(k, init=1)

	fp = gzip.open(filename, 'rt')

	for line in fp.readlines():
		f = line.split()
		beg = int(f[1])
		seq = f[-1]
		for i in range(d, len(seq) - k + 1 - a):
			kmer = seq[i:i+k]
			if kmer not in prox: continue
			if beg <= t: prox[kmer] += 1
			else:        dist[kmer] += 1

	# freqs
	pfreq = count2freq(prox)
	dfreq = count2freq(dist)
	imeter = {}
	for kmer in pfreq:
		imeter[kmer] = math.log2(pfreq[kmer] / dfreq[kmer])

	# done
	return imeter, pfreq, dfreq

# CLI

file = '../imeval/at_ime_tissues.txt.gz'
don_change = 5
acc_change = 10
cut_change =  400
k_change = 5
# Main

imeter, prox, dist = training(file, t = cut_change, k = k_change,
	a = acc_change, d = don_change)

# Output
print('# kmer, imeter, prox, dist')
for k in imeter:
	print(k, imeter[k], prox[k], dist[k])