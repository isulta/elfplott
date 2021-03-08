import numpy as np
import matplotlib.pyplot as plt
np.seterr(divide='ignore')

class RestFrame:
    coords1d = np.linspace(-5,5,20)
    X, Y, Z = np.meshgrid(coords1d, coords1d, np.linspace(-5,5,21))
    z0 = 10 # index of z-dimension coressponding to z=0 (i.e. xy-plane)
    
    def __init__(self):
        self.Ex = np.zeros_like(RestFrame.X)
        self.Ey = np.zeros_like(RestFrame.X)
        self.Ez = np.zeros_like(RestFrame.X)
        self.point_charges = []
    
    def plot_E_xyplane(self, show_charges=True):
        plt.figure(dpi=150)
        plt.streamplot(self.X[:,:,RestFrame.z0], self.Y[:,:,RestFrame.z0], self.Ex[:,:,RestFrame.z0], self.Ey[:,:,RestFrame.z0], density=2, linewidth=.5)

        if show_charges:
            for xq, yq, q in self.point_charges:
                if (np.abs(xq)<=RestFrame.coords1d[-1]) and (np.abs(yq)<=RestFrame.coords1d[-1]):
                    plt.scatter(xq, yq, marker=('_' if q<0 else '+'), c=('k' if q<0 else 'r'), zorder=4, s=100)
        
        plt.show()

    def add_point_charge(self, xq, yq, q):
        X1 = self.X - xq
        Y1 = self.Y - yq
        Phi1 = np.arctan2(Y1, X1)
        Theta1 = np.arctan( np.sqrt(X1**2 + Y1**2)/self.Z )
        E = q / (X1**2 + Y1**2 + self.Z**2)
        self.Ex += E * np.sin(Theta1) * np.cos(Phi1)
        self.Ey += E * np.sin(Theta1) * np.sin(Phi1)
        self.Ez += E * np.cos(Theta1)

        self.point_charges.append((xq, yq, q))
    
    def add_point_charges(self, x_coords, y_coords, charges):
        for xq, yq, q in zip(x_coords, y_coords, charges):
            self.add_point_charge(xq, yq, q)