import matplotlib.pyplot as plt

imeter_entropy = {}

def add_value_to_key(key, value):
    if key not in imeter_entropy:
        imeter_entropy[key] = []
    imeter_entropy[key].append(value)

i = 0
min_entropy = 2**31 - 1
max_entropy = -2**31
with open('imeval\entropy_scores.txt', 'r') as file:
    for line in file:
        i += 1
        i %= 100
        if(i != 1): continue
        fields = line.split(',')
        entry_name = fields[0]
        entropy = float(fields[1])
        min_entropy = min(min_entropy, entropy)
        max_entropy = max(max_entropy, entropy)
        add_value_to_key(entry_name, entropy)
print(min_entropy, max_entropy)

j = 0
min_imeter = 2**31 - 1
max_imeter = -2**31
with open('imeval\intron_imeter_scores.txt', 'r') as file:
    for line in file:
        j += 1
        j %= 100
        if(j != 1): continue
        fields = line.split(',')
        entry_name = fields[0]
        imeter_score = float(fields[3])
        min_imeter = min(min_imeter, imeter_score)
        max_imeter = max(max_imeter, imeter_score)
        add_value_to_key(entry_name, imeter_score)
print(min_imeter, max_imeter)

x_values = [value[0] for value in imeter_entropy.values()]
y_values = [value[1] for value in imeter_entropy.values()]

# Create a line graph
plt.scatter(x_values, y_values, marker=".")

# Add titles and labels
plt.title('Entropy vs. IMEter Score')
plt.xlabel('Entropy Values')
plt.ylabel('IMEter Score')

# Display the graph
plt.show()