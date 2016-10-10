# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.12-1 replay file
# Internal Version: 2012_03_13-20.21.46 119612
# Run by s1208454 on Mon Oct 10 17:43:12 2016
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
    name='/home/s1208454/FEMSS4/Labs/column/DLOAD/column1DL.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/s1208454/FEMSS4/Labs/column/DLOAD/column1DL.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=1)
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.animationOptions.setValues(frameRate=48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.81103, 
    farPlane=5.51849, width=0.337192, height=0.184352, viewOffsetX=-0.141133, 
    viewOffsetY=-0.572387)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.56424, 
    farPlane=5.76528, width=3.32276, height=1.87123, viewOffsetX=-0.258887, 
    viewOffsetY=-0.174447)
session.animationController.setValues(animationType=NONE)
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=AUTO)
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.animationOptions.setValues(mode=SWING)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.57432, 
    farPlane=5.7552, width=3.20155, height=1.80296, viewOffsetX=-0.195147, 
    viewOffsetY=-0.108423)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.68336, 
    farPlane=5.64617, width=2.69907, height=1.51999, viewOffsetX=-0.0605769, 
    viewOffsetY=-0.0660567)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.75892, 
    farPlane=5.5706, width=0.963767, height=0.54275, viewOffsetX=-0.0672888, 
    viewOffsetY=0.358001)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.75736, 
    farPlane=5.57216, width=0.963367, height=0.542524, viewOffsetX=-0.0542423, 
    viewOffsetY=0.0159487)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.73756, 
    farPlane=5.59196, width=1.22119, height=0.68772, viewOffsetX=-0.129693, 
    viewOffsetY=0.0313552)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.7356, 
    farPlane=5.59392, width=1.22055, height=0.68736, viewOffsetX=-0.109546, 
    viewOffsetY=-0.441221)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.74894, 
    farPlane=5.58058, width=1.04211, height=0.586869, viewOffsetX=-0.0953415, 
    viewOffsetY=-0.469056)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(COMPONENT, 'RF2'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=SYMBOLS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setSymbolVariable(
    variableLabel='RF', outputPosition=NODAL, vectorQuantity=RESULTANT, )
session.viewports['Viewport: 1'].odbDisplay.setSymbolVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, 
    tensorQuantity=ALL_PRINCIPAL_COMPONENTS, )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.84926, 
    farPlane=5.48027, width=0.774461, height=0.436141, viewOffsetX=-0.0718466, 
    viewOffsetY=-0.537085)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.81476, 
    farPlane=5.51476, width=1.22149, height=0.687888, viewOffsetX=-0.164558, 
    viewOffsetY=-0.531473)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxValue=-9.33967E+06, minValue=-1.0633E+07, showMinLocation=ON, 
    showMaxLocation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.3234, 
    farPlane=5.1468, width=1.89024, height=1.0645, viewOffsetX=-0.0478574, 
    viewOffsetY=-0.134651)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    showMinLocation=OFF, showMaxLocation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.25996, 
    farPlane=5.21024, width=2.72404, height=1.53405, viewOffsetX=-0.0329402, 
    viewOffsetY=0.056421)
session.Path(name='Mid-Height-cut', type=NODE_LIST, expression=(('PART-1-1', (
    '501:505:1', )), ))
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Mid-Height-cut']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    pathStyle=PATH_POINTS, numIntervals=10, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE_X)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Mid-Height-cut']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    pathStyle=PATH_POINTS, numIntervals=10, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE_X)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['_temp_2']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.xyDataObjects.changeKey(fromName='_temp_2', toName='Mid-Height-y-disp')
odb = session.odbs['/home/s1208454/FEMSS4/Labs/column/DLOAD/column1DL.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
xQuantity = visualization.QuantityType(type=PATH_X)
yQuantity = visualization.QuantityType(type=DISPLACEMENT)
session.xyDataObjects['Mid-Height-y-disp'].setValues(
    axis1QuantityType=xQuantity, axis2QuantityType=yQuantity, )
#* NameError: name 'PATH_X' is not defined
