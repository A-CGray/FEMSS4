# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.12-1 replay file
# Internal Version: 2012_03_13-20.21.46 119612
# Run by s1208454 on Mon Nov 14 16:44:18 2016
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
openMdb(
    '/home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Abaqus Files/2nd_attempt.cae')
#: The model database "/home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Abaqus Files/2nd_attempt.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.650764, 
    farPlane=1.01781, width=0.126129, height=0.0767577, viewOffsetX=-0.0164808, 
    viewOffsetY=-0.0106751)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.708977, 
    farPlane=0.974834, width=0.137412, height=0.0836239, cameraPosition=(
    0.533797, 0.136272, 0.649202), cameraUpVector=(-0.38096, 0.872405, 
    -0.306233), cameraTarget=(0.0117888, 0.00345338, 0.0120953), 
    viewOffsetX=-0.0179551, viewOffsetY=-0.01163)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#f0 #0 #3c00 ]', ), )
p.Set(faces=faces, name='hub-holes')
#: The set 'hub-holes' has been created (8 faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.703954, 
    farPlane=0.979858, width=0.184733, height=0.112422, 
    viewOffsetX=-0.00656501, viewOffsetY=-0.00749148)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#0 #360000 ]', ), )
p.Set(faces=faces, name='hub-washers')
#: The set 'hub-washers' has been created (4 faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.695008, 
    farPlane=0.988804, width=0.284458, height=0.173111, 
    viewOffsetX=-0.00224926, viewOffsetY=-0.00151805)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.646915, 
    farPlane=1.04927, width=0.264774, height=0.161132, cameraPosition=(
    0.692457, -0.313365, -0.363796), cameraUpVector=(-0.130254, 0.948125, 
    -0.289988), cameraTarget=(0.0102849, -0.00193822, 0.00184358), 
    viewOffsetX=-0.00209362, viewOffsetY=-0.00141301)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.695459, 
    farPlane=1.00265, width=0.284642, height=0.173223, cameraPosition=(
    0.597083, -0.11567, -0.579983), cameraUpVector=(-0.203184, 0.976257, 
    0.075085), cameraTarget=(0.00810955, 0.00207392, -0.00094498), 
    viewOffsetX=-0.00225072, viewOffsetY=-0.00151904)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#0 #8000 ]', ), )
p.Set(faces=faces, name='hub-interface')
#: The set 'hub-interface' has been created (1 face).
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.676109, 
    farPlane=1.02084, width=0.276722, height=0.168403, cameraPosition=(
    0.779616, 0.0685653, 0.340279), cameraUpVector=(-0.361943, 0.914594, 
    -0.180321), cameraTarget=(0.0140845, 0.00548072, 0.0146719), 
    viewOffsetX=-0.0021881, viewOffsetY=-0.00147677)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#0 #80000 ]', ), )
p.Set(faces=faces, name='perimeter-interface')
#: The set 'perimeter-interface' has been created (1 face).
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2000000 #1000000 ]', ), )
p.Set(faces=faces, name='centre-hole')
#: The set 'centre-hole' has been created (2 faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.678691, 
    farPlane=1.01898, width=0.277779, height=0.169046, cameraPosition=(
    0.818986, 0.0279503, -0.20893), cameraUpVector=(-0.350325, 0.933138, 
    0.0807759), cameraTarget=(0.013042, 0.00484162, 0.00544968), 
    viewOffsetX=-0.00219646, viewOffsetY=-0.00148241)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.690758, 
    farPlane=1.00736, width=0.282718, height=0.172052, cameraPosition=(
    0.720432, 0.0350312, -0.435475), cameraUpVector=(-0.296694, 0.929762, 
    0.217982), cameraTarget=(0.010657, 0.00508163, 0.00197391), 
    viewOffsetX=-0.00223551, viewOffsetY=-0.00150877)
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.767582, 
    farPlane=0.84772, width=0.295503, height=0.179833, cameraPosition=(
    0.00555463, -0.0771333, -0.795151), cameraTarget=(0.00555463, -0.0771333, 
    0.0125))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#c0000000 #7fff #8000 ]', ), )
p.Set(faces=faces, name='perimeter-washers')
#: The set 'perimeter-washers' has been created (18 faces).
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(seeds=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(seeds=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.62476, 
    farPlane=0.990542, cameraPosition=(0.451232, 0.208295, 0.649134), 
    cameraUpVector=(-0.385621, 0.822246, -0.418579), cameraTarget=(
    -2.09548e-09, -3.72529e-09, 0.0125))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.617135, 
    farPlane=0.998166, width=0.717602, height=0.436707, cameraPosition=(
    0.472471, 0.194212, 0.638687), cameraTarget=(0.0212393, -0.014083, 
    0.00205371))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#5ffff00 #fe800000 #3ff ]', ), )
p.Set(faces=faces, name='perimeter-holes')
#: The set 'perimeter-holes' has been created (36 faces).
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#0 #360000 ]', ), )
p.Surface(side1Faces=side1Faces, name='hub-washers')
#: The surface 'hub-washers' has been created (4 faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.592307, 
    farPlane=1.023, width=0.467149, height=0.28429, cameraPosition=(0.468436, 
    0.457923, 0.485033), cameraTarget=(0.0021384, -0.00837418, 0.0187358))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.643799, 
    farPlane=0.980457, cameraPosition=(0.508361, 0.143807, 0.629374), 
    cameraUpVector=(-0.364893, 0.861503, -0.35308), cameraTarget=(0.0021384, 
    -0.00837417, 0.0187358))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.658566, 
    farPlane=0.965689, width=0.299522, height=0.182278, cameraPosition=(
    0.504163, 0.164909, 0.627595), cameraTarget=(-0.0020596, 0.0127275, 
    0.0169571))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#f0 #0 #3c00 ]', ), )
p.Surface(side1Faces=side1Faces, name='hub-holes')
#: The surface 'hub-holes' has been created (8 faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.610401, 
    farPlane=1.00976, cameraPosition=(0.779573, 0.201385, -0.077515), 
    cameraUpVector=(-0.470649, 0.746098, 0.470985), cameraTarget=(-0.000541311, 
    0.0129286, 0.01307))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.636389, 
    farPlane=0.971662, cameraPosition=(0.50481, -0.225964, -0.571186), 
    cameraUpVector=(0.0494636, 0.993784, 0.0997311), cameraTarget=(-0.00136543, 
    0.0116468, 0.0115893))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#2000000 #1000000 ]', ), )
p.Surface(side1Faces=side1Faces, name='hub-interface')
#: The surface 'hub-interface' has been created (2 faces).
mdb.models['Model-1'].parts['Wheel Centre Blank2'].surfaces.changeKey(
    fromName='hub-interface', toName='centre-hole')
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#0 #8000 ]', ), )
p.Surface(side1Faces=side1Faces, name='hub-interface')
#: The surface 'hub-interface' has been created (1 face).
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#c0000000 #7fff #8000 ]', ), )
p.Surface(side1Faces=side1Faces, name='perimeter-washers')
#: The surface 'perimeter-washers' has been created (18 faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.603891, 
    farPlane=1.01141, cameraPosition=(0.801652, 0.0970369, -0.00293269), 
    cameraUpVector=(-0.120856, 0.955812, -0.267987), cameraTarget=(
    -1.21072e-08, -1.5134e-09, 0.0125))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.617816, 
    farPlane=0.997486, cameraPosition=(0.545993, 0.226867, 0.562702), 
    cameraUpVector=(-0.394822, 0.918666, 0.0130046), cameraTarget=(2.02563e-07, 
    -1.08499e-07, 0.0124995))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#0 #80000 ]', ), )
