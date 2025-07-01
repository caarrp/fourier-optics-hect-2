import plotly.graph_objects as go
import numpy as np
from common_types import sinc_x_sinc_y

# 3D meshgrid 

def test_plotly(sinc = False, rect = False, triangle = False, gaussian = False):

    if sinc:
        x, y, z = sinc_x_sinc_y()
        xu, yv = np.meshgrid(x, y)
        zw = np.outer(z, z)

    fig = go.Figure(data=[go.Surface(z=zw, x=xu, y=yv)])
    fig.update_layout(
        title='Your Sinc Function Calculation',
        scene=dict(
            xaxis_title='x',
            yaxis_title='y',
            zaxis_title='sinc(x)*sinc(y)'
        )
    )
    fig.show()

if __name__ == "__main__":
    test_plotly(sinc = True)