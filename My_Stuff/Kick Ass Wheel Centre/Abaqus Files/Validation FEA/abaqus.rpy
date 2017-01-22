# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_16-03.28.56 126354
# Run by Ali on Sun Jan 22 13:41:34 2017
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=92.1698379516602, 
    height=121.12760925293)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Rear Wheel Assembly .cae')
#: The model database "C:\Users\Ali\Documents\MEGA\University\5th_Year\FEM 4\My_Stuff\Kick Ass Wheel Centre\Abaqus Files\Validation FEA\Rear Wheel Assembly .cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['bolt1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['Model-1'].steps.changeKey(fromName='Step-1', toName='Preload')
mdb.models['Model-1'].StaticStep(name='Wheel-load', previous='Preload')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Wheel-load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].ContactProperty('Gen-contact')
mdb.models['Model-1'].interactionProperties['Gen-contact'].TangentialBehavior(
    formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
    pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((
    0.1, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
    fraction=0.005, elasticSlipStiffness=None)
#: The interaction property "Gen-contact" has been created.
mdb.models['Model-1'].ContactStd(name='Int-1', createStepName='Initial')
mdb.models['Model-1'].interactions['Int-1'].includedPairs.setValuesInStep(
    stepName='Initial', useAllstar=ON)
mdb.models['Model-1'].interactions['Int-1'].contactPropertyAssignments.appendInStep(
    stepName='Initial', assignments=((GLOBAL, SELF, 'Gen-contact'), ))
#: The interaction "Int-1" has been created.
session.viewports['Viewport: 1'].view.setValues(nearPlane=675.38, 
    farPlane=1127.12, width=96.3784, height=47.5554, viewOffsetX=-31.4536, 
    viewOffsetY=22.2513)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
a.Surface(side1Faces=side1Faces1, name='CP-4-bolt1-1')
region1=a.surfaces['CP-4-bolt1-1']
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['nut1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#200 ]', ), )
a.Surface(side1Faces=side1Faces1, name='CP-4-nut1-1')
region2=a.surfaces['CP-4-nut1-1']
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
a.Surface(side1Faces=side1Faces1, name='CP-8-bolt2-1')
region3=a.surfaces['CP-8-bolt2-1']
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['nut2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#200 ]', ), )
a.Surface(side1Faces=side1Faces1, name='CP-8-nut2-1')
region4=a.surfaces['CP-8-nut2-1']
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt3-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
a.Surface(side1Faces=side1Faces1, name='CP-12-bolt3-1')
region5=a.surfaces['CP-12-bolt3-1']
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['nut3-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#200 ]', ), )
a.Surface(side1Faces=side1Faces1, name='CP-12-nut3-1')
region6=a.surfaces['CP-12-nut3-1']
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt4-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
a.Surface(side1Faces=side1Faces1, name='CP-16-bolt4-1')
region7=a.surfaces['CP-16-bolt4-1']
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['nut4-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#200 ]', ), )
a.Surface(side1Faces=side1Faces1, name='CP-16-nut4-1')
region8=a.surfaces['CP-16-nut4-1']
mdb.models['Model-1'].Tie(name='CP-4-bolt1-1-nut1-1', master=region1, 
    slave=region2, positionToleranceMethod=COMPUTED, adjust=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE)
mdb.models['Model-1'].Tie(name='CP-8-bolt2-1-nut2-1', master=region3, 
    slave=region4, positionToleranceMethod=COMPUTED, adjust=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE)
mdb.models['Model-1'].Tie(name='CP-12-bolt3-1-nut3-1', master=region5, 
    slave=region6, positionToleranceMethod=COMPUTED, adjust=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE)
mdb.models['Model-1'].Tie(name='CP-16-bolt4-1-nut4-1', master=region7, 
    slave=region8, positionToleranceMethod=COMPUTED, adjust=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=657.036, 
    farPlane=1145.46, width=276.946, height=136.652, viewOffsetX=-15.5037, 
    viewOffsetY=22.7009)
session.viewports['Viewport: 1'].view.setValues(nearPlane=652.444, 
    farPlane=1146.64, width=275.01, height=135.697, cameraPosition=(661.206, 
    607.171, -108.464), cameraUpVector=(-0.866211, 0.413839, -0.28003), 
    cameraTarget=(4.40019, -7.94496, -58.6212), viewOffsetX=-15.3953, 
    viewOffsetY=22.5423)
session.viewports['Viewport: 1'].view.setValues(nearPlane=660.645, 
    farPlane=1145.13, width=278.467, height=137.403, cameraPosition=(392.407, 
    541.357, -656.576), cameraUpVector=(-0.830919, 0.432362, 0.350194), 
    cameraTarget=(-8.13336, -10.7182, -67.4866), viewOffsetX=-15.5888, 
    viewOffsetY=22.8256)
session.viewports['Viewport: 1'].view.setValues(nearPlane=644.28, 
    farPlane=1156.95, width=271.57, height=133.999, cameraPosition=(549.265, 
    569.512, -480.08), cameraUpVector=(-0.872359, 0.450738, 0.189273), 
    cameraTarget=(-4.53921, -9.25371, -67.0702), viewOffsetX=-15.2026, 
    viewOffsetY=22.2602)
session.viewports['Viewport: 1'].view.setValues(nearPlane=646.531, 
    farPlane=1158.49, width=272.519, height=134.467, cameraPosition=(571.708, 
    585.222, 331.901), cameraUpVector=(-0.793701, 0.488709, -0.362218), 
    cameraTarget=(10.2536, -1.54985, -58.8859), viewOffsetX=-15.2557, 
    viewOffsetY=22.338)
session.viewports['Viewport: 1'].view.setValues(nearPlane=649.809, 
    farPlane=1159.44, width=273.901, height=135.149, cameraPosition=(517.897, 
    629.697, 342.775), cameraUpVector=(-0.804291, 0.429821, -0.41033), 
    cameraTarget=(11.8718, 0.11183, -56.9848), viewOffsetX=-15.333, 
    viewOffsetY=22.4512)
session.viewports['Viewport: 1'].view.setValues(nearPlane=685.896, 
    farPlane=1123.36, width=34.2523, height=16.9009, viewOffsetX=-36.2744, 
    viewOffsetY=22.3038)
mdb.models['Model-1'].constraints['CP-4-bolt1-1-nut1-1'].setValues(
    positionToleranceMethod=SPECIFIED, positionTolerance=1.0)
mdb.models['Model-1'].constraints['CP-4-bolt1-1-nut1-1'].setValues(
    positionToleranceMethod=COMPUTED)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    interactions=OFF, constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.39218e+006, 
    farPlane=4.01911e+006, width=7.88476e+006, height=3.90627e+006, 
    cameraPosition=(1.51915e+006, 1.89008e+006, 1.20006e+006), 
    viewOffsetX=753370, viewOffsetY=-131254)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=652.809, 
    farPlane=1149.69, width=221.855, height=109.911, viewOffsetX=-8.90595, 
    viewOffsetY=6.82046)