p.Surface(side1Faces=side1Faces, name='perimeter-interface')
#: The surface 'perimeter-interface' has been created (1 face).
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.72777, 
    farPlane=0.88753, cameraPosition=(-0.0848824, -0.0426875, 0.814542), 
    cameraUpVector=(-0.0379143, 0.998074, 0.0491087), cameraTarget=(4.5076e-07, 
    -2.49711e-08, 0.0124995))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.671201, 
    farPlane=0.9441, cameraPosition=(0.300893, 0.153297, 0.746164), 
    cameraUpVector=(-0.17071, 0.976173, -0.133957), cameraTarget=(1.59256e-07, 
    -1.73459e-07, 0.0124996))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.612199, 
    farPlane=1.0031, cameraPosition=(0.523812, 0.281191, 0.559174), 
    cameraUpVector=(-0.251453, 0.937334, -0.241196), cameraTarget=(6.00703e-08, 
    -2.30502e-07, 0.0124997))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.520001, 
    0.286992, 0.559842), cameraTarget=(-0.0038106, 0.00580046, 0.0131673))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.612246, 
    farPlane=1.00306, width=0.491219, height=0.298938)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.652647, 
    farPlane=0.961285, cameraPosition=(0.438971, 0.124789, 0.678063), 
    cameraUpVector=(-0.118287, 0.988126, -0.0980602), cameraTarget=(
    -0.00381057, 0.00580052, 0.0131673))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.67403, 
    farPlane=0.939902, width=0.252195, height=0.153477, cameraPosition=(
    0.400046, 0.166358, 0.696546), cameraTarget=(-0.0427355, 0.0473697, 
    0.0316499))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.6745, 
    farPlane=0.939432, cameraPosition=(0.404231, 0.0533924, 0.713975), 
    cameraTarget=(-0.0385509, -0.0655961, 0.0490793))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.6745, 
    farPlane=0.939432, cameraPosition=(0.42432, 0.0293336, 0.704902), 
    cameraTarget=(-0.0184616, -0.0896549, 0.0400065))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.489419, 
    0.0783877, 0.652771), cameraTarget=(0.0466378, -0.0406008, -0.0121246))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.472525, 
    0.179397, 0.645945), cameraTarget=(0.0297435, 0.0604086, -0.0189504))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.660861, 
    farPlane=0.953069, width=0.409553, height=0.249239, cameraPosition=(
    0.492849, 0.210225, 0.626893), cameraTarget=(0.0500676, 0.0912364, 
    -0.038002))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#5ffff00 #fe800000 #3ff ]', ), )
p.Surface(side1Faces=side1Faces, name='perimeter-holes')
#: The surface 'perimeter-holes' has been created (36 faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.640301, 
    farPlane=0.97363, width=0.613719, height=0.373488, cameraPosition=(
    0.513128, 0.158489, 0.622647), cameraTarget=(0.070347, 0.039501, 
    -0.0422484))
mdb.save()
#: The model database has been saved to "/home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Abaqus Files/2nd_attempt.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.666583, 
    farPlane=0.86224, cameraPosition=(0.20944, 0.0117682, 0.752781), 
    cameraUpVector=(0.0161036, 0.999352, 0.0322007), cameraTarget=(0.0706049, 
    0.0396256, -0.0423589))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
#: 
#: Point 1: 0., 0., 25.E-03  Point 2: 0., 37.25E-03, 25.E-03
#:    Distance: 37.25E-03  Components: 0., 37.25E-03, 0.
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='aluminium')
mdb.models['Model-1'].materials['aluminium'].Elastic(table=((70000000000.0, 
    0.33), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='solid-aluminium', 
    material='aluminium', thickness=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.736689, 
    farPlane=0.878613, width=0.652474, height=0.397072, cameraPosition=(
    0.0465897, 0.0253725, 0.820151), cameraTarget=(0.0465897, 0.0253725, 
    0.0125))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
p.SectionAssignment(region=region, sectionName='solid-aluminium', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.6586, 
    farPlane=1.02566, cameraPosition=(0.665095, -0.0127824, 0.530473), 
    cameraUpVector=(0.11651, 0.990986, -0.0661248), cameraTarget=(0.0465897, 
    0.0253725, 0.0125))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.650093, 
    farPlane=1.0602, cameraPosition=(0.813638, 0.0683116, 0.269512), 
    cameraUpVector=(-0.0496801, 0.998743, -0.00658933), cameraTarget=(
    0.0526716, 0.0286928, 0.00181526))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
a.Instance(name='Wheel Centre Blank2-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.623325, 
    farPlane=1.04525, width=0.437008, height=0.265947, viewOffsetX=0.0100455, 
    viewOffsetY=-0.0183275)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    interactions=OFF, constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON, seeds=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.556874, 
    farPlane=1.05843, cameraPosition=(0.699952, 0.39199, -0.0808318), 
    cameraUpVector=(-0.746774, 0.56199, -0.355661), cameraTarget=(-7.45058e-09, 
    7.91624e-09, 0.0125))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.618886, 
    farPlane=0.996416, cameraPosition=(0.583385, 0.11738, -0.533562), 
    cameraUpVector=(-0.759083, 0.624537, -0.183701), cameraTarget=(1.02445e-08, 
    5.68107e-08, 0.0125001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.586689, 
    farPlane=1.02861, cameraPosition=(0.293265, 0.597785, -0.44461), 
    cameraUpVector=(-0.944145, 0.208166, 0.255456), cameraTarget=(-1.90921e-08, 
    1.19209e-07, 0.0125001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.559513, 
    farPlane=1.05579, cameraPosition=(0.407626, 0.657101, 0.245652), 
    cameraUpVector=(-0.982061, 0.172414, 0.0763539), cameraTarget=(
    -9.31323e-10, 1.37836e-07, 0.0125002))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.591565, 
    farPlane=1.02374, cameraPosition=(0.425356, 0.431296, 0.546688), 
    cameraUpVector=(-0.933251, 0.355968, -0.048264), cameraTarget=(4.88944e-09, 
    1.40164e-07, 0.0125002))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.614772, 
    farPlane=1.00053, cameraPosition=(-0.0882786, 0.641349, -0.470387), 
    cameraUpVector=(-0.896643, -0.293793, 0.331236), cameraTarget=(
    -1.54134e-07, 1.84402e-07, 0.0124999))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.615738, 
    farPlane=0.999566, cameraPosition=(-0.15898, 0.558273, -0.549068), 
    cameraUpVector=(-0.856349, -0.312769, 0.410904), cameraTarget=(
    -1.94006e-07, 1.39349e-07, 0.0124999))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.587261, 
    farPlane=1.02804, cameraPosition=(-0.329053, 0.55639, -0.471707), 
    cameraUpVector=(-0.715454, -0.423227, 0.555881), cameraTarget=(
    -2.20258e-07, 1.40251e-07, 0.0124999))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.616044, 
    farPlane=0.99926, cameraPosition=(-0.0854116, 0.636393, -0.477409), 
    cameraUpVector=(-0.896664, -0.278383, 0.344234), cameraTarget=(
    -1.65543e-07, 1.62923e-07, 0.0124999))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
v, e, d = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(point3=v[94], cells=pickedCells, 
    point1=p.InterestingPoint(edge=e[0], rule=CENTER), 
    point2=p.InterestingPoint(edge=e[2], rule=CENTER))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#3 ]', ), )
p.setMeshControls(regions=pickedRegions, technique=SWEEP, 
    algorithm=ADVANCING_FRONT)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
p.seedPart(size=0.016, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
p.seedPart(size=0.005, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
p.seedPart(size=0.005, deviationFactor=0.02, minSizeFactor=0.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.587654, 
    farPlane=1.02765, width=0.53697, height=0.327613, cameraPosition=(0.479851, 
    0.458855, 0.472687), cameraTarget=(0.0135532, -0.00744249, 0.0063894))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.666763, 
    farPlane=0.924895, cameraPosition=(-0.357106, 0.0115229, 0.723713), 
    cameraUpVector=(-0.109143, 0.883741, -0.45507), cameraTarget=(0.013553, 
    -0.00744256, 0.00638943))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.595651, 
    farPlane=0.982908, cameraPosition=(-0.744361, 0.0242828, 0.274021), 
    cameraUpVector=(0.272915, 0.898842, -0.342928), cameraTarget=(0.0193055, 
    -0.00763211, 0.0130695))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.607777, 
    farPlane=0.970783, width=0.39659, height=0.241965, cameraPosition=(
    -0.748376, 0.024294, 0.26227), cameraTarget=(0.0152907, -0.00762089, 
    0.00131886))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.6037, 
    farPlane=0.960975, cameraPosition=(0.519395, 0.211405, 0.558046), 
    cameraUpVector=(-0.567175, 0.784255, -0.251508), cameraTarget=(-0.0142188, 
    -0.0119762, -0.00556577))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.591797, 
    farPlane=0.972878, width=0.537194, height=0.327749, cameraPosition=(
    0.521275, 0.226102, 0.550441), cameraTarget=(-0.0123389, 0.00272083, 
    -0.0131706))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.543979, 
    farPlane=1.03489, cameraPosition=(0.543756, 0.527367, 0.235096), 
    cameraUpVector=(-0.74148, 0.478402, -0.470466), cameraTarget=(-0.0130663, 
    -0.00702705, -0.00296707))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.55583, 
    farPlane=1.03701, cameraPosition=(0.471709, 0.567452, -0.287248), 
    cameraUpVector=(-0.953734, 0.287367, -0.0883843), cameraTarget=(-0.0114038, 
    -0.00795204, 0.00908638))
