# add parent folder to path
import sys
sys.path.append('../')
# import mathplotter
from MathPlotter import MathPlotter
import numpy as np

plotter = MathPlotter("POST/FILENAME", width=6, height=6, xlabel="", ylabel="", xlim=(0,1))
# get color palette
color_palette = plotter.color_palette

"""
----------------------------------------------------
START PLOTTING
----------------------------------------------------
"""
plotter.plot(lambda x : , linewidth=4, color=color_palette['blue'])