# add parent folder to path
import sys
sys.path.append('../')
# import mathplotter
from MathPlotter import MathPlotter

plotter = MathPlotter("quantum-annealing/annealing", 6, 6, xlabel="Tiempo", ylabel="Energía", xlim=(0,1), ylim=(0,1))
# get color palette
color_palette = plotter.color_palette
# growing magnetic field
plotter.plot(lambda x: 2**(2.2*x-2) - .2, color=color_palette['blue'])
plotter.text(0.54, 0.8, 'Amplitud de los campos \nmagnéticos para\nnuestro sistema', color=color_palette['blue'], fontsize=14)
# decreasing magnetic field
plotter.plot(lambda x: 2**(-4*x) - .05, color=color_palette['yellow'])
plotter.text(0.25, 0.5, 'Amplitud de los campos \n magnéticos iniciales', color=color_palette['yellow'], fontsize=14)
# show
plotter.generate()
