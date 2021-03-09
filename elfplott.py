import numpy as np
import matplotlib.pyplot as plt
# np.seterr(divide='ignore')

class RestFrame:
    coords1d = np.linspace(-5,5,20)                         # x and y coordinates
    coords1d_z = np.linspace(-5,5,21)                       # z coordinates
    X, Y, Z = np.meshgrid(coords1d, coords1d, coords1d_z)
    z0 = list(coords1d_z).index(0.)                         # index of z-dimension corresponding to z=0 (i.e. xy-plane)
    
    def __init__(self):
        self.Ex = np.zeros_like(RestFrame.X)
        self.Ey = np.zeros_like(RestFrame.X)
        self.Ez = np.zeros_like(RestFrame.X)

        self.Bx = 0
        self.By = 0
        self.Bz = 0

        self.Ex_prime = np.zeros_like(RestFrame.X)
        self.Ey_prime = np.zeros_like(RestFrame.X)
        self.Ez_prime = np.zeros_like(RestFrame.X)

        self.Bx_prime = np.zeros_like(RestFrame.X)
        self.By_prime = np.zeros_like(RestFrame.X)
        self.Bz_prime = np.zeros_like(RestFrame.X)

        self.point_charges = []

        self.beta = 0

    def plot_E_xyplane(self, plot_prime=False, show_charges=True):
        plt.figure(dpi=150)
        plt.streamplot(RestFrame.coords1d, RestFrame.coords1d, self.Ex[:,:,RestFrame.z0], self.Ey[:,:,RestFrame.z0], density=2, linewidth=.5)
        
        if plot_prime:
            plt.streamplot(RestFrame.coords1d, RestFrame.coords1d, self.Ex_prime[:,:,RestFrame.z0], self.Ey_prime[:,:,RestFrame.z0], density=2, linewidth=.5)

        if show_charges:
            for xq, yq, q in self.point_charges:
                if (np.abs(xq)<=RestFrame.coords1d[-1]) and (np.abs(yq)<=RestFrame.coords1d[-1]):
                    plt.scatter(xq, yq, marker=('_' if q<0 else '+'), c=('k' if q<0 else 'r'), zorder=4, s=100)
        
        plt.xlabel("$x$")
        plt.ylabel("$y$")
        plt.title(r"$\vec{E}$ projection on $xy$-plane")
        
        plt.gca().set_aspect('equal', 'box')
        plt.show()

    def plot_B(self, x):
        x_idx = np.argmin(np.abs(RestFrame.coords1d-x))
        
        plt.figure(dpi=150)

        plt.streamplot(RestFrame.coords1d_z, RestFrame.coords1d, self.Bz_prime[:,x_idx,:], self.By_prime[:,x_idx,:], density=2, linewidth=.5)

        plt.xlabel("$z$")
        plt.ylabel("$y$")
        plt.title(r"$\vec{B'}$ projection on $yz$-plane, " + f"$x={RestFrame.coords1d[x_idx]}$")
        
        plt.gca().set_aspect('equal', 'box')
        plt.show()

    def add_point_charge(self, xq, yq, q):
        X1 = RestFrame.X - xq
        Y1 = RestFrame.Y - yq
        Phi1 = np.arctan2(Y1, X1)
        Theta1 = np.arctan2( np.sqrt(X1**2 + Y1**2), RestFrame.Z )
        E = q / (X1**2 + Y1**2 + RestFrame.Z**2)
        self.Ex += E * np.sin(Theta1) * np.cos(Phi1)
        self.Ey += E * np.sin(Theta1) * np.sin(Phi1)
        self.Ez += E * np.cos(Theta1)

        self.point_charges.append((xq, yq, q))
        self.boost()
    
    def add_point_charges(self, x_coords, y_coords, charges):
        for xq, yq, q in zip(x_coords, y_coords, charges):
            self.add_point_charge(xq, yq, q)
    
    def gamma(self):
        return 1 / np.sqrt(1-self.beta**2)

    def boost(self, beta=None):
        if beta is not None:
            self.beta = beta
        
        self.Ex_prime = self.Ex
        self.Ey_prime = self.gamma() * (self.Ey - self.beta * self.Bz)
        self.Ez_prime = self.gamma() * (self.Ez + self.beta * self.By)

        self.Bx_prime = self.Bx
        self.By_prime = self.gamma() * (self.By + self.beta * self.Ez)
        self.Bz_prime = self.gamma() * (self.Bz - self.beta * self.Ey)