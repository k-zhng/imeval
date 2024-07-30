import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import numpy.ma as ma
from scipy.spatial import cKDTree
from matplotlib.animation import FuncAnimation, PillowWriter

imeter_scores = {}
entropy_scores = {}
tot_expression_levels = {}
entropy_file = 'at_entropy_scores.txt'
intron_file = 'at_cutoff_intron_imeter_scores.txt'

def add_value_to_key(key, value, curr_dict):
    if key not in curr_dict:
        curr_dict[key] = - 2 ** 31
    curr_dict[key] = max(value, curr_dict[key])

with open(entropy_file, 'r') as file:
    for line in file:
        fields = line.split(',')
        entry_name = fields[0]
        entropy = float(fields[1])
        expression = float(fields[2])
        if expression > 0:
            expression = math.log(expression, math.e)
        if expression < 0:
            expression = 0
        add_value_to_key(entry_name, entropy, entropy_scores)
        add_value_to_key(entry_name, expression, tot_expression_levels)

with open(intron_file, 'r') as file:
    for line in file:
        fields = line.split(',')
        entry_name = fields[0]
        imeter_score = float(fields[3])
        add_value_to_key(entry_name, imeter_score, imeter_scores)

x_values = np.array(list(entropy_scores.values()))
tot_expression_values = np.array(list(tot_expression_levels.values()))
y_values = np.array(list(imeter_scores.values()))

# Generate a grid for the surface plot
x_grid, y_grid = np.meshgrid(np.linspace(x_values.min(), x_values.max(), 50),
                             np.linspace(y_values.min(), y_values.max(), 50))

# Interpolate total expression values for the grid using nearest method
z_grid = griddata((x_values, y_values), tot_expression_values, (x_grid, y_grid), method='nearest')

# Calculate the distance from each grid point to the nearest data point
tree = cKDTree(np.c_[x_values, y_values])
distances, _ = tree.query(np.c_[x_grid.ravel(), y_grid.ravel()], k=1)
distances = distances.reshape(x_grid.shape)

# Mask the grid where there is no nearby data
distance_threshold = 0.2  # Adjust this threshold as needed
z_grid = ma.masked_where(distances > distance_threshold, z_grid)

# Create a 3D surface plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Set color limits based on the range of tot_expression_values
vmin = tot_expression_values.min()
vmax = tot_expression_values.max()

surf = ax.plot_surface(x_grid, y_grid, z_grid, cmap='turbo', edgecolor='none', antialiased=True, vmin=vmin, vmax=vmax)

# Add titles and labels
ax.set_title('Entropy vs. IMEter Score in A. thaliana', fontdict={'fontsize': 18, 'fontweight': 'normal', 'fontfamily': 'Times New Roman'})
ax.set_xlabel('Entropy Values', fontdict={'fontsize': 12, 'fontweight': 'light', 'fontfamily': 'Times New Roman'})
ax.set_ylabel('IMEter Score', fontdict={'fontsize': 12, 'fontweight': 'light', 'fontfamily': 'Times New Roman'})
ax.set_zlabel('Log of Total Expression Levels', fontdict={'fontsize': 12, 'fontweight': 'light', 'fontfamily': 'Times New Roman'})

# Add color bar to show the scale
cbar = plt.colorbar(surf, ax=ax, pad=0.1)
cbar.set_label('Natural Log of Normalized Total Expression Levels')

# Variables for controlling the rotation direction
elev_direction = 1
azim_direction = 1
elev_angle = 30
azim_angle = 270

# Function to update the view angle
def update(frame):
    global elev_angle, azim_angle, elev_direction, azim_direction
    ax.view_init(elev=elev_angle, azim=azim_angle)
    elev_angle += elev_direction * 0.5
    azim_angle += azim_direction * 1
    if elev_angle >= 80 or elev_angle <= 0:
        elev_direction *= -1
    if azim_angle >= 330 or azim_angle <= 210:
        azim_direction *= -1
    return fig,

# Create the animation
ani = FuncAnimation(fig, update, frames=720, interval=20, blit=False)

# Save the animation as a gif
ani.save('3d_plot_rotation_v2.gif', writer=PillowWriter(fps=30))

plt.show()