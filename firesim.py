import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
from perlin_numpy import generate_perlin_noise_2d
# np.random.seed(0) <-- if you want it to be repeatable

alphas = np.array([5.0, 1.0, 7.0, 1.0]) # wind from: top, bottom, left, right
# alphas = np.array([1.0,1.0,1.0,1.0]) # wind from: top, bottom, left, right

# Create NxN array with initial conditions
def create_initial_B():
    B0 = np.zeros((N,N))
    B0[N//2, N//2] = 0.3
    return B0.flatten()

# Create flamibilty 2d array
def create_flammibility():
    f = np.random.rand(N, N) # flammability constants
    # f = np.full((N,N), 0.5)

    # f = generate_perlin_noise_2d((N, N), (N//10, N//10))
    # f += 1
    # f **= 4
    return f

# Define the fire equation system
def fire_equation(t, b, N, f, alphas):
    B_grid = b.reshape((N, N))
    dBdt = np.zeros_like(B_grid)

    for (y, x), B in np.ndenumerate(B_grid):
        B = min(B, 1)
        neighbor_contributions = [alphas[i] * B_grid[y+dy, x+dx] \
                                  if 0 <= x+dx < N and 0 <= y+dy < N else 0.0 \
                                  for i,(dx,dy) in enumerate(offsets)]

        dBdt[y, x] = f[y, x] * B * (1 - B) + sum(neighbor_contributions)
    return dBdt.flatten()

# Define constants
N = 50  # grid size
t_max = 30
t_points = np.linspace(0, t_max, t_max * 20 - 1)  # time points to evaluate
offsets = [[0,-1], [0,1], [-1, 0], [1, 0]]
f = create_flammibility()
solution = solve_ivp(fire_equation, (0, t_max), create_initial_B(), args=(N, f, alphas / sum(alphas)), t_eval=t_points, method='RK45')
u_solutions = solution.y.reshape((N, N, solution.t.size)).transpose(2, 0, 1)

# animate
plt.imshow(f, cmap='gray', interpolation='nearest')
plt.colorbar()

fig, ax = plt.subplots()
image = ax.imshow(u_solutions[0], cmap='hot', interpolation='nearest', vmax=1, vmin=0)
plt.colorbar(image, ax=ax)
ax.set_title("System Evolution Over Time")

def update_animation(frame):
    image.set_array(u_solutions[frame])
    ax.set_title(f"Time: {solution.t[frame]:.2f}")

ani = FuncAnimation(fig, update_animation, frames=len(t_points), interval=50, blit=False)
plt.show()