import matplotlib.pyplot as plt

imeter_scores = {}
entropy_scores = {}

def add_value_to_key(key, value, curr_dict):
    if key not in curr_dict:
        curr_dict[key] = - 2 ** 31
    curr_dict[key] = max (value, curr_dict[key])

with open('imeval\entropy_scores.txt', 'r') as file:
    for line in file:
        fields = line.split(',')
        entry_name = fields[0]
        entropy = float(fields[1])
        add_value_to_key(entry_name, entropy, entropy_scores)

with open('imeval\intron_imeter_scores.txt', 'r') as file:
    for line in file:
        fields = line.split(',')
        entry_name = fields[0]
        imeter_score = float(fields[3])
        add_value_to_key(entry_name, imeter_score, imeter_scores)

x_values = list(entropy_scores.values())
y_values = list(imeter_scores.values())

print(x_values)
print(y_values)

# Create a line graph
plt.scatter(x_values, y_values, marker=".")

# Add titles and labels
plt.title('Entropy vs. IMEter Score')
plt.xlabel('Entropy Values')
plt.ylabel('IMEter Score')

# Display the graph
plt.show()

# print(imeter_scores)
# print(entropy_scores)