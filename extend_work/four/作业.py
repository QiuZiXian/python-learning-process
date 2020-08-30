#PART 1
from __future__ import print_function
import numpy
import os
import netCDF4
import Ngl
dirc  = "/mnt/c/Users/Yingqi Fan"
f=os.path.join(dirc,"20130601_wind_temp_pres.cdf")
data = netCDF4.Dataset(f,"r",format="NETCDF3_CLASSIC")  # Open netCDF file.
T = data.variables["T"]
lat = data.variables["lat"][:,:]
lon = data.variables["lon"][:,:]
T0 = T[5,1,:,:]

wks_type = "png"
wks = Ngl.open_wks(wks_type,"figure")

resources = Ngl.Resources()
resources.sfXArray=lon
resources.sfYArray=lat

map = Ngl.contour_map(wks,T0,resources)
del T
del T0
del lat
del lon
Ngl.end()

#PART2
from __future__ import print_function
import numpy
import os
import netCDF4
import Ngl
dirc  = "/mnt/c/Users/Yingqi Fan"
f=os.path.join(dirc,"20130601_wind_temp_pres.cdf")  # Open netCDF file.
data = netCDF4.Dataset(f,"r",format="NETCDF3_CLASSIC")
T = data.variables["T"]
lat = data.variables["lat"][:,:]
lon = data.variables["lon"][:,:]
T0 = T[5,1,:,:]
wks_type = "png"
wks = Ngl.open_wks(wks_type,"figure")

resources = Ngl.Resources()
resources.sfXArray=lon
resources.sfYArray=lat
resources.mpGridAndLimbOn        = False
resources.mpCenterLatF           = 90.0
resources.mpCenterLonF           = 180.0
resources.mpCenterRotF           = 45.0
resources.mpFillOn               = True
resources.mpGridAndLimbDrawOrder = "Draw"
resources.mpGridLineDashPattern  = 5
resources.mpInlandWaterFillColor = "transparent"
resources.mpOceanFillColor       = "transparent"
resources.mpLandFillColor        = "tan"
resources.mpLabelsOn             = False
resources.mpLeftCornerLatF       = 10.
resources.mpLeftCornerLonF       = -180.
resources.mpLimitMode            = "corners"
resources.mpProjection           = "Stereographic"
resources.mpRightCornerLatF      = 10.
resources.mpRightCornerLonF      = 0.

map = Ngl.contour_map(wks,T0,resources)
del resources
del T
del T0
del lat
del lon
Ngl.end()

#PART3 background map
from __future__ import print_function
import numpy
import os
import netCDF4
import Ngl
dirc  = "/mnt/c/Users/Yingqi Fan"
f=os.path.join(dirc,"20130601_wind_temp_pres.cdf")  # Open netCDF file.
data = netCDF4.Dataset(f,"r",format="NETCDF3_CLASSIC")
T = data.variables["T"]
lat = data.variables["lat"][:,:]
lon = data.variables["lon"][:,:]
time= data.variables["time"]
T0 = T[5,1,:,:]
wks_type = "png"
wks = Ngl.open_wks(wks_type,"figure3")

resources = Ngl.Resources()
resources.sfXArray=lon
resources.sfYArray=lat
resources.mpGridAndLimbOn        = False
resources.mpCenterLatF           = 90.0
resources.mpCenterLonF           = 180.0
resources.mpCenterRotF           = 45.0
resources.mpFillOn               = True
resources.mpGridAndLimbDrawOrder = "Draw"
resources.mpGridLineDashPattern  = 5
resources.mpLabelsOn             = False
resources.mpLeftCornerLatF       = 10.
resources.mpLeftCornerLonF       = -180.
resources.mpLimitMode            = "corners"
resources.mpProjection           = "Stereographic"
resources.mpRightCornerLatF      = 10.
resources.mpRightCornerLonF      = 0.
resources.mpPerimOn         = False
resources.mpLandFillColor= "Tan1"
resources.mpOceanFillColor="SkyBlue"
resources.mpInlandWaterFillColor = "SkyBlue"



# Main Title
ncells = T.shape[1]

resources.tiMainString      = f'{T.long_name} [{T.units}] '
resources.tiMainFontHeightF = 0.02
resources.tiMainSide="top"

resources.cnExplicitLegendLabelsOn    = True     # Turn on the drawing
resources.cnConstFLabelString =  ["forecast reference time: T.time", "Validity time: time.units"]
res.pmLegendSide           = "Bottom"    # Change location of
cnConstFLabelPerimOn= True

map = Ngl.contour_map(wks,T0,resources)
del resources
del T
del T0
del lat
del lon
Ngl.end()

#part 4 contouring
from __future__ import print_function
import numpy
import os
import netCDF4
import Ngl
dirc  = "/mnt/c/Users/Yingqi Fan"
f=os.path.join(dirc,"20130601_wind_temp_pres.cdf")  # Open netCDF file.
data = netCDF4.Dataset(f,"r",format="NETCDF3_CLASSIC")
T = data.variables["T"]
lat = data.variables["lat"][:,:]
lon = data.variables["lon"][:,:]
time= data.variables["time"]
T0 = T[5,1,:,:]
wks_type = "png"
wks = Ngl.open_wks(wks_type,"figure4")

resources = Ngl.Resources()
resources.sfXArray=lon
resources.sfYArray=lat
resources.mpGridAndLimbOn        = False
resources.mpCenterLatF           = 90.0
resources.mpCenterLonF           = 180.0
resources.mpCenterRotF           = 45.0
resources.mpFillOn               = True
resources.mpGridAndLimbDrawOrder = "Draw"
resources.mpGridLineDashPattern  = 5
resources.mpLabelsOn             = False
resources.mpLeftCornerLatF       = 10.
resources.mpLeftCornerLonF       = -180.
resources.mpLimitMode            = "corners"
resources.mpProjection           = "Stereographic"
resources.mpRightCornerLatF      = 10.
resources.mpRightCornerLonF      = 0.
resources.mpPerimOn         = False
resources.mpLandFillColor= "Tan1"
resources.mpOceanFillColor="SkyBlue"
resources.mpInlandWaterFillColor = "SkyBlue"

# Contour options
resources.cnFillOn          = True         # turn on contour fill
resources.cnLinesOn         = True        # turn off contour lines
resources.cnLineLabelsOn    = True       # turn off line labels
resources.cnLevelSpacingF   = 2.5           # NCL chose 5.0
resources.cnFillPalette     = "WhiteBlueGreenYellowRed"
resources.cnLineColor= 6
resources.cnLineDashPattern= 2
resources.cnLineThicknesses= 1.2

ncells = T.shape[1]

resources.tiMainString      = f'{T.long_name} [{T.units}] '
resources.tiMainFontHeightF = 0.02
resources.tiMainSide="top"

resources.cnExplicitLegendLabelsOn    = True     # Turn on the drawing
resources.cnConstFLabelString =  ["forecast reference time: T.time", "Validity time: time.units"]
resources.pmLegendSide           = "Bottom"    # Change location of
cnConstFLabelPerimOn= True

map = Ngl.contour_map(wks,T0,resources)
del resources
del T
del T0
del lat
del lon
Ngl.end()

#part 5 sea level pressure
from __future__ import print_function
import numpy
import os
import netCDF4
import Ngl
dirc  = "/mnt/c/Users/Yingqi Fan"
f=os.path.join(dirc,"20130601_wind_temp_pres.cdf")  # Open netCDF file.
data = netCDF4.Dataset(f,"r",format="NETCDF3_CLASSIC")
seapr = data.variables["PN"]
lat = data.variables["lat"][:,:]
lon = data.variables["lon"][:,:]
time= data.variables["time"]
seapr0 = seapr[5,:,:]
wks_type = "png"
wks = Ngl.open_wks(wks_type,"figure5")

resources = Ngl.Resources()
resources.sfXArray=lon
resources.sfYArray=lat
resources.mpGridAndLimbOn        = False
resources.mpCenterLatF           = 90.0
resources.mpCenterLonF           = 180.0
resources.mpCenterRotF           = 45.0
resources.mpFillOn               = True
resources.mpGridAndLimbDrawOrder = "Draw"
resources.mpGridLineDashPattern  = 5
resources.mpLabelsOn             = False
resources.mpLeftCornerLatF       = 10.
resources.mpLeftCornerLonF       = -180.
resources.mpLimitMode            = "corners"
resources.mpProjection           = "Stereographic"
resources.mpRightCornerLatF      = 10.
resources.mpRightCornerLonF      = 0.
resources.mpPerimOn         = False
resources.mpLandFillColor= "Tan1"
resources.mpOceanFillColor="SkyBlue"
resources.mpInlandWaterFillColor = "SkyBlue"

# Contour options
resources.cnFillOn          = True         # turn on contour fill
resources.cnLinesOn         = True        # turn off contour lines
resources.cnLineLabelsOn    = True       # turn off line labels
resources.cnLevelSpacingF   = 2.5           # NCL chose 5.0
resources.cnFillPalette     = "WhiteBlueGreenYellowRed"
resources.cnLineColor= 6
resources.cnLineDashPattern= 2
resources.cnLineThicknesses= 1.2

ncells = seapr.shape[1]

resources.tiMainString      = f'{seapr.long_name} [{seapr.units}] '
resources.tiMainFontHeightF = 0.02
resources.tiMainSide="top"

resources.cnExplicitLegendLabelsOn    = True     # Turn on the drawing
resources.cnConstFLabelString =  ["forecast reference time: seapr.time", "Validity time: time.units"]
resources.pmLegendSide           = "Bottom"    # Change location of
cnConstFLabelPerimOn= True

map = Ngl.contour_map(wks,seapr0,resources)
del resources
del seapr
del seapr0
del lat
del lon
Ngl.end()

#part 6 wind speed vector

