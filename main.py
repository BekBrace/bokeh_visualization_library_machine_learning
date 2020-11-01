# Apple, Microsoft, Facebook and Google Stock data Visualization using Bokeh Library
import bokeh
from bokeh.sampledata.stocks import AAPL, FB, GOOG, MSFT
from bokeh.plotting import figure, output_file, show
import numpy as np

output_file('stocks.html')

graph = figure(x_axis_type="datetime", title="Stock closing Price")

graph.xaxis.axis_label = "Date"
graph.yaxis.axis_label = "Price (in USD)"

# Plotting the line graph for Apple
x_axis_coordinates = np.array(AAPL['date'], dtype=np.datetime64)
y_axis_coordinates = AAPL['adj_close']
color = "black"
legend_label = "AAPL"
graph.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

# Plotting the line graph for Facebook
x_axis_coordinates = np.array(FB['date'], dtype=np.datetime64)
y_axis_coordinates = FB['adj_close']
color = "blue"
legend_label = "FB"
graph.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

# Plotting the line graph for Google
x_axis_coordinates = np.array(GOOG['date'], dtype=np.datetime64)
y_axis_coordinates = GOOG['adj_close']
color = "orange"
legend_label = "GOOG"
graph.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

# Plotting the line graph for Microsoft
x_axis_coordinates = np.array(MSFT['date'], dtype=np.datetime64)
y_axis_coordinates = MSFT['adj_close']
color = "yellow"
legend_label = "MSFT"
graph.line(x_axis_coordinates, y_axis_coordinates,
           color=color, legend_label=legend_label)

# Relocate the legened table the top left
graph.legend.location = "top_left"

# displaying the model
show(graph)
