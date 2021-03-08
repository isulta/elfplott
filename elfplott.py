import numpy as np
import matplotlib.pyplot as plt

class RestFrame:
    coords1d = np.linspace(-5,5,20)
    X, Y = np.meshgrid(coords1d, coords1d)
    
    def __init__(self):
        self.Ex = np.zeros_like(RestFrame.X)
        self.Ey = np.zeros_like(RestFrame.X)
        self.point_charges = []
    
    def plot(self, show_charges=True):
        plt.figure(dpi=150)
        plt.streamplot(self.X, self.Y, self.Ex, self.Ey, density=2, linewidth=.5)

        if show_charges:
            for xq, yq, q in self.point_charges:
                if (np.abs(xq)<=RestFrame.coords1d[-1]) and (np.abs(yq)<=RestFrame.coords1d[-1]):
                    plt.scatter(xq, yq, marker=('_' if q<0 else '+'), c=('k' if q<0 else 'r'), zorder=4, s=100)
        
        plt.show()

    def add_point_charge(self, xq, yq, q):
        X1 = self.X - xq
        Y1 = self.Y - yq
        Phi1 = np.arctan2(Y1, X1)
        self.Ex += q*np.cos(Phi1) / (X1**2 + Y1**2)
        self.Ey += q*np.sin(Phi1) / (X1**2 + Y1**2)

        self.point_charges.append((xq, yq, q))
    
    def add_point_charges(self, x_coords, y_coords, charges):
        for xq, yq, q in zip(x_coords, y_coords, charges):
            self.add_point_charge(xq, yq, q)