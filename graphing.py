import matplotlib.pyplot as plt
import argparse
import numpy as np
import math

imeter_scores = {}
entropy_scores = {}
tot_expression_levels = {}

def add_value_to_key(key, value, curr_dict):
    if key not in curr_dict:
        curr_dict[key] = - 2 ** 31
    curr_dict[key] = max (value, curr_dict[key])

with open('imeval\entropy_scores.txt', 'r') as file:
    for line in file:
        fields = line.split(',')
        entry_name = fields[0]
        entropy = float(fields[1])
        expression = float(fields[2])
        if (expression > 0):
            expression = math.log(expression)
        add_value_to_key(entry_name, entropy, entropy_scores)
        add_value_to_key(entry_name, expression, tot_expression_levels)

with open('imeval\cutoff_intron_imeter_scores.txt', 'r') as file:
    for line in file:
        fields = line.split(',')
        entry_name = fields[0]
        imeter_score = float(fields[3])
        add_value_to_key(entry_name, imeter_score, imeter_scores)

x_values = np.array(list(entropy_scores.values()))
tot_expression_values = np.array(list(tot_expression_levels.values()))
y_values = np.array(list(imeter_scores.values()))

# sorted_indices = np.argsort(tot_expression_values)
# print(sorted_indices)
# x_values = x_values[sorted_indices]
# y_values = y_values[sorted_indices]
# tot_expression_values = tot_expression_values[sorted_indices]


# Create a line graph
plt.scatter(x_values, y_values, c = tot_expression_values, cmap = 'turbo', s = 1)

# Add titles and labels
plt.title('Entropy vs. IMEter Score (With threshold)')
plt.xlabel('Entropy Values')
plt.ylabel('IMEter Score')

# Set limit to y-axis
plt.ylim(bottom=-75)  # Lower limit of the y-axis
plt.ylim(top=125)  # Upper limit of the y-axis


# Add color bar to show the scale
plt.colorbar(label='Total Expression Levels')

# Display the graph
plt.show()