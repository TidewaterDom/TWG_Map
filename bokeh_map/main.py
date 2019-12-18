#load external libraries
import numpy as np
import geopandas as gpd
import glob
from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, ColumnDataSource, curdoc
from bokeh.models import WMTSTileSource, HoverTool
from bokeh.tile_providers import get_provider, Vendors
from bokeh.models.markers import CircleCross
from bokeh.layouts import column
import pathlib 
import os 

dir_path= os.path.dirname(os.path.realpath(__file__))
path_data = pathlib.Path(os.path.join(dir_path, 'data'))
path_output = pathlib.Path(os.path.join(dirpath, 'output'))

if not path_output.exists():
	path_output.mkdir()


# Read in point data of glacier locations
sw_data = gpd.read_file(path_data/'Glacier_locations/Glacier_Locations_SW.shp')
nw_data = gpd.read_file(path_data/'Glacier_locations/Glacier_Locations_NW.shp')
n_data =  gpd.read_file(path_data/'Glacier_locations/Glacier_Locations_N.shp')
ne_data = gpd.read_file(path_data/'Glacier_locations/Glacier_Locations_NE.shp')
se_data = gpd.read_file(path_data/'Glacier_locations/Glacier_Locations_SE.shp')


# Read in image files for glacier data
path_sw = glob.glob(path_data/'TWG_images/SW/*.shp')
path_nw = glob.glob(path_data/'TWG_images/NW/*.shp')
path_n = glob.glob(path_data/'TWG_images/N/*.shp')
path_ne = glob.glob(path_data/'TWG_images/NE/*.shp')
path_se = glob.glob(path_data/'TWG_images/SE/*.shp')

# Change CRS to be conform with web mercator projection
sw_data = sw_data.to_crs({'init':'epsg:3857'})
nw_data = nw_data.to_crs({'init':'epsg:3857'})
n_data = n_data.to_crs({'init':'epsg:3857'})
ne_data = ne_data.to_crs({'init':'epsg:3857'})
se_data = se_data.to_crs({'init':'epsg:3857'})

# Get glacier names
sw_data = sw_data.sort_values('Name').reset_index(drop=True)
nw_data = nw_data.sort_values('Name').reset_index(drop=True)
ne_data = ne_data.sort_values('Name').reset_index(drop=True)
se_data = se_data.sort_values('Name').reset_index(drop=True)

# Extract x and y values of glacier location coordinates
sw_data['x'] = sw_data.geometry.x
sw_data['y'] = sw_data.geometry.y
nw_data['x'] = nw_data.geometry.x
nw_data['y'] = nw_data.geometry.y
n_data['x'] = n_data.geometry.x
n_data['y'] = n_data.geometry.y
ne_data['x'] = ne_data.geometry.x
ne_data['y'] = ne_data.geometry.y
se_data['x'] = se_data.geometry.x
se_data['y'] = se_data.geometry.y

# Create lists of glacier locations/names to plot
xList_sw = sw_data.x.values
yList_sw = sw_data.y.values
nameList_sw = sw_data.Name.values

xList_nw = nw_data.x.values
yList_nw = nw_data.y.values
nameList_nw = nw_data.Name.values

xList_n = n_data.x.values
yList_n = n_data.y.values
nameList_n = n_data.Name.values

xList_ne = ne_data.x.values
yList_ne = ne_data.y.values
nameList_ne = ne_data.Name.values

xList_se = se_data.x.values
yList_se = se_data.y.values
nameList_se = se_data.Name.values

# Create lists of images to plot
img_list_sw = []
for i in path_sw:
    img_list_sw.append(os.path.abspath(i))
img_list_nw = []
for i in path_nw:
    img_list_nw.append(os.path.abspath(i))
img_list_n = []
for i in path_n:
    img_list_n.append(os.path.abspath(i))
img_list_ne = []
for i in path_ne:
    img_list_ne.append(os.path.abspath(i))
img_list_se = []
for i in path_se:
    img_list_se.append(os.path.abspath(i))
	
# Set up interactive plot
output_file(".html")
tile_providers= get_provider(Vendors.STAMEN_TERRAIN)

source_sw = ColumnDataSource(data=dict(
    x=xList_sw,
    y=yList_sw,
    desc = nameList_sw,
    imgs=img_list_sw,
))

source_nw = ColumnDataSource(data=dict(
    x=xList_nw,
    y=yList_nw,
    desc = nameList_nw,
    imgs=img_list_nw,
))

source_n = ColumnDataSource(data=dict(
    x=xList_n,
    y=yList_n,
    desc = nameList_n,
    imgs=img_list_n,
))

source_ne = ColumnDataSource(data=dict(
    x=xList_ne,
    y=yList_ne,
    desc = nameList_ne,
    imgs=img_list_ne,
))

source_se = ColumnDataSource(data=dict(
    x=xList_se,
    y=yList_se,
    desc = nameList_se,
    imgs=img_list_se,
))

TOOLTIPS = """
    <div>
        <div>
            <img
                src="@imgs" height="650" alt="@imgs" width="650"
                style="float: left; margin: 0px 15px 15px 0px;"
                border="2"
            ></img>
        </div>
        <div>
            <span style="font-size: 17px; font-weight: bold;">@desc</span>
            <span style="font-size: 15px; color: #966;">[$index]</span>
        </div>

    </div>
"""
                 
plot = figure(x_range=(-2500000, -1000000), y_range=(7500000, 15000000),plot_width=1900, plot_height=900,\
           x_axis_type="mercator", y_axis_type="mercator",tools='pan,box_zoom, reset,\
           wheel_zoom,hover',tooltips= TOOLTIPS)
# plot.add_tile(tile_providers)

# sw = CircleCross(x='x',y='y', size=10, line_color="#355C7D", fill_color=None, line_width=2)
# plot.add_glyph(source_sw,sw)

# nw = CircleCross(x='x',y= 'y', size=10, line_color="#008080", fill_color=None, line_width=2)
# plot.add_glyph(source_nw,nw)

# n= CircleCross(x='x',y='y', size=10, line_color="#F8B195",fill_color=None, line_width=2)
# plot.add_glyph(source_n, n)

# ne = CircleCross(x='x',y='y' ,size=10, line_color="#C06C84", fill_color=None, line_width=2)
# plot.add_glyph(source_ne, ne)

# se = CircleCross(x='x',y='y', size=10, line_color="#F67280",fill_color=None, line_width=2)
# plot.add_glyph(source_se,se)

curdoc().add_root(row(plot))
curdoc().title = 'Interactive Map of Tidewater Glaciers in Greenland'
