import numpy as np
import matplotlib.pyplot as plt

prev_base = next_base = []
timesteps = 150
nz = nx = 256
dx = dz = 15
dt = 0.005774
vel = 1500.0
stencil_radius = 1

# Inicializar matrizes:

for z in range(nz*nx):
    prev_base.append(0.0)
    next_base.append(0.0)

# Criar fonte inicial

val = 1.0

for s in range(5,-1,-1):
    for i in range(int(nz/2)-s, int(nz/2)+s):
        offset = i * nx

        for j in range(int(nx/2)-s, int(nx/2)+s):
            prev_base[offset + j] = val
    val *= 10

# Executar

for n in range(timesteps):
    for i in range(stencil_radius, nz - stencil_radius):
        for j in range(stencil_radius, nx - stencil_radius):
            current = i * nx + j
            value = 0.0
            value += (prev_base[current + 1] - 2.0*prev_base[current] + prev_base[current - 1]) / (dx*dx)
            value += (prev_base[current + nx] - 2.0*prev_base[current] + prev_base[current - nx]) / (dz*dz)
            value *= (dt * dt) * vel * vel
            next_base[current] = 2.0*prev_base[current] - next_base[current] + value
    
    swap = next_base
    next_base = prev_base
    prev_base = swap

# Plot

with open('wavefield_v1.txt', 'w') as f:
    for i in range(0, nz):
        offset = i * nx
        
        for j in range(0, nx):
            f.write("{} ".format(next_base[offset + j]))

        f.write('\n')
f.close()

input = np.loadtxt('wavefield_v1.txt')

plt.imshow(input)
plt.savefig('plot_v1.png', format='png')