p = mdb.models['Model-1'].parts['bolt1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt1']
p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=40.0)
p = mdb.models['Model-1'].parts['bolt1']
del p.features['Datum plane-1']
session.viewports['Viewport: 1'].view.setValues(nearPlane=176.193, 
    farPlane=304.104, width=100.865, height=49.7693, cameraPosition=(143.225, 
    107.276, 155.539), cameraUpVector=(-0.53704, 0.804097, -0.254984), 
    cameraTarget=(-1.60878, 51.9454, -25.4182))
session.viewports['Viewport: 1'].view.setValues(nearPlane=185.936, 
    farPlane=290.822, width=106.442, height=52.5213, cameraPosition=(181.319, 
    144.137, 96.5269), cameraUpVector=(-0.692449, 0.706492, -0.146231), 
    cameraTarget=(-1.31464, 52.23, -25.8739))
session.viewports['Viewport: 1'].view.setValues(nearPlane=180.225, 
    farPlane=297.256, width=103.173, height=50.9082, cameraPosition=(141.086, 
    172.241, 122.802), cameraUpVector=(-0.798565, 0.559801, -0.221172), 
    cameraTarget=(-1.32906, 52.2401, -25.8645))
p = mdb.models['Model-1'].parts['bolt1']
v = p.vertices
p.DatumPlaneByTwoPoint(point1=v[1], point2=v[0])
p = mdb.models['Model-1'].parts['bolt1']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#3 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['bolt1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
d = p.datums
p.PartitionCellByDatumPlane(datumPlane=d[10], cells=pickedCells)
p = mdb.models['Model-1'].parts['bolt2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt2']
v1 = p.vertices
p.DatumPlaneByTwoPoint(point1=v1[1], point2=v1[0])
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.221, 
    farPlane=275.463, width=112.331, height=55.4267, cameraPosition=(171.319, 
    198.512, 21.9937), cameraUpVector=(-0.83793, 0.21424, -0.50197), 
    cameraTarget=(53.3912, -3.05457, -25.4183))
p = mdb.models['Model-1'].parts['bolt2']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
d1 = p.datums
p.PartitionCellByDatumPlane(datumPlane=d1[4], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=182.319, 
    farPlane=293.02, width=104.372, height=51.4998, cameraPosition=(211.411, 
    127.793, 95.28), cameraUpVector=(-0.669201, 0.605932, -0.430135), 
    cameraTarget=(52.9743, -2.31928, -26.1803))
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
p = mdb.models['Model-1'].parts['bolt3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt3']
e = p.edges
p.DatumPlaneByTwoPoint(point1=p.InterestingPoint(edge=e[1], rule=MIDDLE), 
    point2=p.InterestingPoint(edge=e[0], rule=MIDDLE))
p = mdb.models['Model-1'].parts['bolt3']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
d = p.datums
p.PartitionCellByDatumPlane(datumPlane=d[4], cells=pickedCells)
p = mdb.models['Model-1'].parts['bolt4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt4']
e1 = p.edges
p.DatumPlaneByTwoPoint(point1=p.InterestingPoint(edge=e1[1], rule=MIDDLE), 
    point2=p.InterestingPoint(edge=e1[0], rule=MIDDLE))
