import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sin, pi

def sinc_x_sinc_y(bounds=5, resolution=100):
    """Calculate sinc(x)*sinc(y) manually"""
    x = []
    y = []
    z = []
    
    for i in range(resolution):
        val = ((i / resolution) * 2 * bounds) - bounds
        x.append(val)
        y.append(val)
        
        # Calculate sinc(x)
        if val == 0:
            sinc_x = 1
        else:
            sinc_x = sin(pi * val) / (pi * val)
        
        # Calculate sinc(y) (same as sinc_x in this case)
        z.append(sinc_x * sinc_x)  # z = sinc(x)*sinc(y)
    
    return x, y, z

def rect_x_rect_y(bounds=5, resolution=100):
    """Rectangular function rect(x)*rect(y)"""
    x = np.linspace(-bounds, bounds, resolution)
    y = np.linspace(-bounds, bounds, resolution)
    X, Y = np.meshgrid(x, y)
    Z = np.where((np.abs(X) <= 0.5) & (np.abs(Y) <= 0.5), 1, 0)
    return X, Y, Z

def triangle_x_triangle_y(bounds=5, resolution=100):
    """Triangular function tri(x)*tri(y)"""
    x = np.linspace(-bounds, bounds, resolution)
    y = np.linspace(-bounds, bounds, resolution)
    X, Y = np.meshgrid(x, y)
    tri = lambda t: np.where(np.abs(t) < 1, 1 - np.abs(t), 0)
    Z = tri(X) * tri(Y)
    return X, Y, Z

def gaussian_2d(bounds=5, resolution=100, sigma=1):
    """2D Gaussian function"""
    x = np.linspace(-bounds, bounds, resolution)
    y = np.linspace(-bounds, bounds, resolution)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X**2 + Y**2)/(2*sigma**2))
    return X, Y, Z

def test_plotly(sinc=False, rect=False, triangle=False, gaussian=False):
    # Determine which function to plot
    if sinc:
        x, y, z = sinc_x_sinc_y()
        xu, yv = np.meshgrid(x, y)
        zw = np.outer(z, z)
        title = 'Sinc Function: sinc(x)*sinc(y)'
    elif rect:
        xu, yv, zw = rect_x_rect_y()
        title = 'Rectangular Function: rect(x)*rect(y)'
    elif triangle:
        xu, yv, zw = triangle_x_triangle_y()
        title = 'Triangular Function: tri(x)*tri(y)'
    elif gaussian:
        xu, yv, zw = gaussian_2d()
        title = '2D Gaussian Function'
    else:
        raise ValueError("No function selected")

    # Plotly 3D Surface Plot
    # fig = go.Figure(data=[go.Surface(z=zw, x=xu, y=yv, colorscale='Viridis')])
    # fig.update_layout(
    #     title=title,
    #     scene=dict(
    #         xaxis_title='x',
    #         yaxis_title='y',
    #         zaxis_title='Amplitude',
    #         camera=dict(eye=dict(x=1.5, y=1.5, z=0.8))
    # )
    # fig.show()

    # Matplotlib Wireframe Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(xu, yv, zw, rstride=5, cstride=5)
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('Amplitude')
    plt.show()

if __name__ == "__main__":
    test_plotly(sinc=True)  