session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=WIREFRAME)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.596815, 
    farPlane=1.00051, cameraPosition=(0.488604, 0.31215, -0.536832), 
    cameraUpVector=(-0.799993, 0.591242, 0.102199), cameraTarget=(-0.0116421, 
    -0.00435074, 0.012607))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.5978, 
    farPlane=0.999527, width=0.537194, height=0.327749, cameraPosition=(
    0.488604, 0.31215, -0.536832), cameraTarget=(-0.0116421, -0.00435075, 
    0.012607))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#0:3 #a0000 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=4, constraint=FINER)
session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=SHADED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.542575, 
    farPlane=1.04445, cameraPosition=(0.575101, 0.546562, 0.0279761), 
    cameraUpVector=(-0.884821, 0.456709, -0.0922483), cameraTarget=(-0.0126156, 
    -0.00698892, 0.00625039))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.654906, 
    farPlane=0.921193, cameraPosition=(0.211566, 0.191066, 0.747193), 
    cameraUpVector=(-0.174922, 0.836439, -0.519396), cameraTarget=(-0.00613836, 
    -0.000654901, -0.00656419))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.661346, 
    farPlane=0.914754, width=0.476466, height=0.290698, cameraPosition=(0.1702, 
    0.235703, 0.747787), cameraTarget=(-0.0475046, 0.0439818, -0.00597007))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.637365, 
    farPlane=0.938734, width=0.743429, height=0.453576, cameraPosition=(
    0.159107, 0.245336, 0.748541), cameraTarget=(-0.0585976, 0.053615, 
    -0.00521639))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.626637, 
    farPlane=0.988665, cameraPosition=(0.742814, -0.000501095, 0.329559), 
    cameraUpVector=(0.00281696, 0.999983, -0.00501921), cameraTarget=(
    1.11759e-08, -7.27596e-12, 0.0125))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.656795, 
    farPlane=0.958506, width=0.158228, height=0.0965373, cameraPosition=(
    0.755336, -0.000314436, 0.300223), cameraTarget=(0.0125216, 0.000186659, 
    -0.0168356))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.652427, 
    farPlane=0.994524, cameraPosition=(0.810523, 0.0811465, -0.111379), 
    cameraUpVector=(-0.094125, 0.993946, 0.0566707), cameraTarget=(0.0125216, 
    0.000186658, -0.0168356))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.620997, 
    farPlane=1.02595, width=0.511346, height=0.311979, cameraPosition=(
    0.799984, 0.103483, -0.181203), cameraTarget=(0.00198306, 0.0225229, 
    -0.08666))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.589316, 
    farPlane=0.980823, cameraPosition=(0.776947, 0.070974, 0.140048), 
    cameraUpVector=(-0.0523861, 0.997908, -0.0378741), cameraTarget=(
    0.00154036, 0.0218982, -0.0804865))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.622519, 
    farPlane=0.94762, width=0.146128, height=0.0891545, cameraPosition=(
    0.756724, 0.0561917, 0.214442), cameraTarget=(-0.0186825, 0.00711592, 
    -0.0060929))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.645021, 
    farPlane=0.914152, cameraPosition=(0.617921, -0.00134663, 0.488034), 
    cameraUpVector=(0.036289, 0.999013, -0.0255962), cameraTarget=(-0.01469, 
    0.00877091, -0.0139623))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.623755, 
    farPlane=0.935418, width=0.385855, height=0.235415, cameraPosition=(
    0.647788, 0.0197958, 0.450822), cameraTarget=(0.0151769, 0.0299134, 
    -0.0511742))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.605006, 
    farPlane=0.8361, cameraPosition=(-0.311142, 0.000345312, 0.66311), 
    cameraUpVector=(0.389172, 0.891498, 0.231897), cameraTarget=(0.0496968, 
    0.0306136, -0.0588163))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#b ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#0:3 #a00 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=10, constraint=FINER)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.569551, 
    farPlane=0.871043, cameraPosition=(-0.47035, 0.0828272, 0.552542), 
    cameraUpVector=(0.42513, 0.855919, 0.294393), cameraTarget=(0.0689412, 
    0.0206435, -0.0454513))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.565683, 
    farPlane=0.888445, cameraPosition=(-0.38501, 0.218641, 0.589949), 
    cameraUpVector=(0.500421, 0.863879, 0.0573711), cameraTarget=(0.0585918, 
    0.00417299, -0.0499877))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.549879, 
    farPlane=0.942975, cameraPosition=(0.60331, 0.22596, 0.390122), 
    cameraUpVector=(-0.0589659, 0.916451, -0.395779), cameraTarget=(-0.0509501, 
    0.0033618, -0.0278396))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.605959, 
    farPlane=0.899871, cameraPosition=(0.498479, 0.0563844, -0.549341), 
    cameraUpVector=(-0.278725, 0.941321, -0.190333), cameraTarget=(-0.0423517, 
    0.0172706, 0.0492164))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.660924, 
    farPlane=0.85246, cameraPosition=(0.190848, 0.0789594, -0.715755), 
    cameraUpVector=(-0.171609, 0.984589, 0.0336801), cameraTarget=(-0.0199879, 
    0.0156295, 0.0613141))
mdb.save()
#: The model database has been saved to "/home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Abaqus Files/2nd_attempt.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.626031, 
    farPlane=0.872482, cameraPosition=(0.161542, -0.217398, -0.686358), 
    cameraUpVector=(-0.0425961, 0.94296, -0.330169), cameraTarget=(-0.0180143, 
    0.0355872, 0.0593344))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.572275, 
    farPlane=0.909059, cameraPosition=(0.104893, -0.528199, -0.496313), 
    cameraUpVector=(-0.00260098, 0.67668, -0.736273), cameraTarget=(-0.0135994, 
    0.0598096, 0.0445232))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.651301, 
    farPlane=0.861571, cameraPosition=(0.0303445, 0.279055, -0.689963), 
    cameraUpVector=(-0.187942, 0.91858, 0.347691), cameraTarget=(-0.00685747, 
    -0.013196, 0.0620363))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.62162, 
    farPlane=0.887747, cameraPosition=(0.250705, 0.208873, -0.668026), 
    cameraUpVector=(-0.148428, 0.961498, 0.23128), cameraTarget=(-0.0217768, 
    -0.00844435, 0.0605511))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.603826, 
    farPlane=0.900889, cameraPosition=(0.489405, 0.0619567, -0.555593), 
    cameraUpVector=(-0.131316, 0.991211, -0.0160548), cameraTarget=(-0.0385294, 
    0.00186664, 0.0526602))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.560426, 
    farPlane=0.940574, cameraPosition=(0.746964, 0.0728946, 0.0171222), 
    cameraUpVector=(-0.0889938, 0.996009, 0.00679784), cameraTarget=(
    -0.0574578, 0.0010628, 0.0105705))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.55962, 
    farPlane=0.943054, cameraPosition=(0.69801, 0.108714, -0.24345), 
    cameraUpVector=(-0.128887, 0.990616, 0.045468), cameraTarget=(-0.05373, 
    -0.00166478, 0.0304126))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.577898, 
    farPlane=0.924777, width=0.182721, height=0.111481, cameraPosition=(
    0.707183, 0.105434, -0.219593), cameraTarget=(-0.0445573, -0.00494444, 
    0.0542694))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#f ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#29400 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=50, constraint=FINER)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#29400 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=65, constraint=FINER)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.735322, 
    farPlane=0.87998, width=0.66604, height=0.40636, cameraPosition=(0.0105687, 
    -0.0194706, 0.820151), cameraTarget=(0.0105687, -0.0194706, 0.0125))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#f ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#21400 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=100, constraint=FINER)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#88 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=20, constraint=FINER)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.787683, 
    farPlane=0.827619, width=0.0798435, height=0.0487136, cameraPosition=(
    0.127027, -0.00558237, 0.820151), cameraTarget=(0.127027, -0.00558237, 
    0.0125))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.772891, 
    farPlane=0.943223, cameraPosition=(0.449869, 0.0480239, 0.750876), 
    cameraUpVector=(-0.0413672, 0.997665, -0.0543436), cameraTarget=(0.127027, 
    -0.00558237, 0.0125))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.770867, 
    farPlane=0.945246, width=0.103998, height=0.0634506, cameraPosition=(
    0.447085, 0.0473109, 0.752145), cameraTarget=(0.124243, -0.00629535, 
    0.0137692))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#4 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#0:3 #10000 #0 #4000000 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=90, constraint=FINER)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#0:3 #10000 #0 #4000000 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=100, constraint=FINER)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
