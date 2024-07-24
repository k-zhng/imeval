import matplotlib.pyplot as plt

imeter_entropy = {}

def add_value_to_key(key, value):
    if key not in imeter_entropy:
        imeter_entropy[key] = []
    imeter_entropy[key].append(value)

i = 0
with open('imeval\entropy_scores.txt', 'r') as file:
    for line in file:
        i += 1
        i %= 1000
        if(i != 1): continue
        fields = line.split(',')
        entry_name = fields[0]
        entropy = fields[1]
        add_value_to_key(entry_name, entropy)

j = 0
with open('imeval\intron_imeter_scores.txt', 'r') as file:
    for line in file:
        j += 1
        j %= 1000
        if(j != 1): continue
        fields = line.split(',')
        entry_name = fields[0]
        imeter_score = fields[3]
        add_value_to_key(entry_name, imeter_score)


x_values = [value[0] for value in imeter_entropy.values()]
y_values = [value[1] for value in imeter_entropy.values()]

# Create a line graph
plt.plot(x_values, y_values, marker='o')  # marker='o' adds a dot at each data point

# Add titles and labels
plt.title('Entropy vs. Imeter Score')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Display the graph
plt.show()

