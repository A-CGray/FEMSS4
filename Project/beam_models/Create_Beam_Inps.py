from beam_input_generator import beam_input_generator # Import input file writing function
import os # import the os library will allow the loop to create subfolders
mesh_size = [2,10] # define the range of mesh sizes
element = ['B23', 'B22', 'B21'] # define the range of element types
beam_type = ['thin', 'thick'] # define the two beam sizes
filepath = os.path.dirname(os.path.realpath(__file__)) # get the location the script is being run from
batch = open('run_beam_models.bat', 'w') # create a new batch file
for n in mesh_size: # for each mesh size
    for type in element: # for each element type
        for beam in beam_type: # for each beam size
            filename = beam_input_generator(type, n, beam) # create the input file
            # the input file writing function creates a subfolder in the run directory so the first part of the batch
            #  command needs to move the computer to this directory
            batch.write('cd ' + filepath + '\\'  + filename + '& ')
            # Tell the batch file to print a statement at the start of each simulation
            batch.write('echo Running next simulation & ')
            # Run the simulation
            batch.write('abaqus job=' + filename + ' interactive & ')
batch.write('PAUSE')
batch.close()
