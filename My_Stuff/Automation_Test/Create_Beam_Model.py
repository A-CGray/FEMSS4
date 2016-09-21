#================================ Set Variables ================================
Beam_Length = 1 # Beam Length in m
Beam_Height = 0.1 # Beam Height in m
Beam_Width = 0.1 # Beam Width in m
Material = 'Steel' # Material Name
Youngs_mod = 200*10**9 # Young's modulus in N/m^2
Poissons_ratio = 0.3 # Poisson ratio
Tip_Load = 20000 # Total tip load in N
L_Mesh_Points = 5 # Mesh points along beam length
H_Mesh_Points = 4 # Mesh points along height
Mesh_Type = 'Quad' # Mesh order ('Lin' for Linear or 'Quad' for Quadratic)
Name = '2D_' + str(Beam_Length) + 'x' + str(Beam_Height) + 'x' + str(Beam_Width) + '_Cantilever_' + str(\
    L_Mesh_Points) + 'x' + str(H_Mesh_Points) + '_' + str(Mesh_Type) + '_Mesh_' + str(Tip_Load) + 'N_Tip_Load'
#===============================================================================
# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import inspect, os
#================================ Save CAE File ================================
Parent = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # Set location of python file as parent directory
Child = Parent + '/' + Name # Create parameter specific subfolder
if not os.path.exists(Child): # Create subfolder if it doesn't already exist
    os.makedirs(Child)
os.chdir(Child)
mdb.saveAs(pathName=Child + '/' + Name + '.cae') # Save CAE File in subfolder
#================================ Create Part ================================
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0),
    point2=(Beam_Length, Beam_Height))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Beam', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Beam'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
#================================ Create Material and Section ================================
mdb.models['Model-1'].Material(name=Material)
mdb.models['Model-1'].materials[Material].Elastic(table=((Youngs_mod, Poissons_ratio),
    ))
mdb.models['Model-1'].HomogeneousSolidSection(material=Material, name=Material,
    thickness=Beam_Width)
#================================ Assign Section ================================
mdb.models['Model-1'].parts['Beam'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=Region(
    faces=mdb.models['Model-1'].parts['Beam'].faces.getSequenceFromMask(mask=(
    '[#1 ]', ), )), sectionName=Material, thicknessAssignment=FROM_SECTION)
#================================ Create Assembly ================================
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Beam-1', part=
    mdb.models['Model-1'].parts['Beam'])
#================================ Create General Static Step ================================
mdb.models['Model-1'].StaticStep(description='Tip Load', name='Step-1',
    previous='Initial')
#================================ Create BC's ================================
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Beam-1'].edges.getSequenceFromMask(
    ('[#8 ]', ), ), name='Fixed_End')
mdb.models['Model-1'].EncastreBC(createStepName='Step-1', localCsys=None, name=
    'Cantilever_Fixed', region=
    mdb.models['Model-1'].rootAssembly.sets['Fixed_End']) # Assign the fixed end to a set called Fixed_End

mdb.models['Model-1'].rootAssembly.Set(name='Load_Points', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Beam-1'].vertices.getSequenceFromMask(
    ('[#6 ]', ), ))
mdb.models['Model-1'].ConcentratedForce(cf2=-Tip_Load/2, createStepName='Step-1',
    distributionType=UNIFORM, field='', localCsys=None, name='Tip_Load',
    region=mdb.models['Model-1'].rootAssembly.sets['Load_Points'])
#================================ Create Mesh ================================
mdb.models['Model-1'].parts['Beam'].seedEdgeByNumber(constraint=FINER, edges=
    mdb.models['Model-1'].parts['Beam'].edges.getSequenceFromMask(('[#a ]', ),
    ), number=H_Mesh_Points)
mdb.models['Model-1'].parts['Beam'].seedEdgeByNumber(constraint=FINER, edges=
    mdb.models['Model-1'].parts['Beam'].edges.getSequenceFromMask(('[#5 ]', ),
    ), number=L_Mesh_Points)

if Mesh_Type == 'Lin':
    mdb.models['Model-1'].parts['Beam'].setElementType(elemTypes=(ElemType(
        elemCode=CPS4R, elemLibrary=STANDARD, secondOrderAccuracy=OFF,
        hourglassControl=DEFAULT, distortionControl=DEFAULT), ElemType(
        elemCode=CPS3, elemLibrary=STANDARD)), regions=(
        mdb.models['Model-1'].parts['Beam'].faces.getSequenceFromMask(('[#1 ]', ),
        ), ))
elif Mesh_Type == 'Quad':
    mdb.models['Model-1'].parts['Beam'].setElementType(elemTypes=(ElemType(
        elemCode=CPS8R, elemLibrary=STANDARD), ElemType(elemCode=CPS6M,
        elemLibrary=STANDARD)), regions=(
        mdb.models['Model-1'].parts['Beam'].faces.getSequenceFromMask(('[#1 ]', ),
        ), ))
mdb.models['Model-1'].parts['Beam'].generateMesh()

#================================ Create Field Output and Job ================================
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'MISES', 'E', 'EE', 'U', 'UT', 'UR', 'RF', 'RT', 'RM', 'CF'))

mdb.models['Model-1'].rootAssembly.regenerate()
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF,
    multiprocessingMode=DEFAULT, name='2D_Cantilever', nodalOutputPrecision=SINGLE,
    numCpus=1, numGPUs=0, queue=None, scratch='', type=ANALYSIS,
    userSubroutine='', waitHours=0, waitMinutes=0)
#================================ Submit Job ================================
mdb.saveAs(pathName=Child + '/' + Name + '.cae')
mdb.jobs['2D_Cantilever'].submit(consistencyChecking=OFF)
mdb.jobs['2D_Cantilever'].waitForCompletion()
mdb.saveAs(pathName=Child + '/' + Name + '.cae')
# #================================ Visualisation ================================
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=98.7174224853516,
    height=109.567710876465)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o1 = session.openOdb(name=Child + '/2D_Cantilever.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
### CREATE OUTPUT ###
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.printToFile(fileName=Name + '_Stress.tiff', format=TIFF, canvasObjects=(
session.viewports['Viewport: 1'], ))

session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT,
    'Magnitude'), )
session.printToFile(fileName=Name + '_Displacement.tiff', format=TIFF, canvasObjects=(
session.viewports['Viewport: 1'], ))