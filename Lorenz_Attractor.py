from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x, y, z = 0.1, 0.1, 0.1
a, b, c = 10, 28, 8 / 3

xs, ys, zs, = [], [], []
for _ in range(10_000):
    dx, dy, dz = a * (y - x), (x * (b - z)) - y, (x * y) - (c * z)

    x += dx * 0.01
    y += dy * 0.01
    z += dz * 0.01

    xs += [x]
    ys += [y]
    zs += [z]

ax.plot(xs, ys, zs, color = 'brown')
plt.show()