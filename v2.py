import numpy as np
import matplotlib.pyplot as plt

prev_base = next_base = []
timesteps = 150
nz = nx = 256
dx = dz = 20
dt = 0.002
vel = 1500.0
stencil_radius = 8

start = nx
end = nx * (nz - stencil_radius)
low_limit = nx + stencil_radius - 1
high_limit = nx - stencil_radius
div_dz2 = 1.0 / (dz * dz)
div_dx2 = 1.0 / (dx * dx)
dt2Xvel2 = (dt * dt) * pow(vel, 2)

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
    for i in range(start, end):
        #print(str(i % low_limit) + " > " + str(low_limit))
        #print(str(i % high_limit) + " < " + str(high_limit))
        #if (i % low_limit > low_limit) and (i % high_limit < high_limit):
            value = (prev_base[i] * div_dz2 + prev_base[i] * div_dx2)
            value += (prev_base[i] * div_dz2 + prev_base[i] * div_dx2)
            value += (((prev_base[i + 1] + prev_base[i - 1]) * div_dx2 ) + ((prev_base[i + nx] + prev_base[i - nx]) * div_dz2))
            value *= dt2Xvel2
            next_base[i] = (prev_base[i] + prev_base[i]) - next_base[i] + value
    
    swap = next_base
    next_base = prev_base
    prev_base = swap

# Plot

with open('wavefield_v2.txt', 'w') as f:
    for i in range(0, nz):
        offset = i * nx
        
        for j in range(0, nx):
            f.write("{} ".format(next_base[offset + j]))

        f.write('\n')
f.close()

input = np.loadtxt('wavefield_v2.txt')

plt.imshow(input)
plt.savefig('plot_v2.png', format='png')