p.generateMesh()
mdb.save()
#: The model database has been saved to "/home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Abaqus Files/2nd_attempt.cae".
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    interactions=ON, constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.652409, 
    farPlane=1.06158, width=0.457398, height=0.278356, cameraPosition=(
    0.842202, 0.144144, 0.0785737), cameraUpVector=(-0.455017, 0.835766, 
    -0.307334), cameraTarget=(0.0221508, 0.00591092, 0.0119047), 
    viewOffsetX=0.0105142, viewOffsetY=-0.0191826)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.723034, 
    farPlane=1.01717, width=0.506912, height=0.308489, cameraPosition=(
    0.455685, -0.123509, -0.7184), cameraUpVector=(-0.365528, 0.930763, 
    0.00828096), cameraTarget=(0.0230534, -0.000880156, -0.0156697), 
    viewOffsetX=0.0116524, viewOffsetY=-0.0212592)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.655417, 
    farPlane=1.06549, width=0.459507, height=0.27964, cameraPosition=(0.690887, 
    0.237765, -0.442067), cameraUpVector=(-0.602838, 0.788827, 0.119739), 
    cameraTarget=(0.024336, 0.0128371, 0.00643494), viewOffsetX=0.0105627, 
    viewOffsetY=-0.0192711)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.629749, 
    farPlane=1.08262, width=0.441512, height=0.268688, cameraPosition=(
    0.688648, 0.396209, -0.306848), cameraUpVector=(-0.706615, 0.67858, 
    0.200561), cameraTarget=(0.0201216, 0.0147522, 0.0150224), 
    viewOffsetX=0.010149, viewOffsetY=-0.0185164)
mdb.save()
#: The model database has been saved to "/home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Abaqus Files/2nd_attempt.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF, seeds=OFF)
p1 = mdb.models['Model-1'].parts['Wheel Centre Blank2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].Calibration(name='Calibration-1')
del mdb.models['Model-1'].calibrations['Calibration-1']
mdb.models['Model-1'].materials['aluminium'].Density(table=((2700.0, ), ))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.611013, 
    farPlane=1.00429, cameraPosition=(0.707733, 0.119463, 0.382828), 
    cameraUpVector=(-0.0403344, 0.970888, -0.236113), cameraTarget=(
    1.11759e-08, 1.86265e-09, 0.0125))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.573269, 
    farPlane=1.04203, cameraPosition=(0.624375, 0.424002, 0.300038), 
    cameraUpVector=(-0.393968, 0.837274, -0.379159), cameraTarget=(1.40572e-08, 
    -1.32713e-08, 0.0125))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
e1 = p.edges
p.DatumPointByOffset(point=p.InterestingPoint(edge=e1[10], rule=CENTER), 
    vector=(0.0, 0.0, -100.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.523249, 
    farPlane=36.6849, width=1.06003, height=0.645096, cameraPosition=(0.666129, 
    0.433025, 0.196066), cameraTarget=(0.0417536, 0.00902316, -0.0914715))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.341, 
    farPlane=34.682, cameraPosition=(30.1076, 12.1297, -14.6414), 
    cameraUpVector=(-0.464369, 0.832474, -0.302237), cameraTarget=(2.04453, 
    -1.61468, -9.38143))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.4485, 
    farPlane=34.6709, width=1.37841, height=0.838852, cameraPosition=(30.0978, 
    12.1372, -14.6739), cameraTarget=(2.03477, -1.60719, -9.41393))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=163.438, 
    farPlane=236.565, width=84.0531, height=51.1517, cameraPosition=(117.61, 
    117.582, 61.2463), cameraTarget=(2.13891, 2.11076, -54.2247))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
del p.features['Datum pt-1']
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['Wheel Centre Blank2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].parts['Wheel Centre Blank2'].setValues(space=THREE_D, 
    type=DEFORMABLE_BODY)
p1 = mdb.models['Model-1'].parts['Wheel Centre Blank2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
#: 
#: Point 1: -142.5E-03, 0., 25.E-03  Point 2: 142.5E-03, 0., 25.E-03
#:    Distance: 285.E-03  Components: 285.E-03, 0., 0.
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
e = p.edges
p.DatumPointByOffset(point=p.InterestingPoint(edge=e[10], rule=CENTER), 
    vector=(0.0, 0.0, -0.1))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.585147, 
    farPlane=1.02773, cameraPosition=(0.527088, -0.222643, -0.593654), 
    cameraUpVector=(-0.108002, 0.994028, 0.0156139), cameraTarget=(0.00158707, 
    -0.0179862, -0.0154985))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.599448, 
    farPlane=1.00776, cameraPosition=(0.552978, -0.0974698, -0.600242), 
    cameraUpVector=(-0.19995, 0.969703, 0.140342), cameraTarget=(0.00154818, 
    -0.0181742, -0.0154886))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.603608, 
    farPlane=1.00211, cameraPosition=(0.629133, -0.020497, -0.523762), 
    cameraUpVector=(-0.30944, 0.93997, 0.143889), cameraTarget=(0.00116484, 
    -0.0185617, -0.0158736))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.566026, 
    farPlane=1.03554, cameraPosition=(0.722676, 0.156803, -0.332907), 
    cameraUpVector=(-0.501825, 0.846475, 0.177911), cameraTarget=(0.000606875, 
    -0.0196193, -0.017012))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
e1, d1 = p.edges, p.datums
p.DatumPointByOffset(point=d1[33], vector=(0.0, -0.27, 0.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.52683, 
    farPlane=1.10259, width=1.09225, height=0.664704, cameraPosition=(0.717502, 
    0.203744, -0.318517), cameraTarget=(-0.0045667, 0.0273221, -0.00262169))
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Wheel Centre Blank2-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#0:3 #2 ]', ), )
region1=regionToolset.Region(vertices=verts1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Wheel Centre Blank2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0 #4 ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].Coupling(name='Constraint-1', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
del mdb.models['Model-1'].constraints['Constraint-1']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.594453, 
    farPlane=1.14728, width=0.541943, height=0.329807, viewOffsetX=0.0142659, 
    viewOffsetY=-0.0141359)
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.835386, 
    farPlane=1.20963, width=0.611365, height=0.372055, cameraPosition=(
    0.270601, 0.1245, -0.992917), cameraUpVector=(0.00906493, 0.981089, 
    0.193346))
a = mdb.models['Model-1'].rootAssembly
d1 = a.instances['Wheel Centre Blank2-1'].datums
a.ReferencePoint(point=d1[33])
a = mdb.models['Model-1'].rootAssembly
d21 = a.instances['Wheel Centre Blank2-1'].datums
a.ReferencePoint(point=d21[34])
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
d = p.datums
p.DatumPointByOffset(point=d[33], vector=(0.27, 0.0, 0.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.459913, 
    farPlane=1.03065, cameraPosition=(0.544394, 0.078685, -0.586209), 
    cameraUpVector=(-0.202214, 0.920977, 0.333033), cameraTarget=(0.00684197, 
    0.0355641, 0.0150205))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.580654, 
    farPlane=0.92926, cameraPosition=(-0.0285033, 0.0513431, -0.772612), 
    cameraUpVector=(0.206839, 0.92133, 0.329195), cameraTarget=(0.0547827, 
    0.0378521, 0.0306189))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.496741, 
    farPlane=0.988248, cameraPosition=(-0.208546, -0.0673108, -0.723359), 
    cameraUpVector=(0.155889, 0.975709, 0.153914), cameraTarget=(0.0673489, 
    0.0461336, 0.0271813))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.542942, 
    farPlane=1.00308, cameraPosition=(-0.114828, 0.173162, -0.745532), 
    cameraUpVector=(0.242671, 0.855884, 0.456699), cameraTarget=(0.059125, 
    0.0250316, 0.029127))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.521528, 
    farPlane=0.99969, cameraPosition=(0.307223, 0.122122, -0.727978), 
    cameraUpVector=(-0.113466, 0.896497, 0.428274), cameraTarget=(0.0402141, 
    0.0273185, 0.0283405))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
