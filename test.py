grid_sizes = [64, 128, 256, 512, 1024]
stencil_radius_sizes = [2, 4, 8, 16, 32, 64]

for sr in range (0, 6):
    stencil_radius = stencil_radius_sizes[sr]
    for grid in range(1, 5):
        nx = nz = grid_sizes[grid]
        start = nx
        end = nx * (nz - stencil_radius)
        low_limit = nx + stencil_radius - 1
        high_limit = nx - stencil_radius
        print(str(stencil_radius) + " " + str(nx))
        for i in range(start, end):
            if (i % low_limit > low_limit) and (i % high_limit < high_limit):
                print('Run!')