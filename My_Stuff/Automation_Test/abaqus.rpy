# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_16-03.28.56 126354
# Run by Ali on Mon Sep 12 17:16:47 2016
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.25915, 1.25651), width=185.347, 
    height=124.646)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('Create_Beam_Model.py', __main__.__dict__)
#: The model database has been saved to "C:\Users\Ali\Documents\MEGA\University\5th Year\FEM 4\My_Stuff\Automation_Test\2D_1x0.1x0.1_Cantilever_5x4QuadMesh_20000N_Tip_Load\2D_1x0.1x0.1_Cantilever_5x4QuadMesh_20000N_Tip_Load.cae".
#: The model database has been saved to "C:\Users\Ali\Documents\MEGA\University\5th Year\FEM 4\My_Stuff\Automation_Test\2D_1x0.1x0.1_Cantilever_5x4QuadMesh_20000N_Tip_Load\2D_1x0.1x0.1_Cantilever_5x4QuadMesh_20000N_Tip_Load.cae".
#: The model database has been saved to "C:\Users\Ali\Documents\MEGA\University\5th Year\FEM 4\My_Stuff\Automation_Test\2D_1x0.1x0.1_Cantilever_5x4QuadMesh_20000N_Tip_Load\2D_1x0.1x0.1_Cantilever_5x4QuadMesh_20000N_Tip_Load.cae".
#: Model: C:/Users/Ali/Documents/MEGA/University/5th Year/FEM 4/My_Stuff/Automation_Test/2D_1x0.1x0.1_Cantilever_5x4QuadMesh_20000N_Tip_Load/2D_Cantilever.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          3
#: Number of Steps:              1
print 'RT script done'
#: RT script done
