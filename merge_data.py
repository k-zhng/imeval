import gzip

# Function to read file and return dictionary
def read_file1(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            id_ = parts[0]
            data[id_] = parts[1:]  # Store rest of the parts
    return data

def read_file2(filename):
    data = {}
    with gzip.open(filename, 'rt') as file:
        for line in file:
            parts = line.strip().split('\t')
            id_ = parts[0].rsplit('.', 1)[0]  # Remove the decimal part
            data[id_] = parts[1:]  # Store rest of the parts
    return data

# Read the first file
file1 = '../imeval/o.sativa.expression.txt'
data1 = read_file1(file1)

# Read the second file
file2 = '../imeval/os_ime_notissues.txt.gz'
data2 = read_file2(file2)

# Merge the data and print each line
for id_ in data1:
    if id_ in data2:
        merged_line = [id_] + data2[id_][:3] + data1[id_][:16] + data2[id_][3:]
        print('\t'.join(merged_line))