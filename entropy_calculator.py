import gzip
import numpy as np

def calculate_shannon_entropy(data):
    total = sum(data)
    if (total == 0):
        return -1
    probabilities = [x / total for x in data]
    entropy = -sum(p * np.log2(p) for p in probabilities if p > 0)
    return entropy

expression_sum = [0] * 11

with gzip.open('../imeval/at_ime_tissues.txt.gz', 'rt') as file_handle:
    for line in file_handle.readlines():
        fields = line.split()
        entry_name = fields[0]
        for i in range(4, 15):
            expression_sum[i - 4] += int(fields[i])


with gzip.open('../imeval/at_ime_tissues.txt.gz', 'rt') as file_handle:
    for line in file_handle.readlines():
        fields = line.split()
        entry_name = fields[0]
        expression = []
        total_expression = 0
        for i in range(4, 15):
            curr_expression = int(fields[i])
            expression.append(curr_expression/expression_sum[i - 4])
            total_expression += curr_expression
        print(entry_name, calculate_shannon_entropy(expression), total_expression, sep=',')