import gzip

file = '../imeval/at_ime_tissues.txt.gz' # a. thaliana
model = 'at_kmer_imeter_scores.txt'
# file = 'os_ime_tissues.txt' # o. sativa
# model = 'os_kmer_imeter_scores.txt'

def load_model(file_path):
    model_dict = {}

    file_handle = None
    if file_path.endswith('.gz'):
        file_handle = gzip.open(file_path, 'rt')
    else:
        file_handle = open(file_path)

    with file_handle:
        for line in file_handle.readlines():
            if line.startswith('#'):
                continue
            kmer, metric, _, _ = line.split()
            model_dict[kmer] = float(metric)

    return model_dict

def evaluate_intron(model_dict, sequence, kmer_length, offset=5, adjust=10):
    score = 0
    for index in range(offset, len(sequence) - kmer_length + 1 - adjust):
        kmer = sequence[index:index + kmer_length]
        if kmer in model_dict:
            score += model_dict[kmer]
    return score

def cutoff_evaluate_intron(model_dict, sequence, kmer_length, cutoff, offset=5, adjust=10):
    score = 0
    for index in range(offset, len(sequence) - kmer_length + 1 - adjust):
        if index > cutoff:
            break
        kmer = sequence[index:index + kmer_length]
        if kmer in model_dict:
            score += model_dict[kmer]
    return score

model_dict = load_model(model)
kmer_length = len(list(model_dict.keys())[0])
proximal_cutoff = 400

if file.endswith('.gz'):
    file_handle = gzip.open(file, 'rt')
else:
    file_handle = open(file, 'r')

with file_handle:
    for line in file_handle.readlines():
        fields = line.split()
        entry_name = fields[0]
        start = fields[1]
        stop = fields[2]
        sequence = fields[-1]
        # intron_score = evaluate_intron(model_dict, sequence, kmer_length) #no cutoff
        intron_score = cutoff_evaluate_intron(model_dict, sequence, kmer_length, proximal_cutoff) #with cutoff of proximal_cutoff
        print(entry_name, start, stop, intron_score, sep=',')