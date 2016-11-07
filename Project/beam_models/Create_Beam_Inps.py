from beam_input_generator import beam_input_generator
import os
import subprocess
mesh_size = [2,10]
element = ['B23', 'B22', 'B21']
beam_type = ['thin', 'thick']
filepath = os.path.dirname(os.path.realpath(__file__))
batch = open('run_beam_models.bat', 'w')
for n in mesh_size:
    for type in element:
        for beam in beam_type:
            filename = beam_input_generator(type, n, beam)
            batch.write('cd ' + filepath + '\\'  + filename + '& ')
            batch.write('echo Running next simulation & ')
            batch.write('abaqus job=' + filename + ' interactive & ')
batch.write('PAUSE')
batch.close()
