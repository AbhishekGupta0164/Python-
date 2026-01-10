import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import random

# Set up the figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(0, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Christmas Tree with Blinking Lights 🎄')

# Tree trunk
z_trunk = np.linspace(0, 0.5, 10)
x_trunk = np.zeros_like(z_trunk)
y_trunk = np.zeros_like(z_trunk)
ax.plot(x_trunk, y_trunk, z_trunk, color='sienna', linewidth=5)

# Tree base (stand)
z_base = np.full(10, 0)
x_base = np.linspace(-0.1, 0.1, 10)
y_base = np.full(10, 0)
ax.plot(x_base, y_base, z_base, color='brown', linewidth=3)

# Tree foliage: stacked layers of green points
heights = np.array([2.8, 2.3, 1.8, 1.3, 0.8])
radii = np.array([0.8, 0.6, 0.5, 0.4, 0.3])
tree_points = []

for i, (h, r) in enumerate(zip(heights, radii)):
    theta = np.linspace(0, 2 * np.pi, 20)
    x_layer = r * np.cos(theta)
    y_layer = r * np.sin(theta)
    z_layer = np.full_like(theta, h)
    layer_points = ax.scatter(x_layer, y_layer, z_layer, c='darkgreen', s=50)
    tree_points.append(layer_points)

# Lights: random positions within the tree bounds, with initial states
num_lights = 30
light_positions = []
light_states = [random.choice([True, False]) for _ in range(num_lights)]
light_scatter = None

# Generate light positions: within conical bounds
for i in range(num_lights):
    # Random height between 0.5 and 2.8
    z = random.uniform(0.5, 2.8)
    # Radius decreases with height: approx r = 0.9 * (1 - z/3)
    max_r = 0.9 * (1 - z / 3)
    r = random.uniform(0, max_r)
    theta = random.uniform(0, 2 * np.pi)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    light_positions.append((x, y, z))

def update(frame):
    global light_states, light_scatter
    
    # Clear previous lights
    if light_scatter is not None:
        light_scatter.remove()
    
    # Current positions and colors based on state
    x_lights = [pos[0] for pos in light_positions]
    y_lights = [pos[1] for pos in light_positions]
    z_lights = [pos[2] for pos in light_positions]
    colors = ['yellow' if state else 'darkgreen' for state in light_states]
    sizes = [100 if state else 20 for state in light_states]
    
    light_scatter = ax.scatter(x_lights, y_lights, z_lights, c=colors, s=sizes)
    
    # Toggle some lights randomly
    for i in range(num_lights):
        if random.random() < 0.2:  # 20% chance to toggle
            light_states[i] = not light_states[i]
    
    # Rotate the view for 3D effect
    ax.view_init(elev=20, azim=frame % 360)
    
    return light_scatter,

# Animate
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=300, blit=False)

plt.show()

# To save animation (optional): ani.save('christmas_tree_3d.gif', writer='pillow')