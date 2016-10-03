# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.13-1 replay file
# Internal Version: 2013_05_16-03.28.56 126354
# Run by Ali on Mon Oct 03 22:24:21 2016
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=98.7174224853516, 
    height=99.7669296264648)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o1 = session.openOdb(
    name='C:/Users/Ali/Documents/MEGA/University/5th Year/FEM 4/Labs/column/column1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/Ali/Documents/MEGA/University/5th Year/FEM 4/Labs/column/column1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.08647, 
    farPlane=6.24305, width=4.96389, height=2.00764, viewOffsetX=0.00717767, 
    viewOffsetY=-0.0103459)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=SYMBOLS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.68908, 
    farPlane=5.64044, width=1.73433, height=0.701447, viewOffsetX=0.0724458, 
    viewOffsetY=0.302187)
session.viewports['Viewport: 1'].odbDisplay.setSymbolVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), tensorQuantity=DIRECT_COMPONENT, )
session.viewports['Viewport: 1'].odbDisplay.setSymbolVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), tensorQuantity=DIRECT_COMPONENT, )
session.viewports['Viewport: 1'].odbDisplay.setSymbolVariable(
    variableLabel='RF', outputPosition=NODAL, vectorQuantity=RESULTANT, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.70526, 
    farPlane=5.62426, width=1.15672, height=0.467835, viewOffsetX=0.0672814, 
    viewOffsetY=-0.557804)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.33816, 
    farPlane=5.99136, width=3.30845, height=1.3381, viewOffsetX=0.266066, 
    viewOffsetY=-0.107068)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