d1 = p.datums
p.DatumPointByOffset(point=d1[33], vector=(0.19092, -0.19092, 0.0))
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.926175, 
    farPlane=1.44131, cameraPosition=(0.782602, -0.2251, -0.951536), 
    cameraUpVector=(0.129655, 0.988969, -0.0716293), cameraTarget=(0.0637499, 
    -0.06375, -0.025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.886505, 
    farPlane=1.48098, cameraPosition=(0.924882, 0.223436, -0.784755), 
    cameraUpVector=(-0.162011, 0.969688, 0.182912), cameraTarget=(0.0637499, 
    -0.06375, -0.025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.979866, 
    farPlane=1.38762, cameraPosition=(0.370239, -0.281832, -1.14739), 
    cameraUpVector=(-0.222876, 0.943757, -0.244233), cameraTarget=(0.0637498, 
    -0.06375, -0.025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.01623, 
    farPlane=1.35126, cameraPosition=(-0.151914, -0.154732, -1.18537), 
    cameraUpVector=(-0.204226, 0.978157, -0.0387374), cameraTarget=(0.0637499, 
    -0.06375, -0.025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.03333, 
    farPlane=1.33415, cameraPosition=(0.0463492, 0.12539, -1.19341), 
    cameraUpVector=(-0.0334257, 0.986519, 0.160195), cameraTarget=(0.0637499, 
    -0.06375, -0.025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.98121, 
    farPlane=1.38629, cameraPosition=(0.465239, -0.182821, -1.1322), 
    cameraUpVector=(0.0521069, 0.994749, -0.0880817), cameraTarget=(0.06375, 
    -0.06375, -0.025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.866161, 
    farPlane=1.50134, cameraPosition=(1.07222, -0.37455, -0.561326), 
    cameraUpVector=(0.249879, 0.964189, -0.0888864), cameraTarget=(0.0637499, 
    -0.06375, -0.0250001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.851474, 
    farPlane=1.51602, cameraPosition=(1.14236, -0.444961, -0.329177), 
    cameraUpVector=(0.294419, 0.945271, -0.140643), cameraTarget=(0.0637499, 
    -0.06375, -0.0250001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.89775, 
    farPlane=1.46973, cameraPosition=(1.21317, -0.0127012, -0.303343), 
    cameraUpVector=(-0.0411103, 0.999064, 0.0134803))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.901427, 
    farPlane=1.46606, cameraPosition=(1.22757, -0.0948966, -0.238987), 
    cameraUpVector=(0.0232096, 0.999546, -0.019237), cameraTarget=(0.0637499, 
    -0.06375, -0.0250001))
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF, 
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='torque-0', previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-0')
mdb.models['Model-1'].StaticStep(name='torque-45', previous='torque-0')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-45')
mdb.models['Model-1'].StaticStep(name='torque-90', previous='torque-45')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-90')
mdb.models['Model-1'].StaticStep(name='pos-axial-90', previous='torque-90')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='pos-axial-90')
mdb.models['Model-1'].StaticStep(name='pos-axial-45', previous='pos-axial-90')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='pos-axial-45')
mdb.models['Model-1'].StaticStep(name='pos-axial-0', previous='pos-axial-45')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='pos-axial-0')
mdb.models['Model-1'].StaticStep(name='neg-axial-0', previous='pos-axial-0')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='neg-axial-0')
mdb.models['Model-1'].StaticStep(name='neg-axial-45', previous='neg-axial-0')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='neg-axial-45')
mdb.models['Model-1'].StaticStep(name='neg-axial-90', previous='neg-axial-45')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='neg-axial-90')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
d1 = a.instances['Wheel Centre Blank2-1'].datums
a.ReferencePoint(point=d1[36])
a = mdb.models['Model-1'].rootAssembly
d21 = a.instances['Wheel Centre Blank2-1'].datums
a.ReferencePoint(point=d21[35])
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
a.ReferencePoint(point=r1[7])
a = mdb.models['Model-1'].rootAssembly
r11 = a.referencePoints
a.ReferencePoint(point=r11[8])
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
a.ReferencePoint(point=r1[9])
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('RP-7', 'RP-5', 'RP-6', ))
a = mdb.models['Model-1'].rootAssembly
del a.features['RP-1']
mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='RP-2', 
    toName='RP-1')
mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='RP-3', 
    toName='RP-2')
mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='RP-4', 
    toName='RP-3')
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.667088, 
    farPlane=1.25502, width=0.488199, height=0.2971, cameraPosition=(0.876554, 
    -0.244775, -0.506658), cameraUpVector=(0.292541, 0.939876, 0.176217), 
    cameraTarget=(-0.0101658, -0.0575549, -0.0331577))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.616193, 
    farPlane=1.28151, width=0.450952, height=0.274433, cameraPosition=(
    0.852672, -0.582699, -0.126266), cameraUpVector=(0.537941, 0.826662, 
    0.165072), cameraTarget=(-0.00863859, -0.0359457, -0.0574826))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.68066, 
    farPlane=1.19515, width=0.498132, height=0.303145, cameraPosition=(1.00122, 
    -0.0310737, -0.0605561), cameraUpVector=(-0.0465811, 0.998606, -0.0248233), 
    cameraTarget=(-0.0201706, -0.078768, -0.0625836))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.660157, 
    farPlane=1.20963, width=0.483127, height=0.294014, cameraPosition=(
    0.995116, 0.0230343, -0.00124056), cameraUpVector=(-0.103396, 0.994484, 
    -0.0176165), cameraTarget=(-0.0196199, -0.0836488, -0.0679342))
mdb.save()
#: The model database has been saved to "/home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Abaqus Files/2nd_attempt.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.708219, 
    farPlane=1.20772, width=0.518301, height=0.315419, cameraPosition=(
    0.849192, -0.0489503, -0.574136), cameraUpVector=(-0.204133, 0.94247, 
    -0.264726), cameraTarget=(-0.00594475, -0.0769028, -0.0142456))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.737867, 
    farPlane=1.20882, width=0.539999, height=0.328624, cameraPosition=(
    0.521677, -0.280462, -0.856556), cameraUpVector=(-0.119033, 0.943296, 
    -0.309876), cameraTarget=(0.0161188, -0.0613067, 0.00478001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.775491, 
    farPlane=1.17236, width=0.567534, height=0.345381, cameraPosition=(0.42255, 
    0.0347106, -0.925467), cameraUpVector=(-0.275597, 0.961268, -0.00324753), 
    cameraTarget=(0.0211254, -0.0772249, 0.00826044))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.655353, 
    farPlane=1.27418, width=0.479613, height=0.291875, cameraPosition=(
    0.481156, 0.559511, -0.632254), cameraUpVector=(-0.443083, 0.759343, 
    0.476525), cameraTarget=(0.018202, -0.103403, -0.00636574))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Wheel Centre Blank2-1'].edges
a.ReferencePoint(point=a.instances['Wheel Centre Blank2-1'].InterestingPoint(
    edge=e1[13], rule=CENTER))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.728838, 
    farPlane=1.20266, width=0.533392, height=0.324603, cameraPosition=(
    0.630484, 0.0654873, -0.796649), cameraUpVector=(-0.164675, 0.985378, 
    0.0437289), cameraTarget=(0.00926545, -0.0738381, 0.0034725))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.831025, 
    farPlane=1.13234, width=0.608177, height=0.370114, cameraPosition=(
    0.0473412, -0.314759, -0.974123), cameraUpVector=(-0.331029, 0.911488, 
    -0.244149), cameraTarget=(0.0435363, -0.0514913, 0.0139025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.816838, 
    farPlane=1.13701, width=0.597795, height=0.363796, cameraPosition=(
    0.301241, -0.0743811, -0.972758), cameraUpVector=(-0.26768, 0.959722, 
    -0.0853268), cameraTarget=(0.0329782, -0.0614871, 0.0138457))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.741633, 
    farPlane=1.20597, width=0.542757, height=0.330303, cameraPosition=(
    0.460495, 0.15528, -0.887138), cameraUpVector=(-0.227781, 0.964429, 
    0.134136), cameraTarget=(0.0255474, -0.0722032, 0.00985068))
a = mdb.models['Model-1'].rootAssembly
r11 = a.referencePoints
a.ReferencePoint(point=r11[13])
a = mdb.models['Model-1'].rootAssembly
del a.features['RP-5']
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[13], )
region1=regionToolset.Region(referencePoints=refPoints1)
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['Wheel Centre Blank2-1'].surfaces['centre-hole']
mdb.models['Model-1'].Coupling(name='RP-4-centre-hole', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.842113, 
    farPlane=1.1264, width=0.616294, height=0.375054, cameraPosition=(
    -0.0946244, -0.000145848, -0.994483), cameraUpVector=(-0.391285, 0.912998, 
    0.115456), cameraTarget=(0.0533112, -0.0644297, 0.0152194))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.762653, 
    farPlane=1.18731, width=0.558142, height=0.339665, cameraPosition=(
    0.472326, -0.170227, -0.90392), cameraUpVector=(-0.0715526, 0.985254, 
    -0.155421), cameraTarget=(0.0312795, -0.0578203, 0.0117001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.744786, 
    farPlane=1.20278, width=0.545066, height=0.331708, cameraPosition=(0.55911, 
    0.0701292, -0.852725), cameraUpVector=(-0.0834171, 0.990534, 0.109012), 
    cameraTarget=(0.0270496, -0.0695354, 0.00920481))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[7], )
