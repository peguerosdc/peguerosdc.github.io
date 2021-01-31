# add parent folder to path
import sys
sys.path.append('../')
# import mathplotter
from MathPlotter import MathPlotter
# others
import numpy as np

plotter = MathPlotter("quantum-annealing/adiabatic", width=6, height=5, xlabel="Tiempo", ylabel="Energía", xlim=(0,50), ylim=(0,3))
# get color palette
color_palette = plotter.color_palette

def f1(b,o,s):
    return lambda x: s*np.sin( (np.pi/2)*np.cos( x/b - 1.58 ) ) + o

plotter.plot(f1(15.9,0,1), linewidth=4, color=color_palette['blue'])
plotter.plot(f1(18,2.1,-1), linewidth=4, color=color_palette['yellow'])
plotter.plot(f1(17,2.5,-1), linewidth=4, color=color_palette['red'])
plotter.plot(lambda x: (3 - np.sin(x/17)), linewidth=4, color=color_palette['green'])
plotter.generate()