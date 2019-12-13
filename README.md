# **Interactive Map of Tidewater Glacier Change in Greenland for the past 34 years**

The interactive map shows annual tidewater glacier margin change for the past 34 years, which were mapped using Google Earth Engine Digitsation Tool (GEEDiT) and were processed using the Margin Change Quantification Tool (MaQiT; Lea, 2018)
The following data is avialable for each glacier:

 - Absolute terminus change 
 - Terminus position relative to most recent observation.
 - Annual mean sea surface temperature anomalies to 1961-1990 average (Data taken from the HadISST v1 data set).
 - Annual mean air temperature anomalies to 1961-1990 average (Data taken from Danish Meteorological Institute weather stations).
 - Annual mean runoff anomalies to 1961-1990 average (Data taken from MAR v3.9 re-analysis data set; Fettweis et al., 2013).
 - Annual ice flux deviation from the mean (Data taken from Mankoff et al., 2019 data set).
 - Decadal shallow and deep water ocean temperature anomalies to 1981-2010 average (Data taken from the World Ocean Atlas 2018). 
 
Map one shows the mapped margins on top of a bedmachine v3 DEM (Morlighem et al., 2017); map two shows the locations of SST and deep water temperature data points used to calculate the annual means on top of a bedmachine v3 DEM. The points were determined using a nearest-neighbour analysis, and in case of the deep water temperatures, cropped to a 50 kilometre buffer to exclude data from the shelf. 

To see the map click here:



The code to produce this map is based on bokeh and binder and can be found in the repository. 