region1=regionToolset.Region(referencePoints=refPoints1)
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['Wheel Centre Blank2-1'].surfaces['perimeter-holes']
mdb.models['Model-1'].Coupling(name='RP1-perimeter', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[8], )
region1=regionToolset.Region(referencePoints=refPoints1)
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['Wheel Centre Blank2-1'].surfaces['perimeter-holes']
mdb.models['Model-1'].Coupling(name='RP2-perimeter', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[9], )
region1=regionToolset.Region(referencePoints=refPoints1)
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['Wheel Centre Blank2-1'].surfaces['perimeter-holes']
mdb.models['Model-1'].Coupling(name='RP3-perimeter', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.628453, 
    farPlane=1.30588, width=0.459929, height=0.279896, cameraPosition=(0.82685, 
    0.459383, -0.307052), cameraUpVector=(-0.338918, 0.779862, 0.52626), 
    cameraTarget=(0.013654, -0.0890106, -0.0180964))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.693938, 
    farPlane=1.23401, width=0.507854, height=0.309062, cameraPosition=(
    0.987276, 0.0155693, -0.289907), cameraUpVector=(0.0469118, 0.899989, 
    0.43338), cameraTarget=(0.00447462, -0.0636162, -0.0190774))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.684829, 
    farPlane=1.23072, width=0.501188, height=0.305005, cameraPosition=(
    0.937438, 0.0293197, 0.35634), cameraUpVector=(-0.258478, 0.888689, 
    0.378709), cameraTarget=(0.00750073, -0.0644511, -0.0583172))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.755826, 
    farPlane=1.15015, width=0.553147, height=0.336625, cameraPosition=(0.43454, 
    0.0637018, 0.843631), cameraUpVector=(-0.288513, 0.957397, -0.0123213), 
    cameraTarget=(0.0414898, -0.0667749, -0.0912513))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.655055, 
    farPlane=1.25873, width=0.479398, height=0.291744, cameraPosition=(
    0.839989, 0.2144, 0.460568), cameraUpVector=(-0.303056, 0.951571, 
    -0.0516654), cameraTarget=(0.0119139, -0.0777677, -0.0633084))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.777437, 
    farPlane=1.14619, width=0.568962, height=0.34625, cameraPosition=(0.480106, 
    -0.0329377, -0.891488), cameraUpVector=(-0.0979292, 0.995047, -0.0170481), 
    cameraTarget=(0.0365902, -0.0608083, 0.029399))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.721458, 
    farPlane=1.20494, width=0.527994, height=0.321318, cameraPosition=(
    0.438098, 0.251791, -0.854499), cameraUpVector=(-0.0996895, 0.94566, 
    0.309499), cameraTarget=(0.039241, -0.0787756, 0.0270649))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.720612, 
    farPlane=1.20579, width=0.58343, height=0.355055, viewOffsetX=-0.00435987, 
    viewOffsetY=0.00405096)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
mdb.save()
#: The model database has been saved to "/home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Abaqus Files/2nd_attempt.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-0')
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Wheel Centre Blank2-1'].sets['hub-holes']
mdb.models['Model-1'].DisplacementBC(name='hub-holes', 
    createStepName='torque-0', region=region, u1=0.0, u2=0.0, u3=UNSET, 
    ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Wheel Centre Blank2-1'].sets['hub-washers']
mdb.models['Model-1'].DisplacementBC(name='hub-washers', 
    createStepName='torque-0', region=region, u1=UNSET, u2=UNSET, u3=0.0, 
    ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.662723, 
    farPlane=1.26557, width=0.536562, height=0.326532, cameraPosition=(1.00345, 
    -0.25213, -0.130542), cameraUpVector=(0.227259, 0.775397, 0.589164), 
    cameraTarget=(0.00844774, -0.0432879, -0.021592), viewOffsetX=-0.00400964, 
    viewOffsetY=0.00372554)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.699621, 
    farPlane=1.23586, width=0.566436, height=0.344713, cameraPosition=(
    0.773597, -0.223135, 0.613188), cameraUpVector=(0.0116324, 0.971394, 
    0.237188), cameraTarget=(0.0275965, -0.0488432, -0.0640264), 
    viewOffsetX=-0.00423288, viewOffsetY=0.00393297)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.685329, 
    farPlane=1.26188, width=0.554866, height=0.337671, cameraPosition=(
    0.619146, 0.334292, 0.668565), cameraUpVector=(-0.273423, 0.913503, 
    -0.301252), cameraTarget=(0.0385486, -0.080926, -0.0635644), 
    viewOffsetX=-0.00414641, viewOffsetY=0.00385263)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Wheel Centre Blank2-1'].sets['hub-interface']
mdb.models['Model-1'].DisplacementBC(name='hub-interface', 
    createStepName='torque-0', region=region, u1=UNSET, u2=UNSET, u3=0.0, 
    ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.779261, 
    farPlane=1.17037, width=0.630916, height=0.383953, cameraPosition=(
    -0.163734, 0.170034, 0.893626), cameraUpVector=(0.0327719, 0.971021, 
    -0.236738), cameraTarget=(0.0773125, -0.0730058, -0.0698784), 
    viewOffsetX=-0.00471472, viewOffsetY=0.00438068)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.815513, 
    farPlane=1.13216, width=0.660267, height=0.401815, cameraPosition=(
    0.0100155, 0.128516, 0.928162), cameraUpVector=(0.0388044, 0.980343, 
    -0.193448), cameraTarget=(0.0689412, -0.0713487, -0.0728846), 
    viewOffsetX=-0.00493405, viewOffsetY=0.00458447)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[7], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].ConcentratedForce(name='Force-0', 
    createStepName='torque-0', region=region, cf2=1500.0, 
    distributionType=UNIFORM, field='', localCsys=None)
mdb.models['Model-1'].loads['Force-0'].setValues(cf1=2165.0, 
    distributionType=UNIFORM, field='')
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.912281, 
    farPlane=1.4552, cameraPosition=(0.89728, 0.0867735, -0.851927), 
    cameraUpVector=(-0.0932125, 0.991873, 0.0865966), cameraTarget=(0.0637499, 
    -0.06375, -0.025))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
v1, e2, d = p.vertices, p.edges, p.datums
p.DatumCsysByThreePoints(point1=d[35], point2=v1[96], name='Cyl-coordinates', 
    coordSysType=CYLINDRICAL, origin=p.InterestingPoint(edge=e2[13], 
    rule=CENTER))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.828358, 
    farPlane=1.53912, cameraPosition=(0.720248, 0.869673, -0.339595), 
    cameraUpVector=(-0.593464, 0.598693, 0.537929), cameraTarget=(0.0637499, 
    -0.06375, -0.025))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
