import matplotlib
import matplotlib.pyplot as plt
import numpy as np

DEFAULT_COLOR_PALETTE = {
    'bg': "#1B1B1E",
    'labels': '#FFFFFF',
    'blue': '#8EB8E5',
    'red': '#F49097',
    'yellow': '#F4D35E',
    'green': '#9AE19D'
}

class MathPlotter():

    """docstring for MathPlotter"""
    def __init__(self, post, width, height, xlabel, ylabel, xlim=(0,1), ylim=None, default_linewidth=3.5, color_palette=DEFAULT_COLOR_PALETTE):
        """
        Args:
        * Post: string in the format "{POST}/{FILENAME}" to use it as the path to store this plot
        * Width, Height: dimensiones of the figure in inches
        * xlabel, ylabel: labels of the x and y axes
        * xlim, ylim: boundaries of the area to display
        * default_linewidth: self explanatory
        * color_palette: stores the colors to use. Must contain "bg" for the background and "labels" for the ticks, labels, axis, etc
        """
        # set font
        matplotlib.rcParams['font.family'] = 'sans-serif'
        matplotlib.rcParams['font.sans-serif'] = ['CMU Sans Serif']
        # set post directory
        self.filename = f"../../assets/img/{post}"
        # create figure with size in inches
        self.fig = plt.figure(figsize=[width, height])
        # add subplot
        self.ax = self.fig.add_subplot()
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.grid(True)
        # create x axis
        self.x = np.arange(xlim[0], xlim[1], 0.001)
        self.ax.set_xlim(xlim)
        if ylim:
            self.ax.set_ylim(ylim)
        # create color palette
        self.color_palette = DEFAULT_COLOR_PALETTE
        # Store line width
        self.default_linewidth = default_linewidth
        # init borders
        self.toggle_borders()

    def plot(self, y, *args, **kwargs):
        """
        - y is a function that receives the x axis and returns the values
        - args can be any argument supported by AxesSubplot.plot()
        """
        kwargs["linewidth"] = kwargs.get("linewidth", self.default_linewidth)
        self.ax.plot(self.x, y(self.x), *args, **kwargs)

    def text(self, x, y, text, *args, **kwargs):
        self.ax.text(x,y,text,*args,**kwargs)

    def toggle_borders(self, show_top=False, show_right=False, show_bottom=True, show_left=True):
        self.ax.spines['right'].set_visible(show_right)
        self.ax.spines['left'].set_visible(show_left)
        self.ax.spines['top'].set_visible(show_top)
        self.ax.spines['bottom'].set_visible(show_bottom)
        
    def generate(self, production=False):
        if production:
            # change color of borders to match background
            self.ax.spines['bottom'].set_color(self.color_palette['labels'])
            self.ax.spines['top'].set_color(self.color_palette['labels'])
            self.ax.spines['left'].set_color(self.color_palette['labels'])
            self.ax.spines['right'].set_color(self.color_palette['labels'])
            # change color of x axis to match background
            self.ax.tick_params(axis='x', colors=self.color_palette['labels'])
            self.ax.xaxis.label.set_color(self.color_palette['labels'])
            # change color of y axis to match background
            self.ax.tick_params(axis='y', colors=self.color_palette['labels'])
            self.ax.yaxis.label.set_color(self.color_palette['labels'])
            # save
            self.fig.savefig(f"{self.filename}.svg", transparent=True)
        else:
            plt.show(block=True)