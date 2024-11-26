import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Define the heat equation system
def heat_equation(t, b, N, f, alpha):
    B_grid = b.reshape((N, N))
    dBdt = np.zeros_like(B_grid)

    for (x, y), B in np.ndenumerate(B_grid):
        offsets = [[0,-1], [0,1], [-1, 0], [1, 0]]
        neighbors = [B_grid[y+dy, x+dx] for dx,dy in offsets \
            if 0 <= x+dx < N and 0 <=y+dy < N]
        B = min(B, 1)

        dBdt[y, x] = f[y, x] * B * (1 - B) + alpha * sum(neighbors) / len(neighbors)
    return dBdt.flatten()

N = 30  # grid size
f = np.random.rand(N, N) # flammability constants
# f = np.full((N,N), 0.5)
# print('flammability:')
# print(f)
alpha = 0.5 # fire spreading constant
B0 = np.zeros((N,N))
B0[N//2, N//2] = 0.3
B0 = B0.flatten()

t_max = 50

t_span = (0, t_max)  # time range
t_points = np.linspace(*t_span, t_max * 20)  # time points to evaluate

solution = solve_ivp(heat_equation, t_span, B0, args=(N, f, alpha), t_eval=t_points, method='RK45')
u_solutions = solution.y.reshape((N, N, solution.t.size)).transpose(2, 0, 1)

# animate
fig, ax = plt.subplots()
image = ax.imshow(u_solutions[0], cmap='hot', interpolation='nearest', vmax=1, vmin=0)
plt.colorbar(image, ax=ax)
ax.set_title("System Evolution Over Time")

def update_animation(frame):
    image.set_array(u_solutions[frame])
    ax.set_title(f"Time: {solution.t[frame]:.2f}")

ani = FuncAnimation(fig, update_animation, frames=solution.t.size, interval=50, blit=False)
plt.show()