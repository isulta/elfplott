# elfplott: Electric Field Plotting and Lorentz Transformation Tool
The **El**ectric **F**ield **P**lotting and **Lo**rentz **T**ransformation **T**ool (`elfplott`) is a physics visualization software that plots the electric field of a given static charge distribution, and plots the electromagnetic fields in an inertial reference frame that is moving relative to the charge distribution.

`elfplott` was created as part of the Physics 414-1 Winter 2021 numerical project.

## Usage

The included Jupyter notebook `Tutorial.ipynb` demonstrates the main [features](#Features) of `elfplott`.

To run `elfplott`, Python 3 and the [dependencies](#Dependencies) listed below are required.

## Features
- Create a rest frame charge distribution composed of point charges
- Import a charge distribution from an image
- Plot the electric field in the rest frame on the xy-plane
- Perform a Lorentz boost to an inertial frame moving along the x-axis relative to the rest frame of the charge distribution
- Plot the Lorentz transformed electric and magnetic fields in the inertial frame

## Dependencies

- Matplotlib

- NumPy

- [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)

## References
- [Plotting Vector Fields in Python](https://krajit.github.io/sympy/vectorFields/vectorFields.html)
- [Electric field](https://en.wikipedia.org/wiki/Electric_field)
- [Importing Image Data into NumPy Arrays](https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays)