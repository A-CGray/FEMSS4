# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.12-1 replay file
# Internal Version: 2012_03_13-20.21.46 119612
# Run by s1208454 on Mon Oct  3 17:33:41 2016
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=242.093734741211, 
    height=123.630004882812)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
o1 = session.openOdb(
    name='/home/s1208454/FEMSS4/Labs/cantilever/cantilever1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/s1208454/FEMSS4/Labs/cantilever/cantilever1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          3
#: Number of Steps:              1
odb = session.odbs['/home/s1208454/FEMSS4/Labs/cantilever/cantilever1.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('S', 
    INTEGRATION_POINT, ((COMPONENT, 'S11'), )), ), nodePick=(('PART-1-1', 5, (
    '[#421084 ]', )), ), )
odb = session.odbs['/home/s1208454/FEMSS4/Labs/cantilever/cantilever1.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'S', INTEGRATION_POINT, ((COMPONENT, 'S11'), )), ), nodePick=(('PART-1-1', 
    5, ('[#421084 ]', )), ), )
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
del session.xyDataObjects['S:S11 (Avg: 75%) PI: PART-1-1 N: 9']
del session.xyDataObjects['S:S11 (Avg: 75%) PI: PART-1-1 N: 109']
del session.xyDataObjects['S:S11 (Avg: 75%) PI: PART-1-1 N: 209']
del session.xyDataObjects['S:S11 (Avg: 75%) PI: PART-1-1 N: 309']
del session.xyDataObjects['S:S11 (Avg: 75%) PI: PART-1-1 N: 409']
del session.xyDataObjects['_S:S11 (Avg: 75%) PI: PART-1-1 N: 9']
del session.xyDataObjects['_S:S11 (Avg: 75%) PI: PART-1-1 N: 109']
del session.xyDataObjects['_S:S11 (Avg: 75%) PI: PART-1-1 N: 209']
del session.xyDataObjects['_S:S11 (Avg: 75%) PI: PART-1-1 N: 309']
del session.xyDataObjects['_S:S11 (Avg: 75%) PI: PART-1-1 N: 409']
odb = session.odbs['/home/s1208454/FEMSS4/Labs/cantilever/cantilever1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.Path(name='Mid-Beam-Section', type=NODE_LIST, expression=(('PART-1-1', 
    ('9:409:100', )), ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'))
pth = session.paths['Mid-Beam-Section']
session.XYDataFromPath(name='Mid-Section-Stress', path=pth, 
    includeIntersections=False, pathStyle=PATH_POINTS, numIntervals=10, 
    shape=UNDEFORMED, labelType=TRUE_DISTANCE_Y)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Mid-Beam-Section']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    pathStyle=PATH_POINTS, numIntervals=10, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE_Y)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xQuantity = visualization.QuantityType(type=STRESS)
yQuantity = visualization.QuantityType(type=PATH_Y)
session.xyDataObjects['Mid-Section-Stress'].setValues(
    axis1QuantityType=xQuantity, axis2QuantityType=yQuantity, )
#* NameError: name 'PATH_Y' is not defined
del session.xyDataObjects['_temp_1']
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'))
pth = session.paths['Mid-Beam-Section']
session.XYDataFromPath(name='Mid-Section-S12', path=pth, 
    includeIntersections=False, pathStyle=PATH_POINTS, numIntervals=10, 
    shape=UNDEFORMED, labelType=TRUE_DISTANCE_Y)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Mid-Beam-Section']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    pathStyle=PATH_POINTS, numIntervals=10, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE_Y)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['Mid-Section-S12']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['Mid-Section-S12']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
odb = session.odbs['/home/s1208454/FEMSS4/Labs/cantilever/cantilever1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
del session.xyDataObjects['Mid-Section-S12']
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['Mid-Section-Stress']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.xyDataObjects.changeKey(fromName='Mid-Section-Stress', 
    toName='Mid-Section-S11')
pth = session.paths['Mid-Beam-Section']
session.XYDataFromPath(name='Mid-Section-S12', path=pth, 
    includeIntersections=False, pathStyle=PATH_POINTS, numIntervals=10, 
    shape=UNDEFORMED, labelType=TRUE_DISTANCE_Y)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Mid-Beam-Section']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    pathStyle=PATH_POINTS, numIntervals=10, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE_Y)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
del session.xyDataObjects['_temp_1']
del session.xyDataObjects['Mid-Section-S12']
pth = session.paths['Mid-Beam-Section']
session.XYDataFromPath(name='Mid-Section-S12', path=pth, 
    includeIntersections=False, pathStyle=PATH_POINTS, numIntervals=10, 
    shape=UNDEFORMED, labelType=TRUE_DISTANCE)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Mid-Beam-Section']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    pathStyle=PATH_POINTS, numIntervals=10, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
odb = session.odbs['/home/s1208454/FEMSS4/Labs/cantilever/cantilever1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.Path(name='Mid-Beam-Section', type=NODE_LIST, expression=(('PART-1-1', 
    ('9:409:100', )), ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['Mid-Section-S11']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['Mid-Section-S12']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
odb = session.odbs['/home/s1208454/FEMSS4/Labs/cantilever/cantilever1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Min. Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=SYMBOLS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setSymbolVariable(
    variableLabel='RF', outputPosition=NODAL, vectorQuantity=RESULTANT, )
session.viewports['Viewport: 1'].odbDisplay.setSymbolVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, 
    tensorQuantity=ALL_PRINCIPAL_COMPONENTS, )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourType=LINE, maxValue=7876.86, minValue=-7876.86)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourType=QUILT)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourType=BANDED)
