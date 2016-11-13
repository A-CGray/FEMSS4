# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.12-1 replay file
# Internal Version: 2012_03_13-20.21.46 119612
# Run by s1208454 on Fri Nov 11 14:26:52 2016
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=279.311737060547, 
    height=158.678115844727)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
step = mdb.openStep(
    '/home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Wheel Centre Blank.step', 
    scaleFromFile=OFF)
mdb.models['Model-1'].PartFromGeometryFile(name='Wheel Centre Blank', 
    geometryFile=step, combine=False, dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Wheel Centre Blank']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((70000.0, 0.33), 
    ))
mdb.models['Model-1'].materials.changeKey(fromName='Material-1', 
    toName='aluminium')
mdb.models['Model-1'].HomogeneousSolidSection(name='aluminium', 
    material='aluminium', thickness=None)
p = mdb.models['Model-1'].parts['Wheel Centre Blank']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Wheel Centre Blank']
p.SectionAssignment(region=region, sectionName='aluminium', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
del session.viewports['Viewport: 1']
#* CanvasError: SystemError: the current viewport may not be deleted.
