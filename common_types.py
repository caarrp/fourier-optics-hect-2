from math import sin, cos, pi, exp, sqrt
resolution = 12
bounds = 2

#rect(x)

#triangle(x)

#sinc(x)
def sinc_x_sinc_y(scalar_x=1, shift_x=0, scalar_y=1, shift_y=0, bounds=5, resolution=100):
    """
    Your precise implementation with manual point calculation
    Returns X, Y, Z arrays for plotting
    """
    x = []
    y = []
    z = []
    
    for i in range(resolution):
        # Calculate x and y values
        x_val = ((i / resolution) * 2 * bounds) - bounds
        y_val = ((i / resolution) * 2 * bounds) - bounds
        
        # Sinc calculation for x
        if x_val - shift_x == 0:
            sinc_x = 1
        else:
            sinc_x = sin(pi * scalar_x * (x_val - shift_x)) / (pi * scalar_x * (x_val - shift_x))
        
        # Sinc calculation for y
        if y_val - shift_y == 0:
            sinc_y = 1
        else:
            sinc_y = sin(pi * scalar_y * (y_val - shift_y)) / (pi * scalar_y * (y_val - shift_y))
        
        x.append(x_val)
        y.append(y_val)
        z.append(sinc_x * sinc_y)  # z = sinc(x) * sinc(y)
  
    return x, y, z
#gaussian(x)? copilot gave me this one

if __name__ == "__main__":
    print(sinc_x_sinc_y())