del p.features['Cyl-coordinates']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.872245, 
    farPlane=1.49523, cameraPosition=(0.904387, 0.332131, -0.75838), 
    cameraUpVector=(-0.307368, 0.938958, 0.154538), cameraTarget=(0.0637499, 
    -0.0637499, -0.025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.90473, 
    farPlane=1.46275, cameraPosition=(0.617659, 0.38061, -0.972084), 
    cameraUpVector=(-0.358847, 0.908021, 0.216163), cameraTarget=(0.0637499, 
    -0.0637499, -0.025))
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
v, e1 = p.vertices, p.edges
p.DatumCsysByThreePoints(point2=v[96], name='cyl-coordinates', 
    coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0), 
    point1=p.InterestingPoint(edge=e1[106], rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.88244, 
    farPlane=1.48504, cameraPosition=(1.07702, 0.138777, -0.602503), 
    cameraUpVector=(-0.0854901, 0.977504, 0.192816), cameraTarget=(0.0637499, 
    -0.0637499, -0.025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.918801, 
    farPlane=1.44868, cameraPosition=(0.987153, -0.108236, 0.714318), 
    cameraUpVector=(0.0293906, 0.999294, 0.0234136), cameraTarget=(0.0637499, 
    -0.0637499, -0.025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.959279, 
    farPlane=1.4082, cameraPosition=(0.728737, -0.076174, 0.954225), 
    cameraUpVector=(-0.0204312, 0.999439, 0.02655), cameraTarget=(0.0637499, 
    -0.0637499, -0.025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.00584, 
    farPlane=1.36165, cameraPosition=(0.182529, 0.186044, 1.12597), 
    cameraUpVector=(-0.0761717, 0.97601, -0.203966), cameraTarget=(0.0637499, 
    -0.0637499, -0.025))
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-45')
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[8], )
region = regionToolset.Region(referencePoints=refPoints1)
datum = mdb.models['Model-1'].rootAssembly.instances['Wheel Centre Blank2-1'].datums[38]
mdb.models['Model-1'].ConcentratedForce(name='Force-45', 
    createStepName='torque-45', region=region, cf1=1.0, 
    distributionType=UNIFORM, field='', localCsys=datum)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.944928, 
    farPlane=1.42256, width=0.593185, height=0.360991, cameraPosition=(
    0.736863, 0.0322259, 0.943998), cameraUpVector=(0.135168, 0.972395, 
    -0.190206), cameraTarget=(0.06375, -0.06375, -0.0250001))
mdb.models['Model-1'].loads['Force-45'].setValues(cf1=-1500.0, cf2=2165.0, 
    distributionType=UNIFORM, field='')
del mdb.models['Model-1'].loads['Force-0']
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-0')
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[7], )
region = regionToolset.Region(referencePoints=refPoints1)
datum = mdb.models['Model-1'].rootAssembly.instances['Wheel Centre Blank2-1'].datums[38]
mdb.models['Model-1'].ConcentratedForce(name='Force-0', 
    createStepName='torque-0', region=region, cf1=-1500.0, cf2=2165.0, 
    distributionType=UNIFORM, field='', localCsys=datum)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-90')
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[9], )
region = regionToolset.Region(referencePoints=refPoints1)
datum = mdb.models['Model-1'].rootAssembly.instances['Wheel Centre Blank2-1'].datums[38]
mdb.models['Model-1'].ConcentratedForce(name='Force-90', 
    createStepName='torque-90', region=region, cf1=-1500.0, cf2=2165.0, 
    distributionType=UNIFORM, field='', localCsys=datum)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='pos-axial-90')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
del mdb.models['Model-1'].steps['neg-axial-90']
del mdb.models['Model-1'].steps['neg-axial-45']
del mdb.models['Model-1'].steps['neg-axial-0']
del mdb.models['Model-1'].steps['pos-axial-0']
del mdb.models['Model-1'].steps['pos-axial-45']
del mdb.models['Model-1'].steps['pos-axial-90']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-45')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].loads['Force-0'].setValuesInStep(stepName='torque-45', 
    cf1=0.0, cf2=0.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-90')
mdb.models['Model-1'].loads['Force-45'].setValuesInStep(stepName='torque-90', 
    cf1=0.0, cf2=0.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Model2-test', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', multiprocessingMode=DEFAULT, numCpus=4, numDomains=4, 
    numGPUs=0)
mdb.jobs['Model2-test'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Model2-test.inp" has been submitted for analysis.
#: Error in job Model2-test: SYSTEM ERROR IN PRE_NRCOUPLING - NO ENTRY FOR REFERENCE NODE 1 (ASSEMBLY).
#: Job Model2-test: Analysis Input File Processor aborted due to errors.
#: Error in job Model2-test: Analysis Input File Processor exited with an error.
#: Job Model2-test aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.95935, 
    farPlane=1.40814, width=0.602239, height=0.366501, cameraPosition=(
    0.690726, -0.114901, 0.977764), cameraUpVector=(0.363394, 0.913965, 
    -0.18059), cameraTarget=(0.06375, -0.06375, -0.0250001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.889943, 
    farPlane=1.47755, width=0.558668, height=0.339985, cameraPosition=(1.22099, 
    0.101035, 0.161814), cameraUpVector=(-0.120557, 0.985158, -0.122191), 
    cameraTarget=(0.06375, -0.06375, -0.0250002))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.993101, 
    farPlane=1.37439, width=0.623426, height=0.379395, cameraPosition=(
    0.535089, -0.129205, -1.10889), cameraUpVector=(-0.505512, 0.819708, 
    -0.269327), cameraTarget=(0.06375, -0.06375, -0.0250002))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.914341, 
    farPlane=1.45316, width=0.573984, height=0.349306, cameraPosition=(
    0.00263345, -1.07528, -0.636829), cameraUpVector=(-0.40056, 0.491812, 
    -0.773093), cameraTarget=(0.0637498, -0.0637503, -0.0250001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.02602, 
    farPlane=1.34148, width=0.644091, height=0.391971, cameraPosition=(
    0.155703, 0.166383, -1.18252), cameraUpVector=(-0.0106703, 0.980909, 
    0.194173), cameraTarget=(0.0637498, -0.06375, -0.0250002))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.874588, 
    farPlane=1.49292, width=0.549029, height=0.334119, cameraPosition=(
    0.659021, 0.588281, -0.813528), cameraUpVector=(-0.316697, 0.834476, 
    0.450947), cameraTarget=(0.0637499, -0.0637499, -0.0250001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.882447, 
    farPlane=1.48506, width=0.553963, height=0.337122, viewOffsetX=0.0109034, 
    viewOffsetY=0.0165049)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Wheel Centre Blank2-1', 'RP-4', 'RP-3', 'RP-2', 'RP-1', ))
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Wheel Centre Blank2']
a1.Instance(name='Wheel Centre Blank2-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.954836, 
    farPlane=1.53861, width=0.729704, height=0.444072, cameraPosition=(1.19536, 
    -0.175159, -0.536263), cameraUpVector=(-0.310848, 0.947343, -0.0769113), 
    cameraTarget=(0.0752714, -0.0679624, -0.032309))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.979498, 
    farPlane=1.5159, width=0.748552, height=0.455542, cameraPosition=(0.882673, 
    -0.241245, -0.949457), cameraUpVector=(-0.134409, 0.980174, 0.145582), 
    cameraTarget=(0.071805, -0.068695, -0.0368896))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
d11 = a.instances['Wheel Centre Blank2-1'].datums
a.ReferencePoint(point=d11[34])
a = mdb.models['Model-1'].rootAssembly
d21 = a.instances['Wheel Centre Blank2-1'].datums
a.ReferencePoint(point=d21[36])
a = mdb.models['Model-1'].rootAssembly
d11 = a.instances['Wheel Centre Blank2-1'].datums
a.ReferencePoint(point=d11[35])
a = mdb.models['Model-1'].rootAssembly
e21 = a.instances['Wheel Centre Blank2-1'].edges
a.ReferencePoint(point=a.instances['Wheel Centre Blank2-1'].InterestingPoint(
    edge=e21[13], rule=CENTER))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.jobs['Model2-test'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Model2-test.inp".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[25], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].constraints['RP1-perimeter'].setValues(
    controlPoint=region1)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[26], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].constraints['RP2-perimeter'].setValues(
    controlPoint=region1)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[27], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].constraints['RP3-perimeter'].setValues(
    controlPoint=region1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.999589, 
    farPlane=1.4958, width=0.499791, height=0.304155, viewOffsetX=0.0118721, 
    viewOffsetY=0.0142997)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[28], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].constraints['RP-4-centre-hole'].setValues(
    controlPoint=region1)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-0')
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.981546, 
    farPlane=1.51385, width=0.720413, height=0.438418, viewOffsetX=0.0389784, 
    viewOffsetY=0.0305394)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[25], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].loads['Force-0'].setValues(region=region, 
    distributionType=UNIFORM, field='')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-45')
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[26], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].loads['Force-45'].setValues(region=region, 
    distributionType=UNIFORM, field='')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-90')
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[27], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].loads['Force-90'].setValues(region=region, 
    distributionType=UNIFORM, field='')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Model2-test'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Model2-test.inp".
