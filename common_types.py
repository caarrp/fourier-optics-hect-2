from math import sin, cos, pi, exp, sqrt
resolution = 12
bounds = 2

#rect(x)

#triangle(x)

#sinc(x)
def sinc_x_sinc_y(scalar_x = 1, shift = 0, scalar_y = 1, shift_y = 0):

    x = []
    y = []

    for i in range(resolution):
        x_val = ((i / resolution) * 2 * bounds) - bounds
        y_val = ((i / resolution) * 2 * bounds) - bounds

        if x_val - shift == 0:
            x.append(1)
        else:
            x.append(sin(pi * scalar_x * (x_val - shift)) / (pi * scalar_x * (x_val - shift)))

        if y_val - shift_y == 0:
            y.append(1)
        else:
            y.append(sin(pi * scalar_y * (y_val - shift_y)) / (pi * scalar_y * (y_val - shift_y)))

    return x, y

#gaussian(x)? copilot gave me this one

if __name__ == "__main__":
    print(sinc_x_sinc_y())