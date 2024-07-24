import gzip
import numpy as np

def calculate_shannon_entropy(data):
    total = sum(data)
    if (total == 0):
        return 0
    probabilities = [x / total for x in data]
    entropy = -sum(p * np.log2(p) for p in probabilities if p > 0)
    return entropy


with gzip.open('../imeval/at_ime_tissues.txt.gz', 'rt') as file_handle:
    for line in file_handle.readlines():
        fields = line.split()
        entry_name = fields[0]
        expression = []
        for i in range(4, 15):
            expression.append(int(fields[i]))
        print(entry_name, calculate_shannon_entropy(expression), sep=',')