mdb.jobs['Model2-test'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Model2-test.inp" has been submitted for analysis.
#: Error in job Model2-test: SYSTEM ERROR IN PRE_NRCOUPLING - NO ENTRY FOR REFERENCE NODE 1 (ASSEMBLY).
#: Job Model2-test: Analysis Input File Processor aborted due to errors.
#: Error in job Model2-test: Analysis Input File Processor exited with an error.
#: Job Model2-test aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.01421, 
    farPlane=1.48118, width=0.342824, height=0.178857, viewOffsetX=0.0246342, 
    viewOffsetY=0.0463632)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.0834, 
    farPlane=1.46262, width=0.36621, height=0.191058, cameraPosition=(0.568568, 
    0.126676, -1.17804), cameraUpVector=(-0.219333, 0.879627, 0.422077), 
    cameraTarget=(0.0834133, -0.0632619, -0.0606279), viewOffsetX=0.0263147, 
    viewOffsetY=0.0495259)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.02576, 
    farPlane=1.52027, width=0.991769, height=0.517422, viewOffsetX=0.069594, 
    viewOffsetY=0.0566845)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.877649, 
    farPlane=1.52809, width=0.84857, height=0.442713, cameraPosition=(1.1359, 
    -0.263941, -0.533388), cameraUpVector=(-0.139133, 0.978077, 0.154945), 
    cameraTarget=(0.0433139, -0.0851287, 0.00915532), viewOffsetX=0.0595455, 
    viewOffsetY=0.0485)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.858436, 
    farPlane=1.46977, width=0.829994, height=0.433022, cameraPosition=(1.13396, 
    -0.177096, 0.421266), cameraUpVector=(-0.217801, 0.9651, -0.145416), 
    cameraTarget=(-0.017092, -0.0758186, -0.00873833), viewOffsetX=0.058242, 
    viewOffsetY=0.0474383)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.846435, 
    farPlane=1.49094, width=0.818391, height=0.426968, cameraPosition=(
    0.671613, 0.483176, 0.811446), cameraUpVector=(-0.423797, 0.666239, 
    -0.613614), cameraTarget=(-0.00341462, -0.108064, -0.0340447), 
    viewOffsetX=0.0574278, viewOffsetY=0.0467751)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.882926, 
    farPlane=1.4259, width=0.853673, height=0.445375, cameraPosition=(0.52147, 
    0.284003, 0.977397), cameraUpVector=(-0.310287, 0.786807, -0.533532), 
    cameraTarget=(-0.00795234, -0.108915, -0.0644331), viewOffsetX=0.0599036, 
    viewOffsetY=0.0487916)
mdb.models['Model-1'].constraints['RP2-perimeter'].suppress()
mdb.models['Model-1'].constraints['RP3-perimeter'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
mdb.models['Model-1'].loads['Force-45'].suppress()
mdb.models['Model-1'].loads['Force-90'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='torque-45')
mdb.models['Model-1'].steps['torque-45'].suppress()
mdb.models['Model-1'].steps['torque-90'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Model2-test'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Model2-test.inp" has been submitted for analysis.
#: Job Model2-test: Analysis Input File Processor completed successfully.
#: Job Model2-test: Abaqus/Standard completed successfully.
#: Job Model2-test completed successfully. 
mdb.jobs['Model2-test'].submit(consistencyChecking=OFF)
#: The job input file "Model2-test.inp" has been submitted for analysis.
#: Job Model2-test: Analysis Input File Processor completed successfully.
#: Job Model2-test: Abaqus/Standard completed successfully.
#: Job Model2-test completed successfully. 
o3 = session.openOdb(
    name='/home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Abaqus Files/Model2-test.odb')
#: Model: /home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Abaqus Files/Model2-test.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       9
#: Number of Node Sets:          11
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FEATURE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.80382, 
    farPlane=1.27279, width=0.767769, height=0.400558, cameraPosition=(
    0.484525, 0.0899724, 0.87987), cameraUpVector=(-0.410758, 0.858413, 
    -0.307252), cameraTarget=(0.00465599, -0.0615885, -0.0312684))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.84468, 
    farPlane=1.23014, width=0.806796, height=0.420919, cameraPosition=(
    0.311655, -0.0768136, 0.963105), cameraUpVector=(-0.343103, 0.911014, 
    -0.228766), cameraTarget=(0.00508359, -0.061176, -0.0314743))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.animationController.animationOptions.setValues(mode=SWING, 
    frameRate=53)
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.794041, 
    farPlane=1.28863, width=0.669043, height=0.349051, cameraPosition=(0.67166, 
    -0.158614, 0.763142), cameraUpVector=(0.308738, 0.940302, -0.143222))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.830718, 
    farPlane=1.32561, width=0.808692, height=0.421908, cameraPosition=(
    0.626621, -0.205889, 0.838065), cameraUpVector=(-0.252619, 0.964777, 
    -0.0734092), cameraTarget=(0.00333652, -0.0627142, -0.0295323))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.862739, 
    farPlane=1.29359, width=0.431191, height=0.22496, viewOffsetX=-0.0123742, 
    viewOffsetY=0.0209376)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.859011, 
    farPlane=1.32152, width=0.429328, height=0.223988, cameraPosition=(0.36912, 
    0.335719, 0.92112), cameraUpVector=(-0.459778, 0.724411, -0.513646), 
    cameraTarget=(0.0121285, -0.0593665, -0.0159884), viewOffsetX=-0.0123208, 
    viewOffsetY=0.0208471)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=WIREFRAME, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.845507, 
    farPlane=1.31829, width=0.422579, height=0.220467, cameraPosition=(
    0.819238, 0.13024, 0.653916), cameraUpVector=(-0.29289, 0.853867, 
    -0.430264), cameraTarget=(0.00541277, -0.0697001, -0.0238901), 
    viewOffsetX=-0.0121271, viewOffsetY=0.0205194)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.848102, 
    farPlane=1.29379, width=0.423877, height=0.221144, cameraPosition=(
    0.607687, -0.260313, -0.883527), cameraUpVector=(-0.0596502, 0.98606, 
    0.155331), cameraTarget=(-0.0227355, -0.0684534, -0.0306106), 
    viewOffsetX=-0.0121643, viewOffsetY=0.0205824)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.828046, 
    farPlane=1.32375, width=0.413854, height=0.215914, cameraPosition=(0.76335, 
    0.214701, -0.732397), cameraUpVector=(-0.383884, 0.818785, 0.426878), 
    cameraTarget=(-0.0141061, -0.0706549, -0.0425829), viewOffsetX=-0.0118766, 
    viewOffsetY=0.0200957)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.835577, 
    farPlane=1.31622, width=0.348188, height=0.181656, viewOffsetX=-0.0198852, 
    viewOffsetY=0.0414798)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.84108, 
    farPlane=1.28783, width=0.350481, height=0.182852, cameraPosition=(1.02705, 
    -0.333983, -0.0384546), cameraUpVector=(-0.0992133, 0.955788, 0.276814), 
    cameraTarget=(-0.0158018, -0.062034, -0.053324), viewOffsetX=-0.0200162, 
    viewOffsetY=0.0417529)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.847126, 
    farPlane=1.32687, width=0.353001, height=0.184167, cameraPosition=(
    0.846775, 0.186582, 0.60949), cameraUpVector=(-0.449047, 0.832058, 
    -0.325633), cameraTarget=(0.0236035, -0.0777598, -0.0341164), 
    viewOffsetX=-0.0201601, viewOffsetY=0.0420531)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.828471, 
    farPlane=1.35994, width=0.345228, height=0.180111, cameraPosition=(
    0.720981, 0.414078, 0.647899), cameraUpVector=(-0.512094, 0.690752, 
    -0.510511), cameraTarget=(0.0307094, -0.0724891, -0.0217982), 
    viewOffsetX=-0.0197161, viewOffsetY=0.041127)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=HIDDEN, )
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=FILLED, )
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=SHADED, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.815102, 
    farPlane=1.37331, width=0.508767, height=0.265432, viewOffsetX=-0.0260978, 
    viewOffsetY=0.0241403)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.801198, 
    farPlane=1.38722, width=0.663563, height=0.346192, viewOffsetX=-0.0145035, 
    viewOffsetY=0.0176284)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.840239, 
    farPlane=1.34885, width=0.695897, height=0.363061, cameraPosition=(0.5252, 
    -0.39801, 0.872003), cameraUpVector=(-0.253977, 0.963715, 0.0821561), 
    cameraTarget=(0.0262955, -0.0798886, -0.0288915), viewOffsetX=-0.0152102, 
    viewOffsetY=0.0184874)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.899063, 
    farPlane=1.29014, width=0.744616, height=0.388479, cameraPosition=(
    -0.0245607, -0.334748, 1.03337), cameraUpVector=(-0.198296, 0.97325, 
    -0.116032), cameraTarget=(0.0225629, -0.0807522, -0.0130461), 
    viewOffsetX=-0.0162751, viewOffsetY=0.0197817)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.887693, 
    farPlane=1.30153, width=0.7352, height=0.383566, cameraPosition=(-0.360488, 
    -0.14917, 1.00459), cameraUpVector=(-0.0997409, 0.939457, -0.327831), 
    cameraTarget=(0.0162362, -0.0782713, -0.00277239), viewOffsetX=-0.0160693, 
    viewOffsetY=0.0195315)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
mdb.save()
#: The model database has been saved to "/home/s1208454/FEMSS4/My_Stuff/Kick Ass Wheel Centre/Abaqus Files/2nd_attempt.cae".
