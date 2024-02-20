from math import sin, cos, exp
import numpy as np
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=12)
noise4 = PerlinNoise(octaves=24)
noise5 = PerlinNoise(octaves=48)


def gaussian(amplitude, x_centre, y_centre, x_spread, y_spread, rotation, x, y):
    a = cos(rotation)**2 / (2 * x_spread ** 2) + sin(rotation)**2 / (2 * y_spread ** 2)
    b = (-1 * sin(rotation) * cos(rotation)) / x_spread**2 + (sin(rotation) * cos(rotation)) / y_spread**2
    c = sin(rotation)**2 / (2 * x_spread ** 2) + cos(rotation)**2 / (2 * y_spread ** 2)
    dist_x, dist_y = x - x_centre, y - y_centre
    exponent = (a * dist_x**2) + (2 * b * dist_x * dist_y) + (c * dist_y**2)
    return amplitude * exp(-1 * exponent)


x_pixels, y_pixels = 300, 300
pic = np.zeros((300, 300))
for i in range(x_pixels):
    for j in range(y_pixels):
        pic[i][j] = -0.5
        pic[i][j] += noise1([i / x_pixels, j / y_pixels])
        pic[i][j] += 0.5 * noise2([i / x_pixels, j / y_pixels])
        pic[i][j] += 0.25 * noise3([i / x_pixels, j / y_pixels])
        pic[i][j] += 0.125 * noise4([i / x_pixels, j / y_pixels])
        pic[i][j] += 0.03 * noise5([i / x_pixels, j / y_pixels])
        pic[i][j] += gaussian(1.2, 150, 150, 80, 80, 0, i, j)
        if pic[i][j] < 0:
            pic[i][j] = -1

plt.imshow(pic, cmap='viridis')
plt.show()