p = mdb.models['Model-1'].parts['bolt4']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#3 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['bolt4']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
d1 = p.datums
p.PartitionCellByDatumPlane(datumPlane=d1[6], cells=pickedCells)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['bolt4']
p.generateMesh()
p = mdb.models['Model-1'].parts['bolt3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt3']
p.seedPart(size=2.4, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['bolt3']
p.generateMesh()
p = mdb.models['Model-1'].parts['bolt3']
p.deleteMesh()
p = mdb.models['Model-1'].parts['bolt3']
p.seedPart(size=2.0, deviationFactor=0.022, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['bolt3']
p.generateMesh()
p = mdb.models['Model-1'].parts['bolt4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt4']
p.deleteMesh()
p = mdb.models['Model-1'].parts['bolt4']
p.seedPart(size=2.4, deviationFactor=0.022, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['bolt4']
p.generateMesh()
p = mdb.models['Model-1'].parts['bolt3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt4']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#7 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['bolt4']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1f ]', ), )
p.deleteSeeds(regions=pickedEdges)
p = mdb.models['Model-1'].parts['bolt4']
p.seedPart(size=2.0, deviationFactor=0.022, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['bolt4']
p.generateMesh()
p = mdb.models['Model-1'].parts['bolt3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt2']
p.seedPart(size=2.0, deviationFactor=0.022, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['bolt2']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=156.898, 
    farPlane=279.306, cameraPosition=(209.777, -8.45483, 123.35), 
    cameraUpVector=(-0.043254, 0.994205, 0.0984187), cameraTarget=(55, 0, 
    -30.0816))
session.viewports['Viewport: 1'].view.setValues(nearPlane=154.656, 
    farPlane=281.549, cameraPosition=(191.476, 70.0929, 124.935), 
    cameraUpVector=(-0.41653, 0.908062, -0.043883))
p = mdb.models['Model-1'].parts['bolt1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt1']
p.seedPart(size=2.0, deviationFactor=0.022, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['bolt1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1f ]', ), )
p.deleteSeeds(regions=pickedEdges)
p = mdb.models['Model-1'].parts['bolt1']
p.generateMesh()
p = mdb.models['Model-1'].parts['brake']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['hub']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=311.093, 
    farPlane=550.118, width=124.579, height=61.7187, viewOffsetX=13.166, 
    viewOffsetY=-6.15958)
session.viewports['Viewport: 1'].view.setValues(nearPlane=327.095, 
    farPlane=561.799, width=130.986, height=64.8933, cameraPosition=(383.814, 
    220.3, -125.95), cameraUpVector=(-0.753236, 0.555669, -0.351948), 
    cameraTarget=(13.7377, 4.48788, -82.4785), viewOffsetX=13.8432, 
    viewOffsetY=-6.47641)
session.viewports['Viewport: 1'].view.setValues(nearPlane=357.113, 
    farPlane=551.577, width=143.007, height=70.8487, cameraPosition=(283.489, 
    83.0154, -429.873), cameraUpVector=(-0.828034, 0.552141, -0.0974671), 
    cameraTarget=(19.3872, 5.35987, -98.7519), viewOffsetX=15.1136, 
    viewOffsetY=-7.07077)
session.viewports['Viewport: 1'].view.setValues(nearPlane=331.321, 
    farPlane=567.248, width=132.679, height=65.7317, cameraPosition=(332.087, 
    194.393, -316.669), cameraUpVector=(-0.852774, 0.505334, -0.131962), 
    cameraTarget=(18.2788, 8.67561, -87.6388), viewOffsetX=14.022, 
    viewOffsetY=-6.56009)
session.viewports['Viewport: 1'].view.setValues(nearPlane=319.131, 
    farPlane=562.226, width=127.798, height=63.3135, cameraPosition=(267.42, 
    346.339, -137.746), cameraUpVector=(-0.941871, 0.260363, -0.212344), 
    cameraTarget=(7.80175, 8.27541, -76.6517), viewOffsetX=13.5061, 
    viewOffsetY=-6.31874)
session.viewports['Viewport: 1'].view.setValues(nearPlane=323.225, 
    farPlane=543.464, width=129.437, height=64.1259, cameraPosition=(130.478, 
    318.257, 179.386), cameraUpVector=(-0.918063, 0.195239, -0.345025), 
    cameraTarget=(-0.728262, -6.4024, -71.2187), viewOffsetX=13.6794, 
    viewOffsetY=-6.3998)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.02636e+006, 
    farPlane=2.92246e+006, width=5.25882e+006, height=2.60532e+006, 
    cameraPosition=(601604, 1.48862e+006, 1.149e+006), viewOffsetX=539707, 
    viewOffsetY=-124697)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['hub']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['bolt1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
elemType1 = mesh.ElemType(elemCode=C3D20, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['bolt1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['bolt2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
elemType1 = mesh.ElemType(elemCode=C3D20, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['bolt2']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['bolt2']
p.generateMesh()
p = mdb.models['Model-1'].parts['bolt1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=173.596, 
    farPlane=294.694, width=77.4254, height=38.3581, cameraPosition=(101.221, 
    170.693, 146.585), cameraUpVector=(-0.793284, 0.51318, -0.327639), 
    cameraTarget=(-1.55875, 52.7921, -26.8062))
p = mdb.models['Model-1'].parts['bolt1']
p.generateMesh()
p = mdb.models['Model-1'].parts['bolt3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
elemType1 = mesh.ElemType(elemCode=C3D20, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['bolt3']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['bolt3']
p.generateMesh()
p = mdb.models['Model-1'].parts['bolt4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
elemType1 = mesh.ElemType(elemCode=C3D20, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['bolt4']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['bolt4']
p.generateMesh()
p = mdb.models['Model-1'].parts['brake']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['hub']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['nut1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.3299, 
    farPlane=72.9461, width=42.2208, height=20.9171, cameraPosition=(17.7629, 
    46.1829, 61.1872), cameraUpVector=(-0.274433, 0.953851, -0.121877), 
    cameraTarget=(0.55336, 54.6345, 5.81211))
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.3307, 
    farPlane=72.9727, width=42.2217, height=20.9175, cameraPosition=(21.5456, 
    50.1707, 60.3412), cameraUpVector=(-0.306258, 0.9378, -0.163518), 
    cameraTarget=(0.55579, 54.6371, 5.81157))
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.3199, 
    farPlane=71.2978, width=43.1639, height=21.3843, cameraPosition=(-3.37581, 
    67.1895, 62.9236), cameraUpVector=(-0.137685, 0.833865, -0.534521), 
    cameraTarget=(0.533953, 54.652, 5.81383))
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.0935, 
    farPlane=71.8242, width=42.9484, height=21.2775, cameraPosition=(10.7973, 
    62.1238, 63.0126), cameraUpVector=(-0.27417, 0.872015, -0.405488), 
    cameraTarget=(0.463096, 54.6773, 5.81339))
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.686, 
    farPlane=75.3604, width=39.703, height=19.6697, cameraPosition=(24.4939, 
    72.8152, 56.0796), cameraUpVector=(-0.411721, 0.778881, -0.473106), 
    cameraTarget=(0.429946, 54.6514, 5.83017))
p = mdb.models['Model-1'].parts['spacer1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=318.083, 
    farPlane=516.699, width=305.731, height=151.465, cameraPosition=(52.6582, 
    101.764, 366.381), cameraUpVector=(-0.347632, 0.787696, -0.508613), 
    cameraTarget=(3.75537, -2.5603, -36.195))
session.viewports['Viewport: 1'].view.setValues(nearPlane=325.406, 
    farPlane=508.258, width=312.77, height=154.952, cameraPosition=(-35.0866, 
    52.7557, 377.013), cameraUpVector=(-0.259289, 0.841151, -0.474589), 
    cameraTarget=(4.03879, -2.402, -36.2293))
session.viewports['Viewport: 1'].view.setValues(nearPlane=314.129, 
    farPlane=517.963, width=301.931, height=149.583, cameraPosition=(-135.407, 
    19.2424, 357.948), cameraUpVector=(-0.177535, 0.867584, -0.46452), 
    cameraTarget=(4.49774, -2.24868, -36.1421))
session.viewports['Viewport: 1'].view.setValues(nearPlane=320.706, 
    farPlane=514.802, width=308.254, height=152.715, cameraPosition=(78.0827, 
    55.4325, 371.652), cameraUpVector=(-0.320622, 0.856321, -0.404866), 
    cameraTarget=(3.11583, -2.48294, -36.2308))
session.viewports['Viewport: 1'].view.setValues(nearPlane=305.883, 
    farPlane=529.789, width=294.007, height=145.657, cameraPosition=(123.933, 
    107.847, 349.205), cameraUpVector=(-0.356882, 0.801452, -0.479905), 
    cameraTarget=(3.00778, -2.60646, -36.1779))
elemType1 = mesh.ElemType(elemCode=C3D20, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['spacer1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['spacer1']
p.generateMesh()
p = mdb.models['Model-1'].parts['spacer2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
elemType1 = mesh.ElemType(elemCode=C3D20, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['spacer2']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['spacer2']
p.generateMesh()
p = mdb.models['Model-1'].parts['washer1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['wheel-centre']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['wheel-centre']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#20 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
elemType1 = mesh.ElemType(elemCode=C3D20, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['wheel-centre']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1f ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['wheel-centre']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=641.51, 
    farPlane=975.153, width=488.438, height=241.982, cameraPosition=(285.407, 
    72.907, 740.247), cameraUpVector=(-0.0511345, 0.995715, -0.0770517))
session.viewports['Viewport: 1'].view.setValues(nearPlane=580.387, 
    farPlane=1036.28, width=441.9, height=218.926, cameraPosition=(409.909, 
    388.496, 565.813), cameraUpVector=(-0.261826, 0.876762, -0.403404), 
    cameraTarget=(9.29832e-006, 2.67029e-005, -12.4995))
session.viewports['Viewport: 1'].view.setValues(nearPlane=662.242, 
    farPlane=954.421, width=504.224, height=249.803, cameraPosition=(264.178, 
    -95.4097, 745.463), cameraUpVector=(-0.0476556, 0.98885, 0.141083), 
    cameraTarget=(8.34465e-006, 1.33514e-005, -12.4995))
session.viewports['Viewport: 1'].view.setValues(nearPlane=608.544, 
    farPlane=1008.12, width=463.34, height=229.548, cameraPosition=(526.779, 
    111.117, 590.457), cameraUpVector=(-0.22584, 0.974002, 0.0178117), 
    cameraTarget=(-8.58307e-006, -9.53674e-007, -12.4995))
session.viewports['Viewport: 1'].view.setValues(nearPlane=570.228, 
    farPlane=1046.43, width=434.167, height=215.095, cameraPosition=(766.304, 
    157.375, -215.995), cameraUpVector=(-0.211707, 0.976426, -0.0421021), 
    cameraTarget=(-1.43051e-005, -2.38419e-007, -12.4994))
session.viewports['Viewport: 1'].view.setValues(nearPlane=670.731, 
    farPlane=945.931, width=510.689, height=253.006, cameraPosition=(229.809, 
    89.5899, -782.279), cameraUpVector=(0.0102006, 0.99289, 0.118601), 
    cameraTarget=(6.96182e-005, 1.35899e-005, -12.4993))
session.viewports['Viewport: 1'].view.setValues(nearPlane=687.43, 
    farPlane=929.232, width=523.404, height=259.305, cameraPosition=(99.3705, 
    66.4777, -811.94), cameraUpVector=(-0.00213147, 0.99658, 0.0826054), 
    cameraTarget=(9.5129e-005, 1.79112e-005, -12.4993))
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=737.883, 
    farPlane=1068.92, width=250.767, height=124.235, cameraPosition=(268.299, 
    79.0808, 809.668), cameraUpVector=(-0.36829, 0.871667, -0.323355), 
    cameraTarget=(9.1798, -4.46359, -49.4735), viewOffsetX=-10.0666, 
    viewOffsetY=7.7093)
session.viewports['Viewport: 1'].view.setValues(nearPlane=787.946, 
    farPlane=1022.06, width=267.781, height=132.664, cameraPosition=(0.16066, 
    2.70931, 855.655), cameraUpVector=(-0.219656, 0.913099, -0.343513), 
    cameraTarget=(8.76355, -5.23939, -45.5158), viewOffsetX=-10.7496, 
    viewOffsetY=8.23235)
session.viewports['Viewport: 1'].view.setValues(nearPlane=628.891, 
    farPlane=1173.87, width=213.727, height=105.885, cameraPosition=(695.882, 
    490.545, 246.797), cameraUpVector=(-0.673521, 0.595465, -0.43794), 
    cameraTarget=(7.41562, -6.17031, -55.7485), viewOffsetX=-8.57969, 
    viewOffsetY=6.57057)
session.viewports['Viewport: 1'].view.setValues(nearPlane=648.97, 
    farPlane=1150.58, width=220.551, height=109.266, cameraPosition=(718.672, 
    309.098, -494.069), cameraUpVector=(-0.706308, 0.706958, 0.0365928), 
    cameraTarget=(-2.76217, -9.31528, -57.7291), viewOffsetX=-8.85361, 
    viewOffsetY=6.78035)
session.viewports['Viewport: 1'].view.setValues(nearPlane=636.741, 
    farPlane=1164.15, width=216.396, height=107.207, cameraPosition=(717.411, 
    465.632, -331.316), cameraUpVector=(-0.798542, 0.600364, 0.0435203), 
    cameraTarget=(0.151373, -7.68743, -59.7386), viewOffsetX=-8.68678, 
    viewOffsetY=6.65259)
session.viewports['Viewport: 1'].view.setValues(nearPlane=653.555, 
    farPlane=1148.08, width=222.111, height=110.038, cameraPosition=(601.185, 
    357.089, 518.671), cameraUpVector=(-0.669069, 0.693866, -0.266263), 
    cameraTarget=(9.25852, -2.11183, -58.256), viewOffsetX=-8.91617, 
    viewOffsetY=6.82827)
session.viewports['Viewport: 1'].view.setValues(nearPlane=701.5, 
    farPlane=1100.43, width=238.405, height=118.111, cameraPosition=(362.943, 
    209.482, 748.282), cameraUpVector=(-0.518743, 0.779125, -0.351953), 
    cameraTarget=(11.7077, -1.41311, -54.4661), viewOffsetX=-9.57026, 
    viewOffsetY=7.32919)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Part']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].view.setValues(nearPlane=762.559, 
    farPlane=1040.6, width=259.157, height=128.391, cameraPosition=(27.0737, 
    142.59, 840.513), cameraUpVector=(-0.333537, 0.819958, -0.465212), 
    cameraTarget=(12.6069, -1.59483, -49.0088), viewOffsetX=-10.4033, 
    viewOffsetY=7.96713)
session.viewports['Viewport: 1'].view.setValues(nearPlane=680.979, 
    farPlane=1125.76, width=231.432, height=114.656, cameraPosition=(-867.958, 
    -78.4515, 188.807), cameraUpVector=(0.237487, 0.965602, -0.10589), 
    cameraTarget=(1.36577, -5.97263, -37.6239), viewOffsetX=-9.29033, 
    viewOffsetY=7.11479)
session.viewports['Viewport: 1'].view.setValues(nearPlane=750.633, 
    farPlane=1058.25, width=255.104, height=126.384, cameraPosition=(-243.493, 
    11.1816, -920.477), cameraUpVector=(-0.300609, 0.841927, 0.4481), 
    cameraTarget=(-7.92411, -10.7398, -50.8361), viewOffsetX=-10.2406, 
    viewOffsetY=7.84253)
session.viewports['Viewport: 1'].view.setValues(nearPlane=725.111, 
    farPlane=1083.63, width=246.431, height=122.087, cameraPosition=(-410.656, 
    -24.1874, -854.903), cameraUpVector=(-0.194126, 0.869172, 0.454813), 
    cameraTarget=(-8.27703, -10.6086, -48.581), viewOffsetX=-9.89242, 
    viewOffsetY=7.57588)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=645.687, 
    farPlane=1166.13, width=220.326, height=108.714, cameraPosition=(-793.567, 
    395.256, -236.17), cameraUpVector=(0.629231, 0.669479, 0.394799), 
    cameraTarget=(-10.5409, -6.49197, -41.9617), viewOffsetX=-8.80887, 
    viewOffsetY=6.74607)
session.viewports['Viewport: 1'].view.setValues(nearPlane=652.637, 
    farPlane=1159.72, width=222.698, height=109.884, cameraPosition=(-553.508, 
    443.565, -613.503), cameraUpVector=(0.374637, 0.633029, 0.677438), 
    cameraTarget=(-13.0543, -5.58832, -49.2171), viewOffsetX=-8.90369, 
    viewOffsetY=6.81868)
session.viewports['Viewport: 1'].view.setValues(nearPlane=679.087, 
    farPlane=1133.27, width=40.5288, height=19.9979, viewOffsetX=-20.3357, 
    viewOffsetY=-13.5599)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['hub-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#400000 ]', ), )
region = regionToolset.Region(faces=faces1)
mdb.models['Model-1'].DisplacementBC(name='hub-axial', 
    createStepName='Initial', region=region, u1=UNSET, u2=UNSET, u3=SET, 
    ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['hub-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#200000 ]', ), )
region = regionToolset.Region(faces=faces1)
mdb.models['Model-1'].DisplacementBC(name='hub radial', 
    createStepName='Initial', region=region, u1=SET, u2=SET, u3=UNSET, 
    ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=601.659, 
    farPlane=1210.69, width=478.088, height=235.9, viewOffsetX=46.5157, 
    viewOffsetY=22.2329)
session.viewports['Viewport: 1'].view.setValues(nearPlane=667.29, 
    farPlane=1216.46, width=530.24, height=261.633, cameraPosition=(-876.037, 
    169.301, -351.482), cameraUpVector=(0.402798, 0.832043, 0.381391), 
    cameraTarget=(-40.9324, -6.67696, -61.8609), viewOffsetX=51.5898, 
    viewOffsetY=24.6581)
session.viewports['Viewport: 1'].view.setValues(nearPlane=729.514, 
    farPlane=1244.72, width=579.685, height=286.031, cameraPosition=(-953.833, 
    -59.8092, 198.577), cameraUpVector=(0.326494, 0.941891, 0.0790109), 
    cameraTarget=(-84.9033, -22.2477, -37.639), viewOffsetX=56.4005, 
    viewOffsetY=26.9575)
session.viewports['Viewport: 1'].view.setValues(nearPlane=797.622, 
    farPlane=1274.69, width=633.805, height=312.735, cameraPosition=(-552.07, 
    -63.4263, 825.933), cameraUpVector=(0.217774, 0.951644, -0.216677), 
    cameraTarget=(-92.8265, -29.2301, 51.2245), viewOffsetX=61.6661, 
    viewOffsetY=29.4743)
session.viewports['Viewport: 1'].view.setValues(nearPlane=865.55, 
    farPlane=1282.86, width=687.783, height=339.369, cameraPosition=(205.02, 
    -8.15032, 1006.3), cameraUpVector=(-0.0810261, 0.935293, -0.344473), 
    cameraTarget=(-0.377361, -27.862, 128.994), viewOffsetX=66.9178, 
    viewOffsetY=31.9844)
session.viewports['Viewport: 1'].view.setValues(nearPlane=802.97, 
    farPlane=1377.92, width=638.056, height=314.832, cameraPosition=(558.013, 
    230.343, 860.381), cameraUpVector=(-0.272562, 0.834674, -0.47857), 
    cameraTarget=(69.2197, 14.5182, 134.611), viewOffsetX=62.0796, 
    viewOffsetY=29.6719)
mdb.save()
#: The model database has been saved to "C:\Users\Ali\Documents\MEGA\University\5th_Year\FEM 4\My_Stuff\Kick Ass Wheel Centre\Abaqus Files\Validation FEA\Rear Wheel Assembly .cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Preload-Test', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', multiprocessingMode=THREADS, numCpus=4, numDomains=4, 
    numGPUs=0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=824.313, 
    farPlane=1356.58, width=462.179, height=241.055, viewOffsetX=57.2241, 
    viewOffsetY=28.0382)
session.viewports['Viewport: 1'].view.setValues(nearPlane=848.819, 
    farPlane=1384.03, width=475.919, height=248.222, cameraPosition=(1078.55, 
    293.239, -5.79149), cameraUpVector=(-0.584294, 0.786003, -0.20199), 
    cameraTarget=(214.532, 37.4429, 10.8962), viewOffsetX=58.9253, 
    viewOffsetY=28.8718)
session.viewports['Viewport: 1'].view.setValues(nearPlane=832.036, 
    farPlane=1367.59, width=466.51, height=243.314, cameraPosition=(519.85, 
    348.228, 858.277), cameraUpVector=(-0.443615, 0.756841, -0.479997), 
    cameraTarget=(59.3339, 27.8811, 152.912), viewOffsetX=57.7602, 
    viewOffsetY=28.301)
session.viewports['Viewport: 1'].view.setValues(nearPlane=853.542, 
    farPlane=1346.08, width=283.649, height=147.941, viewOffsetX=51.6959, 
    viewOffsetY=38.141)
session.viewports['Viewport: 1'].view.setValues(nearPlane=841.51, 
    farPlane=1360.3, width=279.651, height=145.855, cameraPosition=(990.794, 
    401.237, 224.914), cameraUpVector=(-0.601467, 0.718836, -0.348586), 
    cameraTarget=(174.367, 56.541, 61), viewOffsetX=50.9671, 
    viewOffsetY=37.6033)
session.viewports['Viewport: 1'].view.setValues(nearPlane=837.94, 
    farPlane=1367.9, width=278.465, height=145.237, cameraPosition=(980.972, 
    482.167, -215.651), cameraUpVector=(-0.753588, 0.620514, -0.216949), 
    cameraTarget=(197.152, 83.0396, -19.2856), viewOffsetX=50.7509, 
    viewOffsetY=37.4438)
session.viewports['Viewport: 1'].view.setValues(nearPlane=830.186, 
    farPlane=1379.71, width=275.888, height=143.893, cameraPosition=(871.541, 
    621.028, -334.87), cameraUpVector=(-0.849139, 0.5275, -0.0265905), 
    cameraTarget=(189.436, 107.017, -47.1881), viewOffsetX=50.2812, 
    viewOffsetY=37.0973)
session.viewports['Viewport: 1'].view.setValues(nearPlane=893.853, 
    farPlane=1305.76, width=297.046, height=154.928, cameraPosition=(560.553, 
    47.4469, 899.09), cameraUpVector=(-0.355828, 0.897249, -0.261403), 
    cameraTarget=(60.7114, -33.1809, 153.508), viewOffsetX=54.1373, 
    viewOffsetY=39.9423)
session.viewports['Viewport: 1'].view.setValues(nearPlane=898.265, 
    farPlane=1296.11, width=298.512, height=155.693, cameraPosition=(-92.0149, 
    -645.268, 836.913), cameraUpVector=(-0.104579, 0.966051, 0.236237), 
    cameraTarget=(-69.4313, -148.114, 85.5388), viewOffsetX=54.4045, 
    viewOffsetY=40.1394)
session.viewports['Viewport: 1'].view.setValues(nearPlane=918.148, 
    farPlane=1278.98, width=305.12, height=159.139, cameraPosition=(9.55112, 
    -420.791, 968.573), cameraUpVector=(-0.148656, 0.988812, 0.0123479), 
    cameraTarget=(-50.5104, -115.447, 122.764), viewOffsetX=55.6087, 
    viewOffsetY=41.0279)
session.viewports['Viewport: 1'].view.setValues(nearPlane=870.565, 
    farPlane=1332.66, width=289.307, height=150.892, cameraPosition=(400.651, 
    351.318, 918.271), cameraUpVector=(-0.41488, 0.746748, -0.519847), 
    cameraTarget=(33.0716, 23.861, 163.359), viewOffsetX=52.7268, 
    viewOffsetY=38.9016)
session.viewports['Viewport: 1'].view.setValues(nearPlane=862.002, 
    farPlane=1341.23, width=421.268, height=219.717, viewOffsetX=67.4288, 
    viewOffsetY=38.7902)
session.viewports['Viewport: 1'].view.setValues(nearPlane=865.746, 
    farPlane=1334.02, width=423.097, height=220.672, cameraPosition=(604.627, 
    -169.239, 857.431), cameraUpVector=(-0.265166, 0.959683, -0.0932552), 
    cameraTarget=(65.6153, -74.7214, 141.353), viewOffsetX=67.7216, 
    viewOffsetY=38.9587)
session.viewports['Viewport: 1'].view.setValues(nearPlane=830.14, 
    farPlane=1364.93, width=405.697, height=211.596, cameraPosition=(557.97, 
    -466.943, 776.501), cameraUpVector=(-0.155412, 0.974463, 0.162076), 
    cameraTarget=(51.0248, -129.048, 112.371), viewOffsetX=64.9364, 
    viewOffsetY=37.3564)
session.viewports['Viewport: 1'].view.setValues(nearPlane=881.51, 
    farPlane=1316.97, width=430.802, height=224.69, cameraPosition=(543.301, 
    -101.753, 904.369), cameraUpVector=(-0.282235, 0.944881, -0.16596), 
    cameraTarget=(53.6693, -62.789, 148.738), viewOffsetX=68.9548, 
    viewOffsetY=39.6681)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
mdb.models['Model-1'].constraints.delete(('CP-4-bolt1-1-nut1-1', 
    'CP-8-bolt2-1-nut2-1', 'CP-12-bolt3-1-nut3-1', 'CP-16-bolt4-1-nut4-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=938.119, 
    farPlane=1260.36, width=29.7758, height=14.6921, viewOffsetX=44.1043, 
    viewOffsetY=89.0478)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['bolt1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['nut1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#200 ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].Tie(name='Nut-bolt1', master=region1, slave=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3577.14, 
    farPlane=3954.38, width=181.698, height=89.6544, cameraPosition=(1991.98, 
    -217.037, 3140.07), viewOffsetX=50.4087, viewOffsetY=90.7672)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3591.28, 
    farPlane=3940.24, width=103.518, height=51.0783, viewOffsetX=12.3837, 
    viewOffsetY=58.231)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['bolt4-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt4-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['nut4-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#200 ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].Tie(name='bolt-nut2', master=region1, slave=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3589.98, 
    farPlane=3941.54, width=110.693, height=54.6189, viewOffsetX=38.6444, 
    viewOffsetY=13.0711)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['bolt3-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3607.07, 
    farPlane=3924.45, width=16.3402, height=8.06265, viewOffsetX=31.5189, 
    viewOffsetY=-3.8864)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt3-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['nut3-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#200 ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].Tie(name='bolt-nut3', master=region1, slave=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3595.42, 
    farPlane=3936.1, width=80.6402, height=39.7899, viewOffsetX=76.6701, 
    viewOffsetY=41.3839)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['bolt2-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3605.71, 
    farPlane=3925.81, width=23.8643, height=11.7752, viewOffsetX=80.7645, 
    viewOffsetY=40.2133)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['nut2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#200 ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].Tie(name='bolt-nut4', master=region1, slave=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3600.68, 
    farPlane=3930.84, width=73.0408, height=36.0401, viewOffsetX=75.9688, 
    viewOffsetY=41.9128)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3501.37, 
    farPlane=4030.15, width=840.856, height=414.899, viewOffsetX=58.7559, 
    viewOffsetY=76.7306)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.jobs['Preload-Test'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Preload-Test.inp" has been submitted for analysis.
mdb.save()
#: The model database has been saved to "C:\Users\Ali\Documents\MEGA\University\5th_Year\FEM 4\My_Stuff\Kick Ass Wheel Centre\Abaqus Files\Validation FEA\Rear Wheel Assembly .cae".
#: Error in job Preload-Test: 353921 elements have missing property definitions. The elements have been identified in element set ErrElemMissingSection.
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['wheel-centre']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#: Job Preload-Test: Analysis Input File Processor aborted due to errors.
#: Job Preload-Test: Analysis Input File Processor aborted due to errors.
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Elastic(table=((210000.0, 0.3), ))
#: 
#: Point 1: 0., 55., -25.  Point 2: 0., -55., -25.
#:    Distance: 110.  Components: 0., -110., 0.
mdb.models['Model-1'].Material(name='Aluminium')
mdb.models['Model-1'].materials['Aluminium'].Elastic(table=((70000.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Steel', material='Steel', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='Aluminium', 
    material='Aluminium', thickness=None)
p = mdb.models['Model-1'].parts['wheel-centre']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3f ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['wheel-centre']
p.SectionAssignment(region=region, sectionName='Aluminium', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['bolt1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['bolt1']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['bolt2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt2']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['bolt2']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['bolt3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt3']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['bolt3']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['bolt4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['bolt4']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['bolt4']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['brake']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['brake']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['brake']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['hub']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['hub']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['hub']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['nut1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['nut1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['nut1']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['nut2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['nut2']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['nut2']
p.SectionAssignment(region=region, sectionName='Aluminium', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['nut3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['nut3']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['nut3']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['nut4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['nut4']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['nut4']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['spacer1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['spacer1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['spacer1']
p.SectionAssignment(region=region, sectionName='Aluminium', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['spacer2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['spacer2']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['spacer2']
p.SectionAssignment(region=region, sectionName='Aluminium', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['washer1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['washer1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['washer1']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['washer2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['washer2']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['washer2']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['washer3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['washer3']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['washer3']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['washer4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['washer4']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['washer4']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['wheel-centre']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Section']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].view.setValues(nearPlane=3533.71, 
    farPlane=3997.81, width=422.505, height=208.474, viewOffsetX=75.8198, 
    viewOffsetY=59.6681)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3522.05, 
    farPlane=4021.44, width=421.112, height=207.787, cameraPosition=(2131.72, 
    786.856, 2962.2), cameraUpVector=(-0.404862, 0.838834, -0.363929), 
    cameraTarget=(71.7913, -5.75594, 159.097), viewOffsetX=75.5697, 
    viewOffsetY=59.4713)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3563.86, 
    farPlane=3979.62, width=125.741, height=62.0439, viewOffsetX=78.4331, 
    viewOffsetY=35.8782)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['wheel-centre']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['washer4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['washer4']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['washer4']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3554.67, 
    farPlane=3988.82, width=176.588, height=87.1329, viewOffsetX=75.687, 
    viewOffsetY=34.1356)
p = mdb.models['Model-1'].parts['washer4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].parts['washer4'].sectionAssignments[1]
p = mdb.models['Model-1'].parts['washer3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['washer2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['washer1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Material']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Material']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].view.setValues(nearPlane=3535.32, 
    farPlane=4008.16, width=283.706, height=139.987, viewOffsetX=70.6025, 
    viewOffsetY=35.3672)
p = mdb.models['Model-1'].parts['washer1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['nut1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].parts['nut1'].sectionAssignments[0]
p = mdb.models['Model-1'].parts['nut1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['nut1']
p.SectionAssignment(region=region, sectionName='Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['nut2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['nut2'].sectionAssignments[0].setValues(
    sectionName='Steel')
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3536.45, 
    farPlane=4012.7, width=283.796, height=140.032, cameraPosition=(3636.15, 
    1015.63, -10.1058), cameraUpVector=(-0.578575, 0.798014, -0.168593), 
    cameraTarget=(207.918, 28.3382, 27.6533), viewOffsetX=70.625, 
    viewOffsetY=35.3784)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3521.72, 
    farPlane=4028.46, width=282.614, height=139.449, cameraPosition=(2997.25, 
    1089.44, -2071.31), cameraUpVector=(-0.680398, 0.732272, 0.0289193), 
    cameraTarget=(213.181, 48.7141, -97.7787), viewOffsetX=70.3309, 
    viewOffsetY=35.2311)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3604.25, 
    farPlane=3951.87, width=289.238, height=142.717, cameraPosition=(763.354, 
    -678.817, -3687.71), cameraUpVector=(-0.681182, 0.727882, 0.0786059), 
    cameraTarget=(118.892, -20.2986, -240.968), viewOffsetX=71.9791, 
    viewOffsetY=36.0568)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3540.24, 
    farPlane=4016.28, width=284.101, height=140.182, cameraPosition=(-2169.83, 
    -1036.98, -2964.63), cameraUpVector=(-0.449291, 0.724839, 0.522251), 
    cameraTarget=(-65.0287, -38.5755, -262.401), viewOffsetX=70.7008, 
    viewOffsetY=35.4164)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3531.84, 
    farPlane=4036.43, width=283.427, height=139.85, cameraPosition=(-1021.76, 
    -3405.53, 1248.73), cameraUpVector=(-0.536141, 0.714028, 0.45024), 
    cameraTarget=(-82.3642, -217.136, -47.6931), viewOffsetX=70.533, 
    viewOffsetY=35.3323)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3617.06, 
    farPlane=3950.92, width=290.266, height=143.224, cameraPosition=(-38.1754, 
    -1300.52, 3504.86), cameraUpVector=(-0.375949, 0.926135, -0.0306141), 
    cameraTarget=(-50.9249, -133.037, 133.534), viewOffsetX=72.2349, 
    viewOffsetY=36.1848)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3606.27, 
    farPlane=3959.53, width=289.4, height=142.797, cameraPosition=(-852.905, 
    497.256, 3603.4), cameraUpVector=(-0.702925, 0.41662, -0.576475), 
    cameraTarget=(-53.8461, -51.1375, 169.769), viewOffsetX=72.0194, 
    viewOffsetY=36.0769)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3577.11, 
    farPlane=3990.79, width=287.06, height=141.642, cameraPosition=(-66.8528, 
    -2521.96, 2772.07), cameraUpVector=(-0.863283, 0.503792, -0.0305869), 
    cameraTarget=(3.90926, -204.755, 60.1383), viewOffsetX=71.437, 
    viewOffsetY=35.7852)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3539.81, 
    farPlane=4025.84, width=284.067, height=140.165, cameraPosition=(-1784.77, 
    -1673.03, 2837.22), cameraUpVector=(-0.616495, 0.638194, -0.461132), 
    cameraTarget=(-92.9576, -167.101, 80.5931), viewOffsetX=70.6921, 
    viewOffsetY=35.412)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.save()
#: The model database has been saved to "C:\Users\Ali\Documents\MEGA\University\5th_Year\FEM 4\My_Stuff\Kick Ass Wheel Centre\Abaqus Files\Validation FEA\Rear Wheel Assembly .cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Preload-Test'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Preload-Test.inp".
mdb.jobs['Preload-Test'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Preload-Test.inp" has been submitted for analysis.
#: Error in job Preload-Test: XML parsing failure for job Preload-Test.  Shutting down socket and terminating all further messages.  Please check the .log, .dat, .sta, or .msg files for information about the status of the job.
#: Error in job Preload-Test: XML parsing failure for job Preload-Test.  Shutting down socket and terminating all further messages.  Please check the .log, .dat, .sta, or .msg files for information about the status of the job.
#: Job Preload-Test aborted due to errors.
#: Job Preload-Test aborted due to errors.
#: Error in job Preload-Test: XML parsing failure for job Preload-Test.  Shutting down socket and terminating all further messages.  Please check the .log, .dat, .sta, or .msg files for information about the status of the job.
#: Job Preload-Test aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Wheel-load')
mdb.models['Model-1'].steps['Wheel-load'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Preload-Test'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Preload-Test.inp".
mdb.save()
#: The model database has been saved to "C:\Users\Ali\Documents\MEGA\University\5th_Year\FEM 4\My_Stuff\Kick Ass Wheel Centre\Abaqus Files\Validation FEA\Rear Wheel Assembly .cae".
mdb.jobs['Preload-Test'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Preload-Test.inp" has been submitted for analysis.
#: Error in job Preload-Test: Detected lock file Preload-Test.lck. Please confirm that no other applications are attempting to write to the output database associated with this job before removing the lock file and resubmitting.
#: Job Preload-Test aborted due to errors.
mdb.jobs['Preload-Test'].submit(consistencyChecking=OFF)
#: The job input file "Preload-Test.inp" has been submitted for analysis.
#: Error in job Preload-Test: Unable to delete file(s) ["C:\\Users\\Ali\\Documents\\MEGA\\University\\5th_Year\\FEM 4\\My_Stuff\\Kick Ass Wheel Centre\\Abaqus Files\\Validation FEA\\Preload-Test.023"]. Please check that you have file ownership and permissions for removal.
#: Job Preload-Test aborted due to errors.
mdb.jobs['Preload-Test'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Preload-Test.inp" has been submitted for analysis.
mdb.jobs['Preload-Test'].kill()
#: Error in job Preload-Test: Process terminated by external request (SIGTERM or SIGINT received).
#: Job Preload-Test: Analysis Input File Processor was terminated prior to analysis completion.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
#: Error in job Preload-Test: Analysis Input File Processor exited with an error.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Preload')
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['nut2-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#20 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['wheel-centre-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
i1 = a.instances['spacer2-1']
leaf = dgm.LeafFromInstance((i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3574.94, 
    farPlane=3990.71, width=170.039, height=83.9013, viewOffsetX=69.4522, 
    viewOffsetY=54.023)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=609.241, 
    farPlane=1076.71, width=208.369, height=102.815, viewOffsetX=-11.0433, 
    viewOffsetY=19.9136)
session.viewports['Viewport: 1'].view.setValues(nearPlane=635.141, 
    farPlane=1067.86, width=217.228, height=107.185, cameraPosition=(337.195, 
    767.489, 100.698), cameraUpVector=(-0.949911, 0.0964314, -0.297271), 
    cameraTarget=(13.7226, 5.41978, -58.1079), viewOffsetX=-11.5128, 
    viewOffsetY=20.7602)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt1-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(side2Faces=side2Faces1)
datumAxis = mdb.models['Model-1'].rootAssembly.instances['bolt1-1'].datums[4]
mdb.models['Model-1'].BoltLoad(name='bolt-preload-1', createStepName='Preload', 
    region=region, magnitude=28100.0, boltMethod=APPLY_FORCE, 
    datumAxis=datumAxis)
session.viewports['Viewport: 1'].view.setValues(nearPlane=621.68, 
    farPlane=1065.57, width=212.624, height=104.914, cameraPosition=(479.156, 
    415.195, 507.404), cameraUpVector=(-0.879708, 0.463, -0.108371), 
    cameraTarget=(12.7081, 2.80934, -60.8985), viewOffsetX=-11.2688, 
    viewOffsetY=20.3202)
session.viewports['Viewport: 1'].view.setValues(nearPlane=720.621, 
    farPlane=969.872, width=246.464, height=121.611, cameraPosition=(96.1571, 
    26.6724, 790.083), cameraUpVector=(-0.656538, 0.695147, -0.292795), 
    cameraTarget=(15.783, 1.69551, -48.6776), viewOffsetX=-13.0622, 
    viewOffsetY=23.5542)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=627.36, 
    farPlane=1058.59, width=106.827, height=52.7108, viewOffsetX=-42.7141, 
    viewOffsetY=11.395)
session.viewports['Viewport: 1'].view.setValues(nearPlane=675.463, 
    farPlane=1049.38, width=115.017, height=56.7524, cameraPosition=(209.996, 
    546.622, 583.912), cameraUpVector=(-0.478867, 0.485745, -0.731258), 
    cameraTarget=(17.0147, 5.7865, -33.2259), viewOffsetX=-45.9892, 
    viewOffsetY=12.2687)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt4-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(side2Faces=side2Faces1)
datumAxis = mdb.models['Model-1'].rootAssembly.instances['bolt4-1'].datums[2]
mdb.models['Model-1'].BoltLoad(name='bolt-preload-2', createStepName='Preload', 
    region=region, magnitude=28100.0, boltMethod=APPLY_FORCE, 
    datumAxis=datumAxis)
session.viewports['Viewport: 1'].view.setValues(nearPlane=698.416, 
    farPlane=1103.09, width=118.926, height=58.6809, cameraPosition=(-389.829, 
    -460.321, 620.826), cameraUpVector=(-0.413795, 0.909025, -0.0494682), 
    cameraTarget=(-6.29567, -9.27522, 20.7721), viewOffsetX=-47.552, 
    viewOffsetY=12.6856)
session.viewports['Viewport: 1'].view.setValues(nearPlane=743.988, 
    farPlane=1077.41, width=126.686, height=62.51, cameraPosition=(-454.941, 
    103.575, 733.362), cameraUpVector=(0.159063, 0.895783, -0.415057), 
    cameraTarget=(-8.47906, 9.54868, 24.535), viewOffsetX=-50.6548, 
    viewOffsetY=13.5133)
session.viewports['Viewport: 1'].view.setValues(nearPlane=720.031, 
    farPlane=1101.37, width=234.247, height=115.583, viewOffsetX=-54.4633, 
    viewOffsetY=1.62802)
mdb.models['Model-1'].Load(name='bolt-preload-3', 
    objectToCopy=mdb.models['Model-1'].loads['bolt-preload-2'], 
    toStepName='Preload')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt3-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(side2Faces=side2Faces1)
datumAxis = mdb.models['Model-1'].rootAssembly.instances['bolt3-1'].datums[2]
mdb.models['Model-1'].loads['bolt-preload-3'].setValues(region=region, 
    datumAxis=datumAxis)
mdb.models['Model-1'].Load(name='bolt-preload-4', 
    objectToCopy=mdb.models['Model-1'].loads['bolt-preload-3'], 
    toStepName='Preload')
session.viewports['Viewport: 1'].view.setValues(nearPlane=693.175, 
    farPlane=1061.09, width=225.51, height=111.272, cameraPosition=(537.798, 
    91.4147, 639.671), cameraUpVector=(-0.46484, 0.868364, -0.172826), 
    cameraTarget=(60.9462, 22.0812, -52.0012), viewOffsetX=-52.4319, 
    viewOffsetY=1.56729)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['bolt2-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(side2Faces=side2Faces1)
datumAxis = mdb.models['Model-1'].rootAssembly.instances['bolt2-1'].datums[2]
mdb.models['Model-1'].loads['bolt-preload-4'].setValues(region=region, 
    datumAxis=datumAxis)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Preload-Test'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Preload-Test.inp".
mdb.save()
#: The model database has been saved to "C:\Users\Ali\Documents\MEGA\University\5th_Year\FEM 4\My_Stuff\Kick Ass Wheel Centre\Abaqus Files\Validation FEA\Rear Wheel Assembly .cae".
mdb.jobs['Preload-Test'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Preload-Test.inp" has been submitted for analysis.
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Part instance']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
#: Job Preload-Test: Analysis Input File Processor completed successfully.
#: !The memory allocation for job Preload-Test was increased to 16131MB based on the analysis estimates.
#: Job Preload-Test: Abaqus/Standard completed successfully.
#: Job Preload-Test completed successfully. 
mdb.save()
#: The model database has been saved to "C:\Users\Ali\Documents\MEGA\University\5th_Year\FEM 4\My_Stuff\Kick Ass Wheel Centre\Abaqus Files\Validation FEA\Rear Wheel Assembly